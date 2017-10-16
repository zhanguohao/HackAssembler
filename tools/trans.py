def dec2bin(dec, bits=15):
	"""
	function:
		convert dec to bin
	:param dec:
	:param bits:
	:return:
	"""
	bin_nums = "{0:0{bitNums}b}".format(dec, bitNums=bits)
	return bin_nums
