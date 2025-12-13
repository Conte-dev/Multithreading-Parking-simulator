# 🚗 Parking Simulator

## 📖 Introduction
**Parking Simulator** is a project developed in **Python** that simulates the operation of a parking lot with limited resources, focusing on **concurrency management**. The program represents a realistic scenario in which multiple vehicles attempt to access a limited number of parking spaces simultaneously. The simulation uses **multithreading** to coordinate operations and includes a **graphical user interface (GUI)** with an integrated terminal for real-time control.

## 🎯 Project Goal
The main goal is to demonstrate the correct use of concurrency, synchronization, and shared resource management. The project allows observing how multiple threads interact without conflicts, dynamically showing the occupancy of parking spaces and the vehicle queue.

## ⚙️ How it Works
The parking lot has **10 spaces** and a **maximum queue of 5 vehicles**. Each vehicle is managed as an **independent thread**. When a car arrives, it attempts to join the queue, waits for a free space, occupies the parking spot for a simulated time, and finally frees the space upon leaving. If the queue is full, the simulation is automatically stopped to ensure system consistency.

## 🧵 Concurrency Management
Thread synchronization is handled using:
- **Semaphore**: limits the number of available parking spaces and controls the queue length.
- **Lock**: protects shared variables such as the state of the parking spaces and the queue counter.  

This approach prevents race conditions and ensures system correctness even with multiple active threads.

## 🖥️ Graphical User Interface
The GUI, built with **Tkinter**, displays in real time:
- the status of parking spaces (free or occupied)
- the number of vehicles in the queue
- a text-based terminal to enter commands

Parking spaces automatically change color to indicate availability, allowing easy monitoring of the parking lot status.

## ⌨️ Available Commands
From the integrated terminal, you can use:
- `run` → starts the simulation and generates vehicles
- `stop` → stops the simulation

## ▶️ Running the Program
To launch the simulator, run:
```bash
python parking_simulator.py
