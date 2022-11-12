class Accelerometer:
    pass

class Gyroscope :
	angle = 0
	name = ""
	status = 1
	power = 1
 
    def __init__(self, name):
    	self.name = 0

    def set_angle(self, angle):
    	self.angle = angle

    def get_angle(self):
    	return angle

    def get_status(self):
    	return status

    def turn_on(self):
    	self.power = 1

    def turn_off(self):
    	self.power = 0

  	def update(self):
  		return [self.power, self.status, self.angle]

    def __str__(self):
    	return "Name: " + self.name + " Angle: " + self.angle