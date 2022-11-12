from status import Status
import math

class Gyroscope :
	# variables dec
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
		# set the status to idle
		self.status = Status.Idle

	def set_angle(self, angle):
		# self.logger.log("GA", angle)
		self.angle = angle

	def get_angle(self):
		return self.angle

	def get_status(self):
		return self.status

	def turn_on(self):
		# log the current state
		self.logger.log("P", "Gyro ON")
		self.status = Status.Running
		self.power = True

	def turn_off(self):
		self.logger.log("P", "Gyro OFF")
		self.status = Status.Idle
		# set the power to False
		self.power = False

	def update(self, data):
		# get the current angle and set it to prev
		self.prev_angle = self.angle
	
		if (abs(self.prev_angle - data.get_dir()) > self.config["MAX_ANGLE"]):
			self.status = Status.Error
			self.turn_off()
			# set the status to error
			self.status = Status.Error
		else:
			# check if the sensor is on
			if (self.power):
				# get the new angle data
				self.angle = data.get_dir();
				# log the new changes
				self.logger.log("GA", self.angle)
			else:
				self.logger.log("W", "Gyro is off")

		# Rreturn the updated values
		return {"power" : self.power, "status" : self.status, "angle" : self.angle}

	def __str__(self):
		return "Name: " + self.name + " Angle: " + self.angle