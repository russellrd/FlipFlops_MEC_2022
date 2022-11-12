import tkinter as tk
from PIL import ImageTk, Image
from tkinter import StringVar, ttk
import accelerometer
import gyroscope

root = tk.Tk()
root.title("Ocean Current Detection (OCD)")
root.resizable(False, False)
frame = ttk.Frame(root)
frame.grid()

green = ImageTk.PhotoImage(Image.open("images/green.png"))
red = ImageTk.PhotoImage(Image.open("images/red.png"))

acc_velocity_var = StringVar()
acc_velocity_var.set(0)
acc_acceleration_var = StringVar()
acc_acceleration_var.set(0)

ttk.Label(frame, text="Ocean Current Detection (OCD)", font='Helvetica 18 bold').grid(columnspan=5)
ttk.Label(frame, text="Accelerometer", font='Helvetica 14 bold').grid(column=0, row=1, padx=10, pady=10)
accOn = ttk.Label(frame, image=red).grid(column=1, row=1, padx=10, pady=10)
ttk.Label(frame, text="Gyroscope", font='Helvetica 14 bold').grid(column=3, row=1, padx=10, pady=10)
gyro = ttk.Label(frame, image=red).grid(column=4, row=1, padx=10, pady=10)
ttk.Label(frame, text="Velocity: ", font='Helvetica 12 bold').grid(column=0, row=2, padx=10, pady=10)
ttk.Label(frame, textvariable=acc_velocity_var, font='Helvetica 12').grid(column=1, row=2, padx=10, pady=10)
ttk.Label(frame, text="Acceleration: ", font='Helvetica 12 bold').grid(column=0, row=3, padx=10, pady=10)
ttk.Label(frame, textvariable=acc_acceleration_var, font='Helvetica 12').grid(column=1, row=3, padx=10, pady=10)

def update():
    # Update the sensor data
    accData = Accelerometer.update()
    gyroData = Gyroscope.update()

    # Update accelerometer "on" icon
    if(accData["on"] == True):
        accOn.configure(image=green)
        accOn.image = green
    else:
        accOn.configure(image=red)
        accOn.image = red

    # Update gyroscope "on" icon
    if(gyroData["on"] == True):
        gyro.configure(image=green)
        gyro.image = green
    else:
        gyro.configure(image=red)
        gyro.image = red

    # Update the labels
    ttk.Label(frame, text="")

    # Update the GUI
    root.after(100, update)

root.mainloop()