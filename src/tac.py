class TAC:

    def __init__(self,ST):
    	self.ST = ST
    	# print(self.ST)
        self.code = []

    def generate_assembly(self,item):
		if item[0]=='func' :
			print(item[1]+':')
			print("\t push %ebp")
			print("\t mov %esp, %ebp")
		elif item[0]=='arg' :
			print("\tmov "+str(4+int(self.ST.find(item[1])['offset']))+"(%ebp), %eax")
			print("\tmov %eax, -"+str(int(self.ST.find(item[1])['offset']))+"(%ebp)")
		elif(item[0]=='ifgoto'):
			v1 = self.ST.find(item[1][0])
			v2 = self.ST.find(item[1][1])
			if v1==None:
				print("\tmov $"+item[1][0]+", %eax")
			else :
				print("\tmov -"+v1['offset']+"(%ebp), %eax")
			if v2==None:
				print("\tmov $"+item[1][1]+", %ebx")
			else :
				print("\tmov -"+v2['offset']+"(%ebp), %ebx")

			print("\tcmp %eax, %ebx")
			if item[2]=='eq':
				print("\tje "+item[3])
			elif item[2]=='neq':
				print("\tjne "+item[3])
			elif item[2]=='gt':
				print("\tjg "+item[3])	
			elif item[2]=='gte':
				print("\tjge "+item[3])	
			elif item[2]=='lt':
				print("\tjl "+item[3])
			elif item[2]=='lte':
				print("\tjle "+item[3])		
		elif(item[0]=='goto'):
			print("\tjmp "+item[1])
		elif(item[0]=='ret'):
			if(item[1]==''):
				print("\t ret")
			else:
				v = self.ST.find(item[1])
				print("\tmov -"+v[offset]+"(%ebp), %eax")
				print("\t ret")
		elif(item[0]=='label'):
			print("\t"+item[1])
		elif(item[0]=='call'):
			if(item[2]==''):
				print("\tcall "+item[1])
			else:
				print("\tcall "+item[1])
				v = self.ST.find(item[2])
				print("\t mov %eax, -"+v['offset']+"(%ebp)")
		elif(item[0]=='adjust_rsp'):
			print("\t add $"+item[1]+", %esp")
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

		elif(item[3]=='%'):

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
					print("\tmov %edx, -" + str(res_var['offset']) + "(%ebp)")
					
			else:
				if self.ST.find(item[2])==None:
					op = self.ST.find(item[1])
					print("\tmov -"+str(op['offset'])+"(%ebp),%eax")
					print("\tmov $0, %edx")
					print("\tmov $" + item[2] +",%ebx")
					print("\tidiv %ebx")
					print("\tmov %edx, -" + str(res_var['offset']) + "(%ebp)")
					
				else:
					op1 = self.ST.find(item[1])
					op2 = self.ST.find(item[2])
					print("\tmov -"+str(op1['offset'])+"(%ebp),%eax")
					print("\tmov $0, %edx")
					print("\tmov -"+str(op2['offset'])+"(%ebp),%eax")
					print("\tidiv %ebx")
					print("\tmov %edx, -" + str(res_var['offset']) + "(%ebp)")


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
					print("\tmov $" + str(val) + ",-" + str(res_var['offset'])+"(%ebp)")

				else:

					op = self.ST.find(item[2])
					print("\tmov $"+ item[1] +",%ebx")
					print("\tmov -"+str(op['offset'])+"(%ebp),%eax")

					if item[3]=='&':
						print("\tand %ebx,%eax")
					elif item[3]=="||":
						print("\tor %ebx,%eax")
					else:
						print("\txor %ebx,%eax")

					print("\tmov %ebx, -"+str(res_var['offset'])+"(%ebp)")
					
			else:

				if self.ST.find(item[2])==None:
					op = self.ST.find(item[1])
					print("\tmov $"+ item[2] +",%ebx")
					print("\tmov -"+str(op['offset'])+"(%ebp),%eax")

					if item[3]=='&':
						print("\tand %ebx,%eax")
					elif item[3]=="||":
						print("\tor %ebx,%eax")
					else:
						print("\txor %ebx,%eax")

					print("\tmov %ebx, -"+str(res_var['offset'])+"(%ebp)")
					
				else:
					op1 = self.ST.find(item[1])
					op2 = self.ST.find(item[2])
					print("\tmov -"+str(op1['offset'])+"(%ebp),%ebx")
					print("\tmov -"+str(op2['offset'])+"(%ebp),%eax")

					if item[3]=='&':
						print("\tand %ebx,%eax")
					elif item[3]=="||":
						print("\tor %ebx,%eax")
					else:
						print("\txor %ebx,%eax")

					print("\tmov %ebx, -"+str(res_var['offset'])+"(%ebp)")
					
		elif item[3]=='=':
			res_var = self.ST.find(item[0])
			op = self.ST.find(item[1])
			if op==None:
				print("\tmov $"+item[1]+",%eax")
			else:
				print("\tmov -"+str(op['offset'])+"%(ebp),%eax")
			print("\t mov %eax, -" + str(res_var['offset']) + "(%ebp)")
			

    def emit(self,list_to_append):
        self.code.append(list_to_append)
        print(list_to_append)
    	self.generate_assembly(list_to_append)

    def print_tac(self):
        for ln in range(1, len(self.code) + 1):
        	print(self.code[ln-1])
