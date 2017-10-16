import Constant


class SymbolTable:
	def __init__(self):
		self.romTable = {}
		self.ramTable = {}
		self.romCounter = 0
		self.ramCounter = Constant.RAM_START_VALUE_FOR_USER

	def add_rom(self, key, value):
		self.romTable[key] = value

	def remove_rom(self, key):
		self.romTable.pop(key)

	def clear_rom(self):
		self.romTable.clear()

	def add_ram(self, key, value):
		self.ramTable[key] = value

	def remove_ram(self, key):
		self.ramTable.pop(key)

	def clear_ram(self):
		self.ramTable.clear()
