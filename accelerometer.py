import math



class Accelerometer: 
    AccX= 0 
    AccY = 0
    speed  = 0
    time = 0 
    magn = 0
    velocity = 0 

    def __init__(self, name, logger):
        self.name = name
        self.logger = logger
	
    def set_x(self, AccX):
        #self.logger.log("AS")
        self.AccX

    def set_y (self, AccY):
        self.AccY

    def set_speed (self, speed): 
        self.speed

    def set_time (self, time): 
        self.time

    def set_magn (self,magn): 
        self.magn

    def set_velocity (self, velocity):
        self.velocity

    def get_x (self):
        return AccX
    
    def get_y (self):
        return AccY
    
    def get_speed(self):
        self.calc_mag()
        return speed
    
    def get_time(self): 
        return time
    
    def get_magn(self): 
        return magn
    
    def get_velocity(self):
        return velocity 
    
    def calc_mag(self):

        self.speed = math. sqrt(self.AccX ** 2 + self.AccY** 2)
        # calc the magnitude using the speed of x and y 
    def calc_velocity (self):
        self.calc_mag ()
        self.velocity = self.speed / self.time

    def __str__(self):
        return "Name: " + self.name + " Speed: " + self.speed
    