import math



class Accelerometer: 
    AccX= 0 
    AccY = 0
    speed  = 0
    time = 0 
    magn = 0
    velocity = 0 

    def __init__(self, name):
        self.name = 0
	
    def set_x(self, AccX):
        pass

    def set_y (self, AccY):
        pass

    def set_speed (self, speed): 
        pass

    def set_time (self, time): 
        pass

    def set_magn (self,magn): 
        pass

    def set_velocity (self, velocity):
        pass

    def get_x (self):
        return AccX
    
    def get_y (self):
        return AccY
    
    def get_speed(self):
        return speed
    
    def get_time(self): 
        return time
    
    def get_magn(self): 
        return magn
    
    def get_velocity(self):
        return velocity 
    
    def __str__(self):
        return "Name: " + self.name + " Speed: " + self.speed

    def check_Y():
        pass
    #def calc_mag ():
       
    # calc the magnitude using the speed of x and y 		
    #def calc_velocity ():