class Gyroscope :
	angle = 0
	name = ""
	status = 1
	power = 1

	def __init__(self, name,logger):
		self.name = 0
		self.logger = logger

	def set_angle(self, angle):
		self.logger.log("GA", angle)
		self.angle = angle

	def get_angle(self):
		return self.angle

	def get_status(self):
		return self.status

	def turn_on(self):
		self.power = 1

	def turn_off(self):
		self.power = 0

		def update(self):
			return {"power" : self.power, "status:" : self.status, "angle" : self.angle}

	def __str__(self):
		return "Name: " + self.name + " Angle: " + self.angle