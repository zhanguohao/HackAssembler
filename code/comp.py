import Constant


class Compute:
	@staticmethod
	def get_code(code):
		if code == "zero":
			return Constant.C_INSTRUCTION + Constant.COMP_INSTRUCTION_A_NOT_M + Constant.COMP_INSTRUCTION_ZERO
		elif code == "one":
			return Constant.C_INSTRUCTION + Constant.COMP_INSTRUCTION_A_NOT_M + Constant.COMP_INSTRUCTION_ONE
		elif code == "neg_one":
			return Constant.C_INSTRUCTION + Constant.COMP_INSTRUCTION_A_NOT_M + Constant.COMP_INSTRUCTION_NEG_ONE
		elif code == "D":
			return Constant.C_INSTRUCTION + Constant.COMP_INSTRUCTION_A_NOT_M + Constant.COMP_INSTRUCTION_D
		elif code == "A":
			return Constant.C_INSTRUCTION + Constant.COMP_INSTRUCTION_A_NOT_M + Constant.COMP_INSTRUCTION_AM
		elif code == "M":
			return Constant.C_INSTRUCTION + Constant.COMP_INSTRUCTION_M_NOT_A + Constant.COMP_INSTRUCTION_AM
		elif code == "not_d":
			return Constant.C_INSTRUCTION + Constant.COMP_INSTRUCTION_A_NOT_M + Constant.COMP_INSTRUCTION_NOT_D
		elif code == "not_a":
			return Constant.C_INSTRUCTION + Constant.COMP_INSTRUCTION_A_NOT_M + Constant.COMP_INSTRUCTION_NOT_AM
		elif code == "not_m":
			return Constant.C_INSTRUCTION + Constant.COMP_INSTRUCTION_M_NOT_A + Constant.COMP_INSTRUCTION_NOT_AM
		elif code == "neg_d":
			return Constant.C_INSTRUCTION + Constant.COMP_INSTRUCTION_A_NOT_M + Constant.COMP_INSTRUCTION_NEG_D
		elif code == "neg_a":
			return Constant.C_INSTRUCTION + Constant.COMP_INSTRUCTION_A_NOT_M + Constant.COMP_INSTRUCTION_NEG_AM
		elif code == "neg_m":
			return Constant.C_INSTRUCTION + Constant.COMP_INSTRUCTION_M_NOT_A + Constant.COMP_INSTRUCTION_NEG_AM
		elif code == "d_plus_one":
			return Constant.C_INSTRUCTION + Constant.COMP_INSTRUCTION_A_NOT_M + Constant.COMP_INSTRUCTION_D_PLUS_ONE
		elif code == "a_plus_one":
			return Constant.C_INSTRUCTION + Constant.COMP_INSTRUCTION_A_NOT_M + Constant.COMP_INSTRUCTION_AM_PLUS_ONE
		elif code == "m_plus_one":
			return Constant.C_INSTRUCTION + Constant.COMP_INSTRUCTION_M_NOT_A + Constant.COMP_INSTRUCTION_AM_PLUS_ONE
		elif code == "d_minus_one":
			return Constant.C_INSTRUCTION + Constant.COMP_INSTRUCTION_A_NOT_M + Constant.COMP_INSTRUCTION_D_MINUS_ONE
		elif code == "a_minus_one":
			return Constant.C_INSTRUCTION + Constant.COMP_INSTRUCTION_A_NOT_M + Constant.COMP_INSTRUCTION_AM_MINUS_ONE
		elif code == "m_minus_one":
			return Constant.C_INSTRUCTION + Constant.COMP_INSTRUCTION_M_NOT_A + Constant.COMP_INSTRUCTION_AM_MINUS_ONE
		elif code == "d_plus_a":
			return Constant.C_INSTRUCTION + Constant.COMP_INSTRUCTION_A_NOT_M + Constant.COMP_INSTRUCTION_D_PLUS_AM
		elif code == "d_plus_m":
			return Constant.C_INSTRUCTION + Constant.COMP_INSTRUCTION_M_NOT_A + Constant.COMP_INSTRUCTION_D_PLUS_AM
		elif code == "d_minus_a":
			return Constant.C_INSTRUCTION + Constant.COMP_INSTRUCTION_A_NOT_M + Constant.COMP_INSTRUCTION_D_MINUS_AM
		elif code == "d_minus_m":
			return Constant.C_INSTRUCTION + Constant.COMP_INSTRUCTION_M_NOT_A + Constant.COMP_INSTRUCTION_D_MINUS_AM
		elif code == "a_minus_d":
			return Constant.C_INSTRUCTION + Constant.COMP_INSTRUCTION_A_NOT_M + Constant.COMP_INSTRUCTION_AM_MINUS_D
		elif code == "m_minus_d":
			return Constant.C_INSTRUCTION + Constant.COMP_INSTRUCTION_M_NOT_A + Constant.COMP_INSTRUCTION_AM_MINUS_D
		elif code == "d_and_a":
			return Constant.C_INSTRUCTION + Constant.COMP_INSTRUCTION_A_NOT_M + Constant.COMP_INSTRUCTION_D_AND_AM
		elif code == "d_and_m":
			return Constant.C_INSTRUCTION + Constant.COMP_INSTRUCTION_M_NOT_A + Constant.COMP_INSTRUCTION_D_AND_AM
		elif code == "d_or_a":
			return Constant.C_INSTRUCTION + Constant.COMP_INSTRUCTION_A_NOT_M + Constant.COMP_INSTRUCTION_D_OR_AM
		elif code == "d_or_m":
			return Constant.C_INSTRUCTION + Constant.COMP_INSTRUCTION_M_NOT_A + Constant.COMP_INSTRUCTION_D_OR_AM
		else:
			return Constant.C_INSTRUCTION + Constant.COMP_INSTRUCTION_A_NOT_M + Constant.COMP_INSTRUCTION_ZERO
