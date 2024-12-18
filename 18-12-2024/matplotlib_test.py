import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Beispiel-Daten erstellen
x = np.linspace(0, 10, 100)  # Werte von 0 bis 10, 100 Punkte
y = np.sin(x)                # Sinus-Funktion für die y-Werte
z = np.cos(x)                # Kosinus-Funktion für die z-Werte

# Plot erstellen
fig, ax = plt.subplots(figsize=(8, 5))
fig.canvas.manager.set_window_title('Beispiel mit matplotlib (Marcel Dorr)')
line, = ax.plot(x, y, label='sin(x)', color='blue', linewidth=2)
line2, = ax.plot(x, z, label='cos(x)', color='red', linewidth=2)

# Titel und Achsenbeschriftungen hinzufügen
ax.set_xlabel('x-Werte', fontsize=12)
ax.set_ylabel('y-Werte', fontsize=12)
ax.legend(fontsize=12)
ax.grid(True, linestyle='--', alpha=0.7)

# Funktion zur Aktualisierung der Animation
def update(frame):
    line.set_ydata(np.sin(x + frame / 40))  # Verschieben der Sinuskurve
    line2.set_ydata(np.cos(x + frame / 40)) # Verschieben der Kosinuskurve
    return line, line2

# Animation erstellen
ani = FuncAnimation(fig, update, frames=100, interval=50, blit=True)

# Plot anzeigen
plt.show()