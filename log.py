class log():
	file_name = ""
	fh = None
	levelDict = {"P": "Power", "E": "Error", "GA": "Angle"}
<<<<<<< HEAD:logging.py
	
=======

>>>>>>> bb1adb0e359c80f6baaf5d91317ce23df6e8cb2a:log.py
	def __init__(self, file_name):
		self.file_name = file_name
		self.fh = open(self.file_name, "w")

	def closeFile(self):
		self.fh.close()

	def log(self, level, data):
		info = self.levelDict[level] + " " + data + "\n"
		self.fh.write(info)