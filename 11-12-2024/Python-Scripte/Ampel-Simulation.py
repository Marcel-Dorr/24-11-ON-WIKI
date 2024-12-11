import tkinter as tk
import time

def update_traffic_light():
    global light_state

    canvas.itemconfig(red_light, fill="gray")
    canvas.itemconfig(yellow_light, fill="gray")
    canvas.itemconfig(green_light, fill="gray")

    if light_state == "red":
        canvas.itemconfig(red_light, fill="red")
        info_label.config(text="Auto muss stehen bleiben")
        light_state = "red_yellow"
    elif light_state == "red_yellow":
        canvas.itemconfig(red_light, fill="red")
        canvas.itemconfig(yellow_light, fill="yellow")
        info_label.config(text="Auto muss stehen bleiben")
        light_state = "green"
    elif light_state == "green":
        canvas.itemconfig(green_light, fill="green")
        info_label.config(text="Auto darf fahren")
        light_state = "yellow"
    elif light_state == "yellow":
        canvas.itemconfig(yellow_light, fill="yellow")
        info_label.config(text="Auto muss stehen bleiben")
        light_state = "red"

    root.after(2000, update_traffic_light)

root = tk.Tk()
root.title("Ampel-Simulation (Marcel Dorr)")

canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

canvas.create_rectangle(150, 50, 250, 350, fill="black")
red_light = canvas.create_oval(175, 60, 225, 110, fill="gray")
yellow_light = canvas.create_oval(175, 140, 225, 190, fill="gray")
green_light = canvas.create_oval(175, 220, 225, 270, fill="gray")

info_label = tk.Label(root, text="", font=("Arial", 16))
info_label.pack(pady=20)

light_state = "red"

update_traffic_light()

root.mainloop()