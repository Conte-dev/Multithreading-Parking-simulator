# Parking Simulator

## Panoramica

Parking Simulator è un progetto Python che simula la gestione di un parcheggio a capacità limitata, con particolare attenzione alla programmazione concorrente e alla sincronizzazione tra thread.

Il sistema utilizza multithreading per rappresentare veicoli indipendenti e integra un’interfaccia grafica sviluppata con Tkinter per il monitoraggio in tempo reale dello stato del parcheggio.

## Obiettivo

L’obiettivo del progetto è dimostrare la corretta gestione di:

- concorrenza tra thread  
- risorse condivise  
- sincronizzazione tramite primitive di locking  

La simulazione riproduce scenari realistici in cui più veicoli competono per l’accesso a un numero limitato di posti auto.

## Funzionamento

Il parcheggio è composto da:

- 10 posti auto disponibili  
- coda massima di 5 veicoli  

Ogni veicolo è rappresentato da un thread indipendente e segue questo ciclo:

1. Richiesta di accesso alla coda  
2. Attesa di un posto libero  
3. Sosta per un intervallo di tempo casuale  
4. Uscita dal parcheggio e rilascio del posto  

Se la coda raggiunge la capacità massima, la simulazione viene arrestata automaticamente.

## Gestione della concorrenza

Il sistema utilizza:

- Semafori (Semaphore) per limitare l’accesso ai posti disponibili e alla coda  
- Lock (Mutex) per garantire l’accesso sicuro alle variabili condivise e prevenire race condition  

Questa combinazione assicura stabilità anche in condizioni di carico elevato.

## Interfaccia grafica

L’applicazione include una GUI sviluppata con Tkinter che permette di:

- Visualizzare lo stato dei posti in tempo reale (libero / occupato)  
- Monitorare il numero di veicoli in coda  
- Utilizzare un terminale integrato per i comandi  
- Aggiornamento automatico ogni 100 ms  

## Comandi disponibili

| Comando | Descrizione |
|---------|------------|
| run     | Avvia la simulazione e genera i veicoli |
| stop    | Arresta la simulazione |

## Requisiti

- Windows 10 / 11  
- Python 3.8 o superiore  
- Librerie standard Python:
  - threading
  - time
  - random
  - tkinter  

Non sono richiesti pacchetti esterni.

## Avvio del programma

Aprire PowerShell o Prompt dei comandi, posizionarsi nella cartella del progetto ed eseguire:
'''bash 
python parking_simulator.py
'''
## Note

Tkinter è incluso nell’installer ufficiale di Python per Windows.  
Assicurarsi che Python sia aggiunto alla variabile di ambiente PATH.
