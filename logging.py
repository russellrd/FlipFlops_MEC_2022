class loggine():
	file_name = ""
	fh = None
	levelDict = {"P": "Power", "E": "Error", "GA": "Angle"}
	def __init__(self, file_name):
		self.file_name = file_name
		self.fh = open(selg.file_name, "w")

	def closeFile(self):
		fh.close()

	def log(self, level, data):
		info = levelDict[level] + " " + data
		f.write(logger)

