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
					print("mov $"+str(res_var['offset'])+",%eax")
					print("addl %rbp,%eax")
					print("mov $"+str(val)+",0(%eax)")
				else:
					op = self.ST.find(item[2])
					print("mov $"+str(op['offset'])+",%ebx")
					print("addl %rbp,%ebx")
					print("mov (%ebx),%eax")
					print("mov $"+item[1]+",%ebx")
					print("addl %eax,%ebx")
					print("mov $"+str(res_var['offset'])+",%eax")
					print("addl %rbp,%eax")
					print("mov %ebx,0(%eax)")
			else:
				if self.ST.find(item[2])==None:
					op = self.ST.find(item[1])
					print("mov $"+str(op['offset'])+",%ebx")
					print("addl %rbp,%ebx")
					print("mov (%ebx),%eax")
					print("mov $"+item[2]+",%ebx")
					print("addl %eax,%ebx")
					print("mov $"+str(res_var['offset'])+",%eax")
					print("addl %rbp,%eax")
					print("mov %ebx,0(%eax)")
				else:
					print("mov $"+str(self.ST.find(item[1])['offset'])+",%ecx")
					print("addl %rbp,%ecx")
					print("mov (%ecx),%eax")
					print("mov $"+str(self.ST.find(item[2])['offset'])+",%ecx")
					print("addl %rbp,%ecx")
					print("mov (%ecx),%ebx")
					print("addl %eax,%ebx")
					print("mov $"+str(res_var['offset'])+",%eax")
					print("addl %rbp,%eax")
					print("mov %ebx,0(%eax)")
		elif(item[3]=='-'):
			res_var = self.ST.find(item[0])
			if self.ST.find(item[1])==None:
				if self.ST.find(item[2])==None:
					val = int(item[1])-int(item[2])
					print("mov $"+str(res_var['offset'])+",%eax")
					print("addl %rbp,%eax")
					print("mov $"+str(val)+",0(%eax)")
				else:
					op = self.ST.find(item[2])
					print("mov $"+str(op['offset'])+",%ebx")
					print("addl %rbp,%ebx")
					print("mov (%ebx),%eax")
					print("mov $"+item[1]+",%ebx")
					print("subl %eax,%ebx")
					print("mov $"+str(res_var['offset'])+",%eax")
					print("addl %rbp,%eax")
					print("mov %ebx,0(%eax)")
			else:
				if self.ST.find(item[2])==None:
					op = self.ST.find(item[1])
					print("mov $"+str(op['offset'])+",%ebx")
					print("addl %rbp,%ebx")
					print("mov (%ebx),%eax")
					print("mov $"+item[2]+",%ebx")
					print("subl %ebx,%eax")
					print("mov $"+str(res_var['offset'])+",%ebx")
					print("addl %rbp,%ebx")
					print("mov %eax,0(%ebx)")
				else:
					print("mov $"+str(self.ST.find(item[1])['offset'])+",%ecx")
					print("addl %rbp,%ecx")
					print("mov (%ecx),%eax")
					print("mov $"+str(self.ST.find(item[2])['offset'])+",%ecx")
					print("addl %rbp,%ecx")
					print("mov (%ecx),%ebx")
					print("subl %ebx,%eax")
					print("mov $"+str(res_var['offset'])+",%ebx")
					print("addl %rbp,%ebx")
					print("mov %eax,0(%ebx)")
		elif(item[3]=='*'):
			res_var = self.ST.find(item[0])
			if self.ST.find(item[1])==None:
				if self.ST.find(item[2])==None:
					val = int(item[1])*int(item[2])
					print("mov $"+str(res_var['offset'])+",%eax")
					print("addl %rbp,%eax")
					print("mov $"+str(val)+",0(%eax)")
				else:
					op = self.ST.find(item[2])
					print("mov $"+str(op['offset'])+",%ebx")
					print("addl %rbp,%ebx")
					print("mov (%ebx),%eax")
					print("mov $"+item[1]+",%ebx")
					print("imul %eax,%ebx")
					print("mov $"+str(res_var['offset'])+",%eax")
					print("addl %rbp,%eax")
					print("mov %ebx,0(%eax)")
			else:
				if self.ST.find(item[2])==None:
					op = self.ST.find(item[1])
					print("mov $"+str(op['offset'])+",%ebx")
					print("addl %rbp,%ebx")
					print("mov (%ebx),%eax")
					print("mov $"+item[2]+",%ebx")
					print("imul %ebx,%eax")
					print("mov $"+str(res_var['offset'])+",%ebx")
					print("addl %rbp,%ebx")
					print("mov %eax,0(%ebx)")
				else:
					print("mov $"+str(self.ST.find(item[1])['offset'])+",%ecx")
					print("addl %rbp,%ecx")
					print("mov (%ecx),%eax")
					print("mov $"+str(self.ST.find(item[2])['offset'])+",%ecx")
					print("addl %rbp,%ecx")
					print("mov (%ecx),%ebx")
					print("imul %ebx,%eax")
					print("mov $"+str(res_var['offset'])+",%ebx")
					print("addl %rbp,%ebx")
					print("mov %eax,0(%ebx)")
		# elif(item[3]=='/'):
		# 	res_var = self.ST.find(item[0])
		# 	if self.ST.find(item[1])==None:
		# 		if self.ST.find(item[2])==None:
		# 			val = int(item[1])/int(item[2])
		# 			print("mov $"+str(res_var['offset'])+",%eax")
		# 			print("addl %rbp,%eax")
		# 			print("mov $"+str(val)+",0(%eax)")
		# 		else:
		# 			op = self.ST.find(item[2])
		# 			print("mov $"+str(op['offset'])+",%ebx")
		# 			print("addl %rbp,%ebx")
		# 			print("mov (%ebx),%eax")
		# 			print("mov $"+item[1]+",%ebx")
		# 			print("idiv %eax,%ebx")
		# 			print("mov $"+str(res_var['offset'])+",%eax")
		# 			print("addl %rbp,%eax")
		# 			print("mov %ebx,0(%eax)")
		# 	else:
		# 		if self.ST.find(item[2])==None:
		# 			op = self.ST.find(item[1])
		# 			print("mov $"+str(op['offset'])+",%ebx")
		# 			print("addl %rbp,%ebx")
		# 			print("mov (%ebx),%eax")
		# 			print("mov $"+item[2]+",%ebx")
		# 			print("idiv %ebx,%eax")
		# 			print("mov $"+str(res_var['offset'])+",%ebx")
		# 			print("addl %rbp,%ebx")
		# 			print("mov %eax,0(%ebx)")
		# 		else:
		# 			print("mov $"+str(self.ST.find(item[1])['offset'])+",%ecx")
		# 			print("addl %rbp,%ecx")
		# 			print("mov (%ecx),%eax")
		# 			print("mov $"+str(self.ST.find(item[2])['offset'])+",%ecx")
		# 			print("addl %rbp,%ecx")
		# 			print("mov (%ecx),%ebx")
		# 			print("idiv %ebx,%eax")
		# 			print("mov $"+str(res_var['offset'])+",%ebx")
		# 			print("addl %rbp,%ebx")
		# 			print("mov %eax,0(%ebx)")
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
					print("mov $"+str(res_var['offset'])+",%eax")
					print("addl %rbp,%eax")
					print("mov $"+str(val)+",0(%eax)")
				else:
					op = self.ST.find(item[2])
					print("mov $"+str(op['offset'])+",%ebx")
					print("addl %rbp,%ebx")
					print("mov (%ebx),%eax")
					print("mov $"+item[1]+",%ebx")
					if item[3]=='&':
						print("and %ebx,%eax")
					elif item[3]=="||":
						print("or %ebx,%eax")
					else:
						print("xor %ebx,%eax")
					print("mov $"+str(res_var['offset'])+",%eax")
					print("addl %rbp,%eax")
					print("mov %ebx,0(%eax)")
			else:
				if self.ST.find(item[2])==None:
					op = self.ST.find(item[1])
					print("mov $"+str(op['offset'])+",%ebx")
					print("addl %rbp,%ebx")
					print("mov (%ebx),%eax")
					print("mov $"+item[2]+",%ebx")
					if item[3]=='&':
						print("and %eax,%ebx")
					elif item[3]=="||":
						print("or %eax,%ebx")
					else:
						print("xor %eax,%ebx")
					print("mov $"+str(res_var['offset'])+",%ebx")
					print("addl %rbp,%ebx")
					print("mov %eax,0(%ebx)")
				else:
					print("mov $"+str(self.ST.find(item[1])['offset'])+",%ecx")
					print("addl %rbp,%ecx")
					print("mov (%ecx),%eax")
					print("mov $"+str(self.ST.find(item[2])['offset'])+",%ecx")
					print("addl %rbp,%ecx")
					print("mov (%ecx),%ebx")
					if item[3]=='&':
						print("and %eax,%bax")
					elif item[3]=="||":
						print("or %eax,%ebx")
					else:
						print("xor %eax,%ebx")
					print("mov $"+str(res_var['offset'])+",%ebx")
					print("addl %rbp,%ebx")
					print("mov %eax,0(%ebx)")
		elif item[3]=='=':
			res_var = self.ST.find(item[0])
			op = self.ST.find(item[1])
			print(res_var['type'])
			print("lkqiwbiebuyveufyvuyv")
			# if op==None:
			# 	print("mov $"+str(res_var['offset'])+",%eax")
			# 	# print("addl %rbp,%eax")
			# 	print("mov $"+str(item[1])+",0(%eax)")
			# else:
			# 	print("mov $"+str(op['offset'])+",%ebx")
			# 	print("addl %rbp,%ebx")
			# 	print("mov (%ebx),%eax")
			# 	print("mov $"+str(res_var['offset'])+",%ebx")
			# 	# print("mov $"+str(res_var['offset'])+",%ebx")
			# 	print("addl %rbp,%ebx")
			# 	print("mov %eax,0(%ebx)")

    def emit(self,list_to_append):
        self.code.append(list_to_append)
        print(list_to_append)
    	self.generate_assembly(list_to_append)

    def print_tac(self):
        for ln in range(1, len(self.code) + 1):
        	print(self.code[ln-1])