import Constant


class Destination:
	@staticmethod
	def get_code(code):
		if code == "D":
			return Constant.DEST_INSTRUCTION_D
		elif code == "A":
			return Constant.DEST_INSTRUCTION_A
		elif code == "M":
			return Constant.DEST_INSTRUCTION_M
		elif set(code) == set("MD"):
			return Constant.DEST_INSTRUCTION_MD
		elif set(code) == set("AD"):
			return Constant.DEST_INSTRUCTION_AD
		elif set(code) == set("AM"):
			return Constant.DEST_INSTRUCTION_AM
		elif set(code) == set("AMD"):
			return Constant.DEST_INSTRUCTION_AMD
		else:
			return Constant.DEST_INSTRUCTION_NULL
