class Memory:
	def __init__(self):
		self.mem = 0

	def store(self,val):
		self.mem = val
		return val

	def recall(self):
		return self.mem

memory = Memory()
