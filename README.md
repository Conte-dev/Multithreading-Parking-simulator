# 🚗 Parking Simulator

## 📖 Introduction
**Parking Simulator** is a Python project that simulates a parking lot with limited spaces, focusing on **concurrent vehicle access**. Multiple vehicles are managed simultaneously using **multithreading**, and the system includes a **Tkinter GUI** with an integrated terminal to monitor and control the simulation in real time.

---

## 🎯 Project Goal
The main goal is to demonstrate proper handling of concurrency, synchronization, and shared resource management. The simulation shows how multiple threads interact safely, dynamically updating parking space occupancy and the vehicle queue.

---

## ⚙️ How It Works
- **10 parking spaces**  
- **Queue for up to 5 vehicles**  

Each vehicle is represented as an independent thread. The workflow is:
1. Vehicle attempts to join the queue.
2. Waits for a free parking space.
3. Parks for a random simulated time.
4. Leaves and frees the space.  

If the queue is full, the simulation automatically stops.

---

## 🧵 Concurrency Management
- **Semaphore**: limits the number of available parking spaces and queue length.  
- **Lock**: protects shared variables, including parking space states and the queue counter.  

This ensures safety and prevents race conditions, even with multiple threads running concurrently.

---

## 🖥️ Graphical User Interface
- Displays parking space status (green = free, red = occupied).  
- Shows number of vehicles in the queue.  
- Terminal allows `run` and `stop` commands.  
- Updates in real time every 100 ms.

---

## ⌨️ Available Commands
- `run` → starts the simulation and generates vehicles.  
- `stop` → stops the simulation.

---

## ▶️ Requirements to Run
To run this project, you need:

- **Python 3.8 or higher**
- Standard Python libraries:
  - `threading`
  - `time`
  - `random`
  - `tkinter` (usually included with Python)
- Optional: run in a terminal that supports Tkinter GUI.

### Installation Notes
- No additional installations are required if Python 3 is correctly set up.  
- On Linux, ensure Tkinter is installed (e.g., `sudo apt install python3-tk`).  
- On Windows and macOS, Tkinter comes pre-installed with Python.

---

## ▶️ Running the Program
```bash
python parking_simulator.py
