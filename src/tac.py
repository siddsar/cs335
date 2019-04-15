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

			res_var = self.ST.find(item[0])

			if self.ST.find(item[1])==None:
				if self.ST.find(item[2])==None:
					val = int(item[1])+int(item[2])
					print("\tmov $"+str(val)+",-"+str(res_var['offset'])+"(%ebp)")
				else:
					op = self.ST.find(item[2])
					print("\tmov -"+str(op['offset'])+"(%ebp),%eax")
					print("\tadd $"+item[1]+",%eax")
					print("\tmov %eax,-"+str(res_var['offset'])+"(%ebp)")

			else:
				if self.ST.find(item[2])==None:
					op = self.ST.find(item[1])
					print("\tmov -"+str(op['offset'])+"(%ebp),%ebx")
					print("\tadd $"+item[2]+",%ebx")
					print("\tmov %ebx, -" + str(res_var['offset']) + "(%ebp)")


				else:
					op1 = self.ST.find(item[1])
					op2 = self.ST.find(item[2])
					print("\tmov -"+str(op1['offset'])+"(%ebp),%eax")
					print("\tadd -"+str(op2['offset'])+"(%ebp),%eax")
					print("\tmov %eax,-"+str(res_var['offset'])+"(%ebp)")



		elif(item[-1]=='-'):

			res_var = self.ST.find(item[0])

			if self.ST.find(item[1])==None:
				if self.ST.find(item[2])==None:
					val = int(item[1])-int(item[2])
					print("\tmov $"+str(val)+",-"+str(res_var['offset'])+"(%ebp)")
				else:
					op = self.ST.find(item[2])
					print("\tmov -"+str(op['offset'])+"(%ebp),%eax")
					print("\tmov $"+str(item[1])",%ebx")
					print("\tsub %eax,%ebx")
					print("\tmov %ebx,-"+str(res_var['offset'])+"(%ebp)")

			else:
				if self.ST.find(item[2])==None:
					op = self.ST.find(item[1])
					print("\tmov -"+str(op['offset'])+"(%ebp),%ebx")
					print("\tsub $"+item[2]+",%ebx")
					print("\tmov %ebx, -" + str(res_var['offset']) + "(%ebp)")


				else:
					op1 = self.ST.find(item[1])
					op2 = self.ST.find(item[2])
					print("\tmov -"+str(op1['offset'])+"(%ebp),%eax")
					print("\tsub -"+str(op2['offset'])+"(%ebp),%eax")
					print("\tmov %eax,-"+str(res_var['offset'])+"(%ebp)")

		elif(item[3]=='*'):

			res_var = self.ST.find(item[0])

			if self.ST.find(item[1])==None:
				if self.ST.find(item[2])==None:
					val = int(item[1])*int(item[2])
					print("\tmov $"+str(val)+",-"+str(res_var['offset'])+"(%ebp)")
				else:
					op = self.ST.find(item[2])
					print("\tmov -"+str(op['offset'])+"(%ebp),%eax")
					print("\timul $"+item[1]+",%eax")
					print("\tmov %eax,-"+str(res_var['offset'])+"(%ebp)")

			else:
				if self.ST.find(item[2])==None:
					op = self.ST.find(item[1])
					print("\tmov -"+str(op['offset'])+"(%ebp),%ebx")
					print("\timul $"+item[2]+",%ebx")
					print("\tmov %ebx, -" + str(res_var['offset']) + "(%ebp)")


				else:
					op1 = self.ST.find(item[1])
					op2 = self.ST.find(item[2])
					print("\tmov -"+str(op1['offset'])+"(%ebp),%eax")
					print("\timul -"+str(op2['offset'])+"(%ebp),%eax")
					print("\tmov %eax,-"+str(res_var['offset'])+"(%ebp)")

		elif(item[3]=='/'):

			res_var = self.ST.find(item[0])

			if self.ST.find(item[1])==None:
				if self.ST.find(item[2])==None:
					val = int(item[1])/int(item[2])
					print("\tmov $"+str(val)+",-"+str(res_var['offset'])+"(%ebp)")
				else:
					op = self.ST.find(item[2])
					dx = int(item[1])>>32
					ax = ((int(item[1])<<32)>>32)
					print("\tmov $" + str(dx) + ", %edx")
					print("\tmov $" + str(ax) + ", %eax")
					print("\tidiv -" + str(op['offset'])+"(%ebp)")
					print("\tmov %eax, -" + str(res_var['offset']) + "(%ebp)")
					
			else:
				if self.ST.find(item[2])==None:
					op = self.ST.find(item[1])
					print("\tmov -"+str(op['offset'])+"(%ebp),%eax")
					print("\tmov $0, %edx")
					print("\tmov $" + item[2] +",%ebx")
					print("\tidiv %ebx")
					print("\tmov %eax, -" + str(res_var['offset']) + "(%ebp)")
					
				else:
					op1 = self.ST.find(item[1])
					op2 = self.ST.find(item[2])
					print("\tmov -"+str(op1['offset'])+"(%ebp),%eax")
					print("\tmov $0, %edx")
					print("\tmov -"+str(op2['offset'])+"(%ebp),%eax")
					print("\tidiv %ebx")
					print("\tmov %eax, -" + str(res_var['offset']) + "(%ebp)")


		elif(item[3]=='&' or item[3]=="||" or item[3]=='^'):

			res_var = self.ST.find(item[0])

			if self.ST.find(item[1])==None:

				if self.ST.find(item[2])==None:

					if item[3]=='&':
						val = int(item[1]) and int(item[2])
					elif item[3]=="||":
						val = int(item[1]) or int(item[2])
					else:
						val = int(item[1])^int(item[2])
					print("mov $" + str(val) + ",-" + str(res_var['offset'])+"(%ebp)")

				else:

					op = self.ST.find(item[2])
					print("mov $"+ item[1] +",%ebx")
					print("mov -"+str(op['offset'])+"(%ebp),%eax")

					if item[3]=='&':
						print("and %ebx,%eax")
					elif item[3]=="||":
						print("or %ebx,%eax")
					else:
						print("xor %ebx,%eax")

					print("mov %ebx, -"+str(res_var['offset'])+"(%ebp)")
					
			else:

				if self.ST.find(item[2])==None:
					op = self.ST.find(item[1])
					print("mov $"+ item[2] +",%ebx")
					print("mov -"+str(op['offset'])+"(%ebp),%eax")

					if item[3]=='&':
						print("and %ebx,%eax")
					elif item[3]=="||":
						print("or %ebx,%eax")
					else:
						print("xor %ebx,%eax")

					print("mov %ebx, -"+str(res_var['offset'])+"(%ebp)")
					
				else:
					op1 = self.ST.find(item[1])
					op2 = self.ST.find(item[2])
					print("mov -"+str(op1['offset'])+"(%ebp),%ebx")
					print("mov -"+str(op2['offset'])+"(%ebp),%eax")

					if item[3]=='&':
						print("and %ebx,%eax")
					elif item[3]=="||":
						print("or %ebx,%eax")
					else:
						print("xor %ebx,%eax")

					print("mov %ebx, -"+str(res_var['offset'])+"(%ebp)")
					
		# elif item[3]=='=':
			# res_var = self.ST.find(item[0])
			# op = self.ST.find(item[1])
			# if op==None:
			# 	print("mov $"+str(res_var['offset'])+",%eax")
			# 	print(" addl %rbp,%eax")
			# 	print("mov $"+str(item[1])+",0(%eax)")
			# else:
			# 	print("mov $"+str(op['offset'])+",%ebx")
			# 	print("addl %rbp,%ebx")
			# 	print("mov (%ebx),%eax")
			# 	print("mov $"+str(res_var['offset'])+",%ebx")
			# 	print("addl %rbp,%ebx")
			# 	print("mov %eax,0(%ebx)")

    def emit(self,list_to_append):
        self.code.append(list_to_append)
        print(list_to_append)
    	self.generate_assembly(list_to_append)

    def print_tac(self):
        for ln in range(1, len(self.code) + 1):
        	print(self.code[ln-1])
