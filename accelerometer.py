import math
from status import Status

# This class will be used to represent the accelerometer. The data is taken from the excel sheet with the simulated data and gives the acceleration and velocity.  

class Accelerometer: 
    # Initializing variables
    AccX= 0 
    AccY = 0
    speed  = 0
    time = 0 
    prev = None
    magn = 0
    velocity = 0 
    power = False
    state = None
    acceler = 0

    config = None
    

    def __init__(self, name, logger, config = {}):
        self.name = name
        self.logger = logger
        self.status = Status.Idle
        self.config = config
        self.logger.log("P", "Accelerometer Init")
        
    # Setters 
    def set_x(self, AccX):
        self.logger.log("A-X", self.AccX)
        self.AccX

    def set_y (self, AccY):
        self.logger.log("A-Y", self.AccY)
        self.AccY

    def set_speed (self, speed): 
        self.logger.log("A-S", self.speed)
        self.speed

    def set_time (self, time): 
        self.time

    def set_magn (self,magn): 
        self.magn

    def set_velocity (self, velocity):
        self.logger.log("A-V", self.velocity)
        self.velocity = velocity

    def set_accelration (self, acceler):
        self.logger.log("A-A", self.acceler)
        self.acceler, acceler

    def set_prev (self, prev):
        self.prev
     
    # Getters 
    def get_x (self):
        return self.AccX

    def get_y (self):
        return self.AccY
    
    def get_speed(self):
        self.calc_mag()
        return self.speed
    
    def get_time(self): 
        return self.time
    
    def get_magn(self): 
        return self.magn
    
    def get_velocity(self):
        return self.velocity 
    
    def get_acceleration(self):
        return self.acceler
    
    def get_prev (self):
        return self.prev
    
    # Function to find the speed 
    def calc_mag(self):
        self.speed = math.sqrt(self.AccX ** 2 + self.AccY** 2)

    # Function to calcaulte acceleration    
    def calc_accelr (self):
        # chehcking if previous time is not equal to None 
        if (self.prev != None):
            self.acceler = (self.velocity-self.prev) / 0.1
        self.prev = self.velocity
        
     # This function will update the values 
    def update(self, data):
        self.set_velocity(data.get_curr_vel ())
        self.calc_mag ()
        self.calc_accelr ()
        self.logger.log("A-M", self.magn)
        self.logger.log("A-A", self.acceler)
        self.logger.log("A-V", self.velocity)
        return {"power" : self.power, "status" : self.status, "velocity" : self.velocity, "acceleration" : self.acceler}

    # This function will turn on the sensor 
    def turn_on(self):
        self.logger.log("P", "Accelerometer ON")
        self.status = Status.Running
        self.power = True

    # This function will turn on the sensor 
    def turn_off(self):
        self.logger.log("P", "Accelerometer OFF")
        self.status = Status.Idle
        self.power = False

    def __str__(self):
        return "Name: " + self.name + " Speed: " + self.speed
