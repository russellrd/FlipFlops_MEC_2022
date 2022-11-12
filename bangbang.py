class BangBangLoop:
	setpoint = 0
	error = 0
	curr = 0

	def __init__(self, setpoint):
		self.setpoint = setpoint

	def get_curr(self):
		return curr

	def set_curr(self, curr):
		self.curr = curr;

	def get_error(self):
		return error

	def update_error(self, new_error):
		self.error = new_error

	def loop(self):
		if (setpoint < curr):
			curr += 0.1
		else:
			curr -= 0.1


