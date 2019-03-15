class TAC:

    def __init__(self):
        self.code = []

    def emit(self,list_to_append):
        self.code.append(list_to_append)

    def print_tac(self):
        for ln in range(1, len(self.code) + 1):
        	print(self.code[ln-1])