import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# 🧠 Step 1: Create main window
root = tk.Tk()
root.title("Neuroscience: Brain Signal Visualizer")
root.geometry("700x500")
root.config(bg="#0d1117")

# 🧩 Step 2: Create Matplotlib figure
fig, ax = plt.subplots(figsize=(6, 4))
ax.set_facecolor("black")
ax.set_title("Brainwave Signal", color="white")
ax.set_xlabel("Time (s)", color="white")
ax.set_ylabel("Amplitude", color="white")
ax.tick_params(colors="white")

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(pady=20)

# 🎛 Step 3: Define a function to generate signals
def generate_wave(freq, color):
    t = np.linspace(0, 1, 1000)
    # Add random noise to simulate real EEG signal
    noise = 0.3 * np.random.randn(1000)
    y = np.sin(2 * np.pi * freq * t) + noise
    ax.clear()
    ax.plot(t, y, color=color)
    ax.set_title(f"{freq}Hz Brainwave", color="white")
    ax.set_xlabel("Time (s)", color="white")
    ax.set_ylabel("Amplitude", color="white")
    ax.set_facecolor("black")
    ax.tick_params(colors="white")
    canvas.draw()

# 🎚 Step 4: Add buttons
frame = ttk.Frame(root)
frame.pack(pady=10)

ttk.Button(frame, text="Alpha (10Hz)", command=lambda: generate_wave(10, "green")).grid(row=0, column=0, padx=5)
ttk.Button(frame, text="Beta (20Hz)", command=lambda: generate_wave(20, "blue")).grid(row=0, column=1, padx=5)
ttk.Button(frame, text="Gamma (40Hz)", command=lambda: generate_wave(40, "orange")).grid(row=0, column=2, padx=5)

# 🧠 Step 5: Run main loop
root.mainloop()
