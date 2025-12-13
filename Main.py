import threading
import time
import random
import tkinter as tk


# ============== MULTITHREADING ==============

class Parcheggio:
    def __init__(self):
        self.reset()

    def reset(self):
        # reset completo del parcheggio
        self.semaforo_posti = threading.Semaphore(10)
        self.semaforo_coda = threading.Semaphore(5)
        self.lock = threading.Lock()
        self.posti = [False] * 10
        self.coda = 0
        self.running = False

    def trova_posto(self):
        # ricerca del primo posto libero nell'array
        self.lock.acquire()
        posto = -1
        for i in range(10):
            if not self.posti[i]:
                self.posti[i] = True
                posto = i
                break
        self.lock.release()
        return posto

    def libera_posto(self, posto):
        # procedura per liberare un posto occupato
        self.lock.acquire()
        self.posti[posto] = False
        self.lock.release()

    def incrementa_coda(self):
        # procedura per aggiungere un'auto alla coda
        self.lock.acquire()
        self.coda += 1
        self.lock.release()

    def decrementa_coda(self):
        # procedura per rimuovere un'auto dalla coda
        self.lock.acquire()
        self.coda -= 1
        self.lock.release()


class Auto:
    def __init__(self, id, parcheggio, log_fn, aggiorna_coda_fn):
        self.id = id
        self.parcheggio = parcheggio
        self.log_fn = log_fn
        self.aggiorna_coda_fn = aggiorna_coda_fn

    def parcheggia(self):
        # controllo se la simulazione è ancora attiva
        if not self.parcheggio.running:
            return

        self.log_fn(f"> Auto {self.id} arriva")

        # tentativo di entrare in coda (non bloccante)
        entrato = self.parcheggio.semaforo_coda.acquire(blocking=False)
        if not entrato:
            self.log_fn(f"> Auto {self.id} - CODA PIENA")
            self.log_fn("> SIMULAZIONE FERMATA\nuser@parking:~$ ")
            self.parcheggio.running = False
            return

        # controllo di nuovo se è ancora attivo
        if not self.parcheggio.running:
            self.parcheggio.semaforo_coda.release()
            return

        # incremento del contatore della coda
        self.parcheggio.incrementa_coda()
        self.aggiorna_coda_fn()

        # attesa di un posto libero (bloccante)
        self.parcheggio.semaforo_posti.acquire()

        # controllo se è stato fermato mentre aspettavo
        if not self.parcheggio.running:
            self.parcheggio.semaforo_posti.release()
            self.parcheggio.semaforo_coda.release()
            self.parcheggio.decrementa_coda()
            self.aggiorna_coda_fn()
            return

        # decremento del contatore coda
        self.parcheggio.decrementa_coda()
        self.aggiorna_coda_fn()

        # occupazione di un posto fisico
        posto = self.parcheggio.trova_posto()
        if posto == -1:
            self.parcheggio.semaforo_posti.release()
            self.parcheggio.semaforo_coda.release()
            return

        self.log_fn(f"> Auto {self.id} posto {posto + 1}")

        # rilascio del semaforo coda
        self.parcheggio.semaforo_coda.release()

        # simulazione tempo di permanenza
        time.sleep(3 + random.random() * 3)

        # liberazione del posto solo se ancora attivo
        if self.parcheggio.running:
            self.parcheggio.libera_posto(posto)
            self.log_fn(f"> Auto {self.id} esce")
            self.parcheggio.semaforo_posti.release()
        else:
            # se fermato, libero comunque le risorse
            self.parcheggio.libera_posto(posto)
            self.parcheggio.semaforo_posti.release()


# ============== GUI ==============

class GUI:
    def __init__(self):
        self.parcheggio = Parcheggio()

        self.root = tk.Tk()
        self.root.title("Parking Simulator")
        self.root.geometry("800x550")
        self.root.configure(bg='#f5f5f5')
        self.root.resizable(False, False)

        tk.Label(self.root, text="PARKING SIMULATOR",
                 font=('Arial', 20, 'bold'), bg='#f5f5f5',
                 fg='#333').pack(pady=15)

        self.crea_parcheggi()
        self.crea_terminale()
        self.aggiorna()

    def crea_parcheggi(self):
        frame = tk.Frame(self.root, bg='#f5f5f5')
        frame.pack(pady=10)

        # creazione delle label per i posti
        self.labels = []
        for i in range(10):
            lbl = tk.Label(frame, text='P', width=4, height=2,
                           bg='#4CAF50', fg='white',
                           font=('Arial', 18, 'bold'),
                           relief='flat', borderwidth=0)
            lbl.grid(row=i // 5, column=i % 5, padx=8, pady=5)
            self.labels.append(lbl)

        # label per visualizzare la coda
        self.label_coda = tk.Label(self.root, text="In coda: 0",
                                   font=('Arial', 12), bg='#f5f5f5',
                                   fg='#666')
        self.label_coda.pack(pady=5)

    def crea_terminale(self):
        tk.Label(self.root, text='Terminal - Comandi: run | stop',
                 font=('Arial', 9), bg='#f5f5f5',
                 fg='#666').pack(pady=(10, 5))

        self.term = tk.Text(self.root, height=10, width=80,
                            bg='#1a1a1a', fg='#00ff41',
                            font=('Courier', 9), insertbackground='#00ff41',
                            relief='flat', padx=10, pady=10)
        self.term.pack()

        self.term.insert('1.0', 'user@parking:~$ ')
        self.term.bind('<Return>', self.processa_comando)

    def log(self, msg):
        self.term.insert(tk.END, msg + '\n')
        self.term.see(tk.END)

    def aggiorna_coda(self):
        self.label_coda.config(text=f"In coda: {self.parcheggio.coda}")

    def genera_auto(self):
        auto_id = 1
        while self.parcheggio.running:
            auto = Auto(auto_id, self.parcheggio, self.log, self.aggiorna_coda)
            threading.Thread(target=auto.parcheggia).start()
            auto_id += 1

            # simulazione di traffico variabile con più picchi
            if random.random() < 0.4:
                # 40% picco di traffico intenso
                time.sleep(0.2 + random.random() * 0.2)
            else:
                # 60% traffico normale
                time.sleep(0.8 + random.random() * 0.8)

    def processa_comando(self, event):
        # lettura del comando utente
        testo = self.term.get('1.0', tk.END).strip().split('\n')[-1]
        cmd = testo.replace('user@parking:~$ ', '').strip()

        if cmd == 'run':
            if self.parcheggio.running:
                self.log('Già in esecuzione\nuser@parking:~$ ')
            else:
                # reset completo prima di riavviare
                self.parcheggio.reset()
                self.parcheggio.running = True
                self.log('Sistema avviato\nuser@parking:~$ ')
                # avvio del thread generatore
                threading.Thread(target=self.genera_auto).start()

        elif cmd == 'stop':
            if self.parcheggio.running:
                self.parcheggio.running = False
                self.log('Sistema fermato\nuser@parking:~$ ')
            else:
                self.log('Già fermo\nuser@parking:~$ ')

        elif cmd:
            self.log('Comandi: run | stop\nuser@parking:~$ ')

        return 'break'

    def aggiorna(self):
        # aggiornamento dello stato visuale dei posti
        for i in range(10):
            if self.parcheggio.posti[i]:
                self.labels[i].config(bg='#f44336')
            else:
                self.labels[i].config(bg='#4CAF50')
        self.root.after(100, self.aggiorna)

    def run(self):
        self.root.mainloop()

 #avvia il programma
if __name__ == "__main__":
    app = GUI()
    app.run()
