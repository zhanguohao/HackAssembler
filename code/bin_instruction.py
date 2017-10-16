import Constant
from code import comp
from code import dest
from code import jump
from code import assignAregister


class Instruction:
	@staticmethod
	def get_bin_code(inst_type, *args):
		# print("--" * 20)
		# print(inst_type)
		# print(args)
		if inst_type == "A":
			return assignAregister.AInstrction.get_code(args[0])
		elif inst_type == "C":
			if args[-1] == Constant.INSTRUCTION_CODE_C_COMP:
				return comp.Compute.get_code(Constant.comp_assign[args[0]]) + dest.Destination.get_code("null") + jump.Jump.get_code("null")
			elif args[-1] == Constant.INSTRUCTION_CODE_C_DEST_COMP:
				return comp.Compute.get_code(Constant.comp_assign[args[1]]) + dest.Destination.get_code(args[0]) + jump.Jump.get_code("null")
			elif args[-1] == Constant.INSTRUCTION_CODE_C_COMP_JUMP:
				return comp.Compute.get_code(Constant.comp_assign[args[0]]) + dest.Destination.get_code("null") + jump.Jump.get_code(args[1])
			elif args[-1] == Constant.INSTRUCTION_CODE_C_DEST_COMP_JUMP:
				return comp.Compute.get_code(Constant.comp_assign[args[1]]) + dest.Destination.get_code(args[0]) + jump.Jump.get_code(args[2])
