class Log():
	file_name = ""
	fh = None
	levelDict = {"P": "Power", "E": "Error", "GA": "Angle", "A-X": "X-Speed", "A-Y":"Y-Speed", "A-M" :" Mag", "A-V" : "Velocity", "A-A": "Acceleration"}

	def __init__(self, file_name):
		self.file_name = file_name
		self.fh = open(self.file_name, "w")

	def closeFile(self):
		self.fh.close()

	def log(self, level, data):
		info = self.levelDict[level] + " " + data + "\n"
		self.fh.write(info)
