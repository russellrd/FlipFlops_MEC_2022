import xlrd
import math
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import StringVar, ttk
from accelerometer import Accelerometer
from gyroscope import Gyroscope
from log import Log
from data_entry import DataEntry
from status import Status

# Constants
MAX_STEPS = 100
MAX_ANGLE = 10
CANVAS_WIDTH = 200
CANVAS_HEIGHT = 200
CANVAS_RADIUS = 40
ARROW_SIZE = 80

# Tkinter setup
root = tk.Tk()
root.title("Ocean Current Detection (OCD)")
root.resizable(False, False)
frame = ttk.Frame(root)
frame.grid()

# On/Off icons
green = ImageTk.PhotoImage(Image.open("images/green.png"))
red = ImageTk.PhotoImage(Image.open("images/red.png"))

# Accelerometer string vars
acc_status_var = StringVar()
acc_status_var.set(Status.Idle.name)
acc_velocity_var = StringVar()
acc_velocity_var.set(0)
acc_acceleration_var = StringVar()
acc_acceleration_var.set(0)

# Gyroscope string vars
gyro_status_var = StringVar()
gyro_status_var.set(Status.Idle.name)
gyro_angle_var = StringVar()
gyro_angle_var.set(0)

# Title label
ttk.Label(frame, text="Ocean Current Detection (OCD)", font='Helvetica 18 bold').grid(columnspan=5)

# Lables for accelerometer
ttk.Label(frame, text="Accelerometer", font='Helvetica 14 bold').grid(column=0, row=1, padx=10, pady=10)
accOn = tk.Label(frame, image=red)
accOn.grid(column=1, row=1, pady=10)
ttk.Label(frame, text="Status: ", font='Helvetica 12 bold').grid(column=0, row=2, padx=10, pady=10)
ttk.Label(frame, textvariable=acc_status_var, font='Helvetica 12').grid(column=1, row=2, padx=10, pady=10)
ttk.Label(frame, text="Velocity: ", font='Helvetica 12 bold').grid(column=0, row=3, padx=10, pady=10)
ttk.Label(frame, textvariable=acc_velocity_var, font='Helvetica 12').grid(column=1, row=3, padx=10, pady=10)
ttk.Label(frame, text="Acceleration: ", font='Helvetica 12 bold').grid(column=0, row=4, padx=10, pady=10)
ttk.Label(frame, textvariable=acc_acceleration_var, font='Helvetica 12').grid(column=1, row=4, padx=10, pady=10)

# Lables for gyroscope
ttk.Label(frame, text="Gyroscope", font='Helvetica 14 bold').grid(column=3, row=1, padx=10, pady=10)
gyroOn = tk.Label(frame, image=red)
gyroOn.grid(column=4, row=1, pady=10)
ttk.Label(frame, text="Status: ", font='Helvetica 12 bold').grid(column=3, row=2, padx=10, pady=10)
ttk.Label(frame, textvariable=gyro_status_var, font='Helvetica 12').grid(column=4, row=2, padx=10, pady=10)
ttk.Label(frame, text="Angle: ", font='Helvetica 12 bold').grid(column=3, row=3, padx=10, pady=10)
ttk.Label(frame, textvariable=gyro_angle_var, font='Helvetica 12').grid(column=4, row=3, padx=10, pady=10)

# Create canvas
canvas = tk.Canvas(frame, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg = 'lightblue')
canvas.grid(column=5, row=0, padx=10, pady=10, columnspan=5, rowspan=5)

# Open excel file
data_workbook = xlrd.open_workbook('MEC_EXCEL.xls').sheet_by_index(0)

# Loop through all data in the excel file
data = []
for i in range(1, data_workbook.nrows):
    data.append(DataEntry(data_workbook.row_values(i,0)[0], data_workbook.row_values(i,0)[1], data_workbook.row_values(i,0)[2]))

# Initialize loggers
acc_logger = Log("accelerometer.log")
gyro_logger = Log("gyroscope.log")

# Initialize sensors
accelerometer = Accelerometer("flip", acc_logger)
gyroscope = Gyroscope("flop", gyro_logger, {"MAX_ANGLE": MAX_ANGLE})

# Turn on sensorws
accelerometer.turn_on()
gyroscope.turn_on()

step = 0

def update():
    global step

    # Get data for specific step
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
    acc_acceleration_var.set(str(round(accData["acceleration"], 2)))

    gyro_status_var.set(gyroData["status"].name)
    gyro_angle_var.set(str(gyroData["angle"])+"°")

    # Draw new boar diagram to canvas
    canvas.delete("all")
    canvas.create_line((CANVAS_WIDTH/2), (CANVAS_HEIGHT/2), (CANVAS_WIDTH/2)+(ARROW_SIZE*math.cos(math.radians(gyroData["angle"]-90))), (CANVAS_HEIGHT/2)+(ARROW_SIZE*math.sin(math.radians(gyroData["angle"]-90))), arrow=tk.LAST, width=8, fill="red", arrowshape=(25, 25, 8))
    canvas.create_oval((CANVAS_WIDTH/2)-CANVAS_RADIUS, (CANVAS_HEIGHT/2)-CANVAS_RADIUS, (CANVAS_WIDTH/2)+CANVAS_RADIUS, (CANVAS_HEIGHT/2)+CANVAS_RADIUS, fill="black", width=2)
    canvas.create_text((CANVAS_WIDTH/2), (CANVAS_HEIGHT/2), text="OCD", font='Helvetica 14 bold', fill="white")
    
    # Call next step after 100ms
    step+=1
    if(step < MAX_STEPS):
        root.after(100, update)

update()
root.mainloop()