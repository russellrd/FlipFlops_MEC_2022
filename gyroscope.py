class Gyroscope :
	prev_angle = 0
	angle = 0
	name = ""
	status = 1
	power = False

	def __init__(self, name,logger):
		self.name = name
		self.logger = logger

	def set_angle(self, angle):
		# self.logger.log("GA", angle)
		self.angle = angle

	def get_angle(self):
		return self.angle

	def get_status(self):
		return self.status

	def turn_on(self):
		self.power = True

	def turn_off(self):
		self.power = False

	def update(self, data):
		prev_angle = self.angle
		return {"power" : self.power, "status:" : self.status, "angle" : self.angle}

	def __str__(self):
		return "Name: " + self.name + " Angle: " + self.angle