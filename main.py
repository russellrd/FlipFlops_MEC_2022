import xlrd
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import StringVar, ttk
from accelerometer import Accelerometer
from gyroscope import Gyroscope
from log import Log
from data_entry import DataEntry
from status import Status

root = tk.Tk()
root.title("Ocean Current Detection (OCD)")
root.resizable(False, False)
frame = ttk.Frame(root)
frame.grid()

green = ImageTk.PhotoImage(Image.open("images/green.png"))
red = ImageTk.PhotoImage(Image.open("images/red.png"))

acc_status_var = StringVar()
acc_status_var.set(Status.Idle.name)
acc_velocity_var = StringVar()
acc_velocity_var.set(0)
acc_acceleration_var = StringVar()
acc_acceleration_var.set(0)

gyro_status_var = StringVar()
gyro_status_var.set(Status.Idle.name)
gyro_angle_var = StringVar()
gyro_angle_var.set(0)

ttk.Label(frame, text="Ocean Current Detection (OCD)", font='Helvetica 18 bold').grid(columnspan=5)
ttk.Label(frame, text="Accelerometer", font='Helvetica 14 bold').grid(column=0, row=1, padx=10, pady=10)
accOn = tk.Label(frame, image=red)
accOn.grid(column=1, row=1, padx=10, pady=10)
ttk.Label(frame, text="Gyroscope", font='Helvetica 14 bold').grid(column=3, row=1, padx=10, pady=10)
gyroOn = tk.Label(frame, image=red)
gyroOn.grid(column=4, row=1, padx=10, pady=10)
ttk.Label(frame, text="Status: ", font='Helvetica 12 bold').grid(column=0, row=2, padx=10, pady=10)
ttk.Label(frame, textvariable=acc_status_var, font='Helvetica 12').grid(column=1, row=2, padx=10, pady=10)
ttk.Label(frame, text="Velocity: ", font='Helvetica 12 bold').grid(column=0, row=3, padx=10, pady=10)
ttk.Label(frame, textvariable=acc_velocity_var, font='Helvetica 12').grid(column=1, row=3, padx=10, pady=10)
ttk.Label(frame, text="Acceleration: ", font='Helvetica 12 bold').grid(column=0, row=4, padx=10, pady=10)
ttk.Label(frame, textvariable=acc_acceleration_var, font='Helvetica 12').grid(column=1, row=4, padx=10, pady=10)

ttk.Label(frame, text="Status: ", font='Helvetica 12 bold').grid(column=3, row=2, padx=10, pady=10)
ttk.Label(frame, textvariable=gyro_status_var, font='Helvetica 12').grid(column=4, row=2, padx=10, pady=10)
ttk.Label(frame, text="Velocity: ", font='Helvetica 12 bold').grid(column=3, row=3, padx=10, pady=10)
ttk.Label(frame, textvariable=gyro_angle_var, font='Helvetica 12').grid(column=4, row=3, padx=10, pady=10)

data_workbook = xlrd.open_workbook('MEC_EXCEL.xls').sheet_by_index(0)

data = []

for i in range(1, data_workbook.nrows):
    data.append(DataEntry(data_workbook.row_values(i,0)[0], data_workbook.row_values(i,0)[1], data_workbook.row_values(i,0)[2]))

acc_logger = Log("accelerometer.log")
gyro_logger = Log("gyroscope.log")

accelerometer = Accelerometer("flip", acc_logger)
gyroscope = Gyroscope("flop", gyro_logger)

accelerometer.turn_on()
gyroscope.turn_on()

MAX_STEPS = 100

step = 0

def update():
    global step
    global accOn
    global gyroOn

    step_data = data[step]

    # Update the sensor data
    accData = accelerometer.update(step_data)
    gyroData = gyroscope.update(step_data)

    # Update accelerometer "on" icon
    if(accData["power"] == True):
        accOn.configure(image=green)
        accOn.image = green
    else:
        accOn.configure(image=red)
        accOn.image = red

    # Update gyroscope "on" icon
    if(gyroData["power"] == True):
        gyroOn.configure(image=green)
        gyroOn.image = green
    else:
        gyroOn.configure(image=red)
        gyroOn.image = red

    # Update the labels
    acc_status_var.set(accData["status"].name)
    acc_velocity_var.set(accData["velocity"])
    acc_acceleration_var.set(step_data.get_curr_vel())

    gyro_status_var.set(gyroData["status"].name)
    gyro_angle_var.set(gyroData["angle"])

    # Update the GUI
    step+=1
    if(step < MAX_STEPS):
        root.after(100, update)

update()
root.mainloop()