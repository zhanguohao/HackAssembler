import Constant


class Jump:
	@staticmethod
	def get_code(code):
		if code == "JGT":
			return Constant.JUMP_INSTRUCTION_JGT
		elif code == "JEQ":
			return Constant.JUMP_INSTRUCTION_JEQ
		elif code == "JGE":
			return Constant.JUMP_INSTRUCTION_JGE
		elif code == "JLT":
			return Constant.JUMP_INSTRUCTION_JLT
		elif code == "JNE":
			return Constant.JUMP_INSTRUCTION_JNE
		elif code == "JLE":
			return Constant.JUMP_INSTRUCTION_JLE
		elif code == "JMP":
			return Constant.JUMP_INSTRUCTION_JMP
		else:
			return Constant.JUMP_INSTRUCTION_NULL
