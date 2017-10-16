import os
import sys
import Constant


def user_prompt(tips):
	print("*" * 50)
	print(tips)
	print("*" * 50)
	print("Syntax:")
	print("\t python hackAssembler.py your/path/to/filename.asm [filename.hack]")
	print("args:")
	print("\t the suffix of program file must be .asm")
	print("\t if filename.hack was omitted , file name would be same with file.asm")


def file_check(*args):
	if len(args) == 3:
		if not os.path.isfile(args[1]):
			user_prompt("\t\tFile Not Found!")
			sys.exit(Constant.INSTRUCTION_FILE_NOT_FOUNT)
		elif not args[1].endswith(".asm"):
			user_prompt("The suffix is Wrong, Please check.")
			sys.exit(Constant.INSTRUCTION_SUFFIX_WRONG)
		elif not args[2].endwith(".hack"):
			user_prompt("The suffix is Wrong, Please check.")
			sys.exit(Constant.INSTRUCTION_SUFFIX_WRONG)
	elif len(args) == 2:
		if not os.path.isfile(args[1]):
			user_prompt("\t\tFile Not Found!")
			sys.exit(Constant.INSTRUCTION_FILE_NOT_FOUNT)
		elif not args[1].endswith(".asm"):
			user_prompt("The suffix is Wrong, Please check.")
			sys.exit(Constant.INSTRUCTION_SUFFIX_WRONG)
	elif len(args) == 1:
		user_prompt("There is no file!")
		sys.exit(Constant.INPUT_ARGS_ERROR)
	else:
		user_prompt("Please check your input!")
		sys.exit(Constant)


def syntax_prompt(line_num, line, tips = "", instruction_code = -2):
	print("Syntax Error Occur!")
	if tips:
		print(tips)
	if instruction_code != -2:
		print("instruction code : ", instruction_code)
	print("Please check this line :")
	print("*" * 50)
	print("line:", line_num, "--> ", line, end = "")
	print("*" * 50)
