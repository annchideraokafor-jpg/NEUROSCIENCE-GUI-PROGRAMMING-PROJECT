import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Function to simulate neuron firing
def simulate_firing(intensity):
    """Generate a spiking pattern that increases with input intensity."""
    t = np.linspace(0, 1, 1000)  # 1 second simulation
    firing_rate = intensity * 20  # Convert slider value to firing frequency
    spikes = np.sin(2 * np.pi * firing_rate * t) > 0.9  # Threshold to mimic spikes
    return t, spikes

# Function to update the plot
def update_plot():
    intensity = intensity_slider.get()
    t, spikes = simulate_firing(intensity)
    ax.clear()
    ax.plot(t, spikes, color='crimson')
    ax.set_title(f"Neuron Firing Simulation (Intensity: {intensity})")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Spike (1 = fired)")
    ax.set_ylim(-0.2, 1.2)
    canvas.draw()

# Create main window
window = tk.Tk()
window.title("Neuron Firing Rate Simulator")
window.geometry("600x450")

# Label
label = tk.Label(window, text="Neuron Firing Rate Simulator", font=("Helvetica", 16, "bold"))
label.pack(pady=10)

# Slider for stimulus intensity
intensity_slider = tk.Scale(window, from_=1, to=10, orient="horizontal", label="Stimulus Intensity")
intensity_slider.pack(pady=10)

# Plot setup
fig, ax = plt.subplots(figsize=(6, 3))
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.get_tk_widget().pack()

# Buttons
simulate_button = tk.Button(window, text="Simulate Firing", command=update_plot, bg="#6A5ACD", fg="white")
simulate_button.pack(pady=10)

quit_button = tk.Button(window, text="Quit", command=window.destroy, bg="gray", fg="white")
quit_button.pack(pady=6)

# Run GUI
window.mainloop()
