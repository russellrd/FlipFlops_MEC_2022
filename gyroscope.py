import status

class Gyroscope :
	prev_angle = 0
	angle = 0
	name = ""
	state = None
	power = False

	config = None

	def __init__(self, name,logger, config):
		self.name = name
		self.logger = logger
		self.config = config
		self.status = Status()
		self.state = self.status.Idle.name

	def set_angle(self, angle):
		# self.logger.log("GA", angle)
		self.angle = angle

	def get_angle(self):
		return self.angle

	def get_status(self):
		return self.status

	def turn_on(self):
		self.state = self.status.Running.name
		self.power = True

	def turn_off(self):
		self.status = self.status.Idle.name
		self.power = False

	def update(self, data):
		prev_angle = self.angle
		return {"power" : self.power, "status:" : self.status, "angle" : self.angle}

	def __str__(self):
		return "Name: " + self.name + " Angle: " + self.angle