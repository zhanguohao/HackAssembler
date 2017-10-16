import sys
from tools import prompt
from parser.syntax import Syntax
from symbolTable.programSymbol import SymbolTable


def main():
	args = sys.argv
	prompt.file_check(args)
	program_parser = SymbolTable()
	par = Syntax(program_parser, *args)
	par.generate_hex()


if __name__ == '__main__':
	main()
