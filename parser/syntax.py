#####################################################################
# 基本功能包括：
#   语法检查：是否有错误语法，如果有，退出程序，并打印提示
#   标号不可用内置变量名
#
#   标号识别，将标号放到symbol里面
#
#####################################################################
import sys
import Constant
from code import bin_instruction
from tools import prompt
from tools import syntaxMatch


class Syntax:
	def __init__(self, syntax_table, *args):
		self.table = syntax_table
		if len(args) == 3:
			self.hex_file = args[2]
		elif len(args) == 2:
			self.hex_file = args[1][:-4] + ".hack"
		self.file = args[1]
		self.line_num = 1

	@staticmethod
	def check_default_sign(instruction):
		label1 = instruction not in Constant.default_dest_symbol
		label2 = label1 and instruction not in Constant.default_jump_symbol
		label3 = label2 and instruction not in Constant.default_register_symbol
		label4 = label3 and instruction not in Constant.default_register_ctrl_symbol
		return label4

	def check_file(self):
		with open(self.file) as file:
			for line in file:
				trim_line = syntaxMatch.trim_line(line)
				instruction = syntaxMatch.instruction_type(trim_line)
				if instruction[1] == Constant.INSTRUCTION_CODE_ERROR:
					prompt.syntax_prompt(self.line_num, line)
					sys.exit(Constant.INSTRUCTION_SYNTAX_ERROR)
				elif instruction[1] == Constant.INSTRUCTION_CODE_ANNOTATION:
					pass
				elif instruction[1] == Constant.INSTRUCTION_CODE_LABEL:
					label1 = self.check_default_sign(instruction[2])
					label = label1 and instruction[2] not in self.table.romTable
					if label:
						self.table.add_rom(instruction[2], self.table.romCounter)
					else:
						prompt.syntax_prompt(self.line_num, line, "Invalid name", Constant.INSTRUCTION_CODE_LABEL)
						sys.exit(Constant.INSTRUCTION_INVALID_NAME)
				elif instruction[1] == Constant.INSTRUCTION_CODE_A_NUMBER:
					if int(instruction[2]) > Constant.MAX_VALUE_OF_RAM_STORAGE:
						prompt.syntax_prompt(self.line_num, line, "Invalid Value", Constant.INSTRUCTION_CODE_A_NUMBER)
						sys.exit(Constant.INSTRUCTION_OVER_RAM_LIMIT)
					else:
						self.table.romCounter += 1

				elif instruction[1] == Constant.INSTRUCTION_CODE_A_LETTER:
					self.table.romCounter += 1

				elif instruction[1] == Constant.INSTRUCTION_CODE_C_COMP:
					if instruction[2][0] not in Constant.comp_assign:
						prompt.syntax_prompt(self.line_num, line, "Unsupported compute sign", Constant.INSTRUCTION_CODE_A_LETTER)
						sys.exit(Constant.INSTRUCTION_UNSUPPORTED_COMPUTE)
					else:
						self.table.romCounter += 1
				elif instruction[1] == Constant.INSTRUCTION_CODE_C_DEST_COMP:
					label = instruction[2][0] in Constant.default_dest_symbol and instruction[2][1] in Constant.comp_assign
					if label:
						self.table.romCounter += 1
					else:
						prompt.syntax_prompt(self.line_num, line, "Unsupported syntax", Constant.INSTRUCTION_CODE_C_DEST_COMP)
						sys.exit(Constant.INSTRUCTION_UNSUPPORTED_COMPUTE)
				elif instruction[1] == Constant.INSTRUCTION_CODE_C_COMP_JUMP:
					label = instruction[2][0] in Constant.comp_assign and instruction[2][1] in Constant.default_jump_symbol
					if label:
						self.table.romCounter += 1
					else:
						prompt.syntax_prompt(self.line_num, line, "Unsupported syntax", Constant.INSTRUCTION_CODE_C_COMP_JUMP)
						sys.exit(Constant.INSTRUCTION_UNSUPPORTED_COMPUTE)
				elif instruction[1] == Constant.INSTRUCTION_CODE_C_DEST_COMP_JUMP:
					label1 = instruction[2][0] in Constant.default_dest_symbol
					label2 = label1 and instruction[2][1] in Constant.comp_assign
					label3 = label2 and instruction[2][2] in Constant.default_jump_symbol
					if label3:
						self.table.romCounter += 1
					else:
						prompt.syntax_prompt(self.line_num, line, "Unsupported syntax", Constant.INSTRUCTION_CODE_C_DEST_COMP_JUMP)
						sys.exit(Constant.INSTRUCTION_UNSUPPORTED_COMPUTE)
				self.line_num += 1

	def generate_code(self):
		with open(self.file) as file:
			with open(self.hex_file, 'w') as hex_file:
				for line in file:
					trim_line = syntaxMatch.trim_line(line)
					instruction = syntaxMatch.instruction_type(trim_line)
					bin_code = ""
					if instruction[1] == Constant.INSTRUCTION_CODE_LABEL:
						pass
					elif instruction[1] == Constant.INSTRUCTION_CODE_A_NUMBER:
						bin_code = bin_instruction.Instruction.get_bin_code(instruction[0], instruction[2], Constant.INSTRUCTION_CODE_A_NUMBER)
					elif instruction[1] == Constant.INSTRUCTION_CODE_A_LETTER:
						if instruction[2] in Constant.default_register_symbol:
							instruction_code_number = Constant.default_register_symbol[instruction[2]]
						elif instruction[2] in Constant.default_register_ctrl_symbol:
							instruction_code_number = Constant.default_register_ctrl_symbol[instruction[2]]
						elif instruction[2] in self.table.romTable:
							instruction_code_number = self.table.romTable[instruction[2]]
						elif instruction[2] in self.table.ramTable:
							instruction_code_number = self.table.ramTable[instruction[2]]
						else:
							instruction_code_number = self.table.ramCounter
							self.table.add_ram(instruction[2], self.table.ramCounter)
							self.table.ramCounter += 1
						bin_code = bin_instruction.Instruction.get_bin_code(instruction[0], instruction_code_number, Constant.INSTRUCTION_CODE_A_LETTER)
					elif instruction[1] == Constant.INSTRUCTION_CODE_C_COMP:
						bin_code = bin_instruction.Instruction.get_bin_code(instruction[0], *instruction[2], Constant.INSTRUCTION_CODE_C_COMP)
					elif instruction[1] == Constant.INSTRUCTION_CODE_C_DEST_COMP:
						bin_code = bin_instruction.Instruction.get_bin_code(instruction[0], *instruction[2], Constant.INSTRUCTION_CODE_C_DEST_COMP)
					elif instruction[1] == Constant.INSTRUCTION_CODE_C_COMP_JUMP:
						bin_code = bin_instruction.Instruction.get_bin_code(instruction[0], *instruction[2], Constant.INSTRUCTION_CODE_C_COMP_JUMP)
					elif instruction[1] == Constant.INSTRUCTION_CODE_C_DEST_COMP_JUMP:
						bin_code = bin_instruction.Instruction.get_bin_code(instruction[0], *instruction[2], Constant.INSTRUCTION_CODE_C_DEST_COMP_JUMP)
					if bin_code:
						hex_file.write(bin_code)
						hex_file.write("\n")

	def generate_hex(self):
		self.check_file()
		self.generate_code()
		print("compile successfully!")
