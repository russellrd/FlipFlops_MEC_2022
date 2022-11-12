from status import Status
import math

class Gyroscope :
	prev_angle = 0
	angle = 0
	name = ""
	state = None
	power = False

	config = None

	def __init__(self, name,logger, config = {}):
		self.name = name
		self.logger = logger
		self.config = config
		self.status = Status.Idle

	def set_angle(self, angle):
		# self.logger.log("GA", angle)
		self.angle = angle

	def get_angle(self):
		return self.angle

	def get_status(self):
		return self.status

	def turn_on(self):
		self.logger.log("P", "Gyro ON")
		self.status = Status.Running
		self.power = True

	def turn_off(self):
		self.logger.log("P", "Gyro OFF")
		self.status = Status.Idle
		self.power = False

	def update(self, data):
		self.prev_angle = self.angle
	
		if (abs(self.prev_angle - data.get_dir()) > self.config["MAX_ANGLE"]):
			self.status = Status.Error
		else:
			if (self.power):
				self.angle = data.get_dir();
				self.logger.log("GA", self.angle)
			else:
				self.logger.log("W", "Gyro is off")

		return {"power" : self.power, "status" : self.status, "angle" : self.angle}

	def __str__(self):
		return "Name: " + self.name + " Angle: " + self.angle