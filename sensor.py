class Accelerometer:
    pass

class Gyroscope :
	angle = 0
	name = ""
 
    def __init__(self, name):
    	self.name = 0

    def set_angle(self, angle):
    	pass

    def get_angle(self):
    	return angle

    def __str__(self):
    	return "Name: " + self.name + " Angle: " + self.angle