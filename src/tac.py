class TAC:

    def __init__(self,ST):
    	self.ST = ST
    	# print(self.ST)
        self.code = []

    def generate_assembly(self,item):
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
			print("llllllllllllll")
			print(item[0])
			res_variable = self.ST.find(item[0])
			print(res_var)
			print("oooooooooo")

			# print(res_var)
			# print()
			if ST.find(item[1])==None:
				if ST.find(item[2])==None:
					res_var = int(item[1])+int(item[2])
					print("mov $"+res_var['offset']+","+"\%eax")
					print("add \%eax,\%rbp")
					print("mov $"+res_var+","+destination_addr)
			

    def emit(self,list_to_append):
        self.code.append(list_to_append)
        print(list_to_append)
    	self.generate_assembly(list_to_append)

    def print_tac(self):
        for ln in range(1, len(self.code) + 1):
        	print(self.code[ln-1])