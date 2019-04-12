# import lexer
# import ply.yacc as yacc
# import argparse
# import sys
# from tac import *
# from symbolt import SymbolTmap
# from pprint import pprint
from parser import *



def generate_assembly(item):
	if(item[0]=='func'):
		print("No imp")
	elif(item[0]=='ifgoto'):
		print("No imp")
	elif(item[0]=='goto'):
		print("No imp")
	elif(item[0]=='ret'):
		print("No imp")
	elif(item[0]=='label'):
		print("No imp")
	elif(item[0]=='call'):
		print("No imp")
	elif(item[-1]=='+'):
		res_var = ST.find(item[0])
		base_pointer=0
		print(res_var)
		destination_addr = base_pointer + res_var['offset']
		if ST.find(item[1])==None:
			if ST.find(item[2])==None:
				res_var = int(item[1])+int(item[2])
				print("mov $"+res_var+","+destination_addr)


tokens = lexer.tokens
parser = yacc.yacc()
inputfile = sys.argv[1]
code = open(inputfile, 'r').read()
code += "\n"
t = yacc.parse(code)
for i in TAC.code:
	print(i)
	generate_assembly(i)