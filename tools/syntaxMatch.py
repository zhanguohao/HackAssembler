import re
import Constant


def trim_line(line):
	"""
	:param line:
	:return:
	"""
	line_compile = re.compile("\s+")
	t_line = re.sub(line_compile, "", line)
	return t_line


def instruction_type(line):
	"""

	:param line:
	:return: instruction_sign instruction number_sign

	instruction_sign
	annotation
	L
	A
	C

	number sign:
	-1: error
	0:  annotation
	1:  label
	2:  A instruction constant
	3:  A instruction letter
	4:  C instruction comp
	5:  C instruction comp;jump
	6:  C instruction dest=comp
	7:  C instruction dest=comp;jump

	see in Constant

	error sign
	l_error
	a_error
	c_error

	"""
	if line == "":
		return "blank_line", Constant.INSTRUCTION_CODE_ANNOTATION
	elif line.startswith("#") or line.startswith("//"):
		return "annotation", Constant.INSTRUCTION_CODE_ANNOTATION
	else:
		line = line.split("//")[0]
		if line.startswith("(") and line.endswith(")"):
			pro_label = line[1:-1]
			label_regex = r"\A[a-zA-Z_]?[.$\w]*\Z"
			if re.match(label_regex, pro_label):
				return "L", Constant.INSTRUCTION_CODE_LABEL, pro_label,
			else:
				return "l_error", Constant.INSTRUCTION_CODE_ERROR
		elif line.startswith("@"):
			a_inst = line[1:]
			a_regex = r"\A[a-zA-Z_]?[.$\w]*\Z"
			if a_inst.isdigit():
				return "A", Constant.INSTRUCTION_CODE_A_NUMBER, a_inst,
			elif re.match(a_regex, a_inst):
				return "A", Constant.INSTRUCTION_CODE_A_LETTER, a_inst
			else:
				return "a_error", Constant.INSTRUCTION_CODE_ERROR
		else:
			c_inst = re.split("[=;]", line)
			comp_regx1 = r"\A[\!ADM\+-01&|]+\Z"
			dest_regx2 = r"\A[AMD]{0,3}[Nn]?[Uu]?[lL]*[^0-9_]\Z"
			jump_regx3 = r"\A[JGLTEQMNP]{0,3}[Nn]?[Uu]?[lL]{0,2}\Z"

			if len(c_inst) == 1:
				if re.match(comp_regx1, c_inst[0]):
					return "C", Constant.INSTRUCTION_CODE_C_COMP, c_inst
				else:
					return "c_error", Constant.INSTRUCTION_CODE_ERROR
			elif len(c_inst) == 2:
				dest_comp = re.match(dest_regx2, c_inst[0]) and re.match(comp_regx1, c_inst[1])
				comp_jump = re.match(comp_regx1, c_inst[0]) and re.match(jump_regx3, c_inst[1])
				if comp_jump and (";" in line):
					return "C", Constant.INSTRUCTION_CODE_C_COMP_JUMP, c_inst
				elif dest_comp and ("=" in line):
					return "C", Constant.INSTRUCTION_CODE_C_DEST_COMP, c_inst
				else:
					return "c_error", Constant.INSTRUCTION_CODE_ERROR
			elif len(c_inst) == 3:
				if re.match(dest_regx2, c_inst[0]) and re.match(comp_regx1, c_inst[1]) and re.match(jump_regx3, c_inst[2]):
					return "C", Constant.INSTRUCTION_CODE_C_DEST_COMP_JUMP, c_inst
				else:
					return "c_error", Constant.INSTRUCTION_CODE_ERROR
			else:
				return "c_error", Constant.INSTRUCTION_CODE_ERROR


def str_match_list_item(s, l):
	"""

	:param s:
	:param l:
	:return:
	"""
	for item in l:
		if set(s) == set(item):
			return True
	return False


if __name__ == '__main__':
	print(instruction_type(trim_line("hello")))
	print(instruction_type(trim_line("#Hello , this is asm assembler")))
	print(instruction_type(trim_line("//Hello , this is asm assembler")))
	print(instruction_type(trim_line("   ##  Hello ")))
	print(instruction_type(trim_line("(BOARD)")))
	print(instruction_type(trim_line("@sys.init")))
	print(instruction_type(trim_line("@ball.show")))
	print(instruction_type(trim_line("@memory.dealloc")))
	print(instruction_type(trim_line("@screen.setcolor")))
	print(instruction_type(trim_line("@ball.draw")))
	print(instruction_type(trim_line("@screen.drawrectangle")))
	print(instruction_type(trim_line("@math.abs")))
	print(instruction_type(trim_line("@ball.setdestination$if_true0")))
	print(instruction_type(trim_line("@SP")))
	print(instruction_type(trim_line("@HOW")))
	print(instruction_type(trim_line("D=M")))
	print(instruction_type(trim_line("D==A")))
	print(instruction_type(trim_line("   D=M              // D = first number")))
	print(instruction_type(trim_line("D;JGT            // if D>0 (first is greater) goto output_first")))
	print(instruction_type(trim_line("ADM")))
	print(instruction_type(trim_line("DM")))
	print(instruction_type(trim_line("DMK")))
	print(instruction_type(trim_line("D;JMP")))
	print(instruction_type(trim_line("D+1;JMP")))
	print(instruction_type(trim_line("D=D-1")))
	print(instruction_type(trim_line("DM=D|M")))
	print(instruction_type(trim_line("AD=A&D")))
	print(instruction_type(trim_line("AD=D+M;JLT")))
	print(trim_line("D;JGT            // if D>0 (first is greater) goto output_first").split("//"))
	print(trim_line("D;JGT        ").split("//"))
	print(instruction_type(trim_line("D;JGT")))

