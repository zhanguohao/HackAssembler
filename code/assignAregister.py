import Constant
from tools import trans


class AInstrction:
	@staticmethod
	def get_code(code):
		return Constant.A_INSTRUCTION + trans.dec2bin(int(code), 15)
