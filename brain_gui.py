# 🧠 Brain Signal Visualizer
# A simple Tkinter GUI that plots a simulated EEG signal (alpha or beta wave)

import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt


def simulate_wave(frequency=10, color='purple', title='Alpha Wave (10Hz)'):
    """Simulate and display an EEG-like signal."""
    t = np.linspace(0, 1, 250, endpoint=False)
    eeg = 50 * np.sin(2 * np.pi * frequency * t) + 20 * np.random.randn(len(t))

    plt.figure(figsize=(6, 3))
    plt.plot(t, eeg, color=color)
    plt.title(f"Simulated EEG Signal — {title}")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude (µV)")
    plt.tight_layout()
    plt.show()


def build_gui():
    """Construct and display the main window."""
    window = tk.Tk()
    window.title("🧠 Neuroscience: Brain Signal Visualizer")
    window.geometry("430x230")

    label = tk.Label(window, text="Brain Signal Visualizer", font=("Helvetica", 16, "bold"))
    label.pack(pady=15)

    alpha_button = tk.Button(window, text="Simulate Alpha Wave (10Hz)",
                             command=lambda: simulate_wave(10, 'purple', 'Alpha Wave (10Hz)'),
                             width=30, height=2, bg="#d1c4e9")
    alpha_button.pack(pady=5)

    beta_button = tk.Button(window, text="Simulate Beta Wave (20Hz)",
                            command=lambda: simulate_wave(20, 'blue', 'Beta Wave (20Hz)'),
                            width=30, height=2, bg="#bbdefb")
    beta_button.pack(pady=5)

    quit_button = tk.Button(window, text="Quit", command=window.destroy,
                            width=20, height=1, bg="#ffcdd2")
    quit_button.pack(pady=10)

    return window


def main():
    window = build_gui()
    window.mainloop()


if __name__ == "__main__":
    main()
