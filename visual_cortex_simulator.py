import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

root = tk.Tk()
root.title("Visual Cortex Receptive Field Simulator")
root.geometry("600x500")

fig, ax = plt.subplots(figsize=(4, 4))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

def gabor_patch(orientation, frequency, contrast):
    x = np.linspace(-2, 2, 200)
    y = np.linspace(-2, 2, 200)
    X, Y = np.meshgrid(x, y)
    theta = np.deg2rad(orientation)
    x_theta = X * np.cos(theta) + Y * np.sin(theta)
    return contrast * np.exp(-(X**2 + Y**2)) * np.cos(2 * np.pi * frequency * x_theta)

def update_plot(val=None):
    ax.clear()
    img = gabor_patch(orientation.get(), frequency.get(), contrast.get())
    ax.imshow(img, cmap='gray', extent=(-2, 2, -2, 2))
    ax.set_title("Neuron Response Pattern")
    ax.axis('off')
    canvas.draw()

orientation = tk.Scale(root, from_=0, to=180, orient='horizontal', label='Orientation', command=update_plot)
orientation.pack(fill='x')

frequency = tk.Scale(root, from_=1, to=10, orient='horizontal', label='Frequency', command=update_plot)
frequency.pack(fill='x')

contrast = tk.Scale(root, from_=0, to=1, resolution=0.1, orient='horizontal', label='Contrast', command=update_plot)
contrast.pack(fill='x')

update_plot()
root.mainloop()
