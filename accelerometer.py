import math
import status

class Accelerometer: 
    AccX= 0 
    AccY = 0
    speed  = 0
    time = 0 
    magn = 0
    velocity = 0 
    power = False
    state = None

    config = None

    def __init__(self, name, logger, config):
        self.name = name
        self.logger = logger
        self.status = Status()
        self.state = self.status.Idle.name
        self.config = config

    def set_x(self, AccX):
        self.logger.log("A-X", AccX)
        self.AccX

    def set_y (self, AccY):
        self.logger.log("A-Y", AccY)
        self.AccY

    def set_speed (self, speed): 
        self.logger.log("A-S", speed)
        self.speed

    def set_time (self, time): 
        self.time

    def set_magn (self,magn): 
        self.magn

    def set_velocity (self, velocity):
        self.logger.log("A-V", velocity)
        self.velocity

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
    
    def calc_mag(self):

        self.speed = math. sqrt(self.AccX ** 2 + self.AccY** 2)
        # calc the magnitude using the speed of x and y 
    def calc_velocity (self):
        self.calc_mag ()
        self.velocity = self.speed / self.time

    def update(self, data):
        return {"power" : self.power, "Status" : self.state, "velocity" : self.velocity}

    def turn_on(self):
        self.state = self.status.Running.name
        self.power = True

    def turn_off(self):
        self.state = self.status.Idle.name
        self.power = False

    def __str__(self):
        return "Name: " + self.name + " Speed: " + self.speed