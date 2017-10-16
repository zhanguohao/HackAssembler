#####################################################################
# default symbol
#####################################################################
default_register_symbol = {
	"R0": 0,
	"R1": 1,
	"R2": 2,
	"R3": 3,
	"R4": 4,
	"R5": 5,
	"R6": 6,
	"R7": 7,
	"R8": 8,
	"R9": 9,
	"R10": 10,
	"R11": 11,
	"R12": 12,
	"R13": 13,
	"R14": 14,
	"R15": 15,
	}

default_register_ctrl_symbol = {
	"SP": 0,
	"LCL": 1,
	"ARG": 2,
	"THIS": 3,
	"THAT": 4,
	"SCREEN": 16384,
	"KBD": 24576
	}

default_jump_symbol = ["null", "NULL", "Null", "JGT", "JEQ", "JGE", "JLT", "JNE", "JLE", "JMP"]

default_dest_symbol = ["null", "NULL", "Null", "D", "A", "M", "AD", "AM", "MD", "AMD"]

#####################################################################
# instruction code
#####################################################################
A_INSTRUCTION = "0"
C_INSTRUCTION = "111"

#####################################################################
# destination code
#####################################################################
DEST_INSTRUCTION_NULL = "000"
DEST_INSTRUCTION_M = "001"
DEST_INSTRUCTION_D = "010"
DEST_INSTRUCTION_A = "100"
DEST_INSTRUCTION_MD = "011"
DEST_INSTRUCTION_AM = "101"
DEST_INSTRUCTION_AD = "110"
DEST_INSTRUCTION_AMD = "111"

#####################################################################
# jump code
#####################################################################
JUMP_INSTRUCTION_NULL = "000"
JUMP_INSTRUCTION_JGT = "001"
JUMP_INSTRUCTION_JEQ = "010"
JUMP_INSTRUCTION_JLT = "100"
JUMP_INSTRUCTION_JGE = "011"
JUMP_INSTRUCTION_JNE = "101"
JUMP_INSTRUCTION_JLE = "110"
JUMP_INSTRUCTION_JMP = "111"

#####################################################################
# comp code
#####################################################################
COMP_INSTRUCTION_A_NOT_M = "0"
COMP_INSTRUCTION_M_NOT_A = "1"
COMP_INSTRUCTION_ZERO = "101010"
COMP_INSTRUCTION_ONE = "111111"
COMP_INSTRUCTION_NEG_ONE = "111010"
COMP_INSTRUCTION_D = "001100"
COMP_INSTRUCTION_AM = "110000"
COMP_INSTRUCTION_NOT_D = "001101"
COMP_INSTRUCTION_NOT_AM = "110001"
COMP_INSTRUCTION_NEG_D = "001111"
COMP_INSTRUCTION_NEG_AM = "110011"
COMP_INSTRUCTION_D_PLUS_ONE = "011111"
COMP_INSTRUCTION_AM_PLUS_ONE = "110111"
COMP_INSTRUCTION_D_MINUS_ONE = "001110"
COMP_INSTRUCTION_AM_MINUS_ONE = "110010"
COMP_INSTRUCTION_D_PLUS_AM = "000010"
COMP_INSTRUCTION_D_MINUS_AM = "010011"
COMP_INSTRUCTION_AM_MINUS_D = "000111"
COMP_INSTRUCTION_D_AND_AM = "000000"
COMP_INSTRUCTION_D_OR_AM = "010101"

#####################################################################
# compute sign
#####################################################################
comp_assign = {
	"0": "zero",
	"1": "one",
	"-1": "neg_one",
	"D": "D",
	"A": "A",
	"M": "M",
	"!D": "not_d",
	"!A": "not_a",
	"!M": "not_m",
	"-D": "neg_d",
	"-A": "neg_a",
	"-M": "neg_m",
	"D+1": "d_plus_one",
	"A+1": "a_plus_one",
	"M+1": "m_plus_one",
	"D-1": "d_minus_one",
	"A-1": "a_minus_one",
	"M-1": "m_minus_one",
	"D+A": "d_plus_a",
	"D+M": "d_plus_m",
	"D-A": "d_minus_a",
	"D-M": "d_minus_m",
	"A-D": "a_minus_d",
	"M-D": "m_minus_d",
	"D&A": "d_and_a",
	"D&M": "d_and_m",
	"D|A": "d_or_a",
	"D|M": "d_or_m"
	}

#####################################################################
# exit sign
#####################################################################
INSTRUCTION_FILE_NOT_FOUNT = 1
INSTRUCTION_SUFFIX_WRONG = 2
INSTRUCTION_SYNTAX_ERROR = 3
INSTRUCTION_INVALID_NAME = 4
INSTRUCTION_OVER_RAM_LIMIT = 5
INSTRUCTION_UNSUPPORTED_COMPUTE = 6
INPUT_ARGS_ERROR = 7
INPUT_ARGS_ERROR_OTHER = 50

#####################################################################
# Hardware sign
#####################################################################
MAX_VALUE_OF_RAM_ADDRESS = 16383
MAX_VALUE_OF_RAM_STORAGE = 65535
RAM_START_VALUE_FOR_USER = 16

#####################################################################
# Instruction code
#####################################################################

INSTRUCTION_CODE_ERROR = -1
INSTRUCTION_CODE_ANNOTATION = 0
INSTRUCTION_CODE_LABEL = 1
INSTRUCTION_CODE_A_NUMBER = 2
INSTRUCTION_CODE_A_LETTER = 3
INSTRUCTION_CODE_C_COMP = 4
INSTRUCTION_CODE_C_COMP_JUMP = 5
INSTRUCTION_CODE_C_DEST_COMP = 6
INSTRUCTION_CODE_C_DEST_COMP_JUMP = 7
