import xlrd
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import StringVar, ttk
from accelerometer import Accelerometer
from gyroscope import Gyroscope
from log import Log
from data_entry import DataEntry

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

data_workbook = xlrd.open_workbook('MEC_EXCEL.xls').sheet_by_index(0)

data = []

for i in range(1, data_workbook.nrows):
    data.append(DataEntry(data_workbook.row_values(i,0), data_workbook.row_values(i,1), data_workbook.row_values(i,2)))

print(data[0])

acc_logger = Log("accelerometer.log")
gyro_logger = Log("gyroscope.log")

accelerometer = Accelerometer("flip", acc_logger)
gyroscope = Gyroscope("flop", gyro_logger)

def update():
    # Update the sensor data
    accData = accelerometer.update()
    gyroData = gyroscope.update()

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
    acc_velocity_var.set(accData["velocity"])
    acc_acceleration_var.set(accData["acceleration"])

    # Update the GUI
    root.after(100, update)

root.mainloop()