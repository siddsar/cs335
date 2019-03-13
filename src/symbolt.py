class SymbolTmap:
    def __init__(self):
        self.cur_sc='begin'
        self.cur_t=SymbolT(self.cur_sc,parent=None)
        self.map_scope = dict()
        self.map_scope[self.cur_sc] = self.cur_t
        self.id_cnt=0
        self.var_cnt=0

    def create_table(self,name):
        self.cur_sc = name
        self.map_scope[self.cur_sc] = SymbolT(name,self.cur_sc)

    def scope_terminate(self):
        self.cur_sc = self.map_scope[self.cur_sc].parent

    def lookup(self,name,func):
        now_sc = self.cur_sc
        while now_sc != None:
            if func and name in self.map_scope[self.cur_sc].funcs:
                return self.map_scope[self.cur_sc].funcs[name]
            elif not func and name in self.map_scope[self.cur_sc].vars:
                return self.map_scope[self.cur_sc].vars[name]
            now_sc = self.map_scope[self.cur_sc].parent

        return None

    def ident(self):
        self.cnt++
        return 'scope__:' + str(self.cnt)

    def parent_scope(self):
        return self.map_scope[self.cur_sc].parent

    def temp_var(self):
        self.var_cnt++
        return 't__' + str(self.var_cnt)

    def insert(self,id,type_name,func=False,params=None,arr=False,size_arr=None,scope=None):
        if scope == None:
            scope=self.cur_sc
        if func:
            self.map_scope[scope].insert_func(id,type_name,params)
        else:
            self.map_scope[scope].insert_var(id,type_name,is_array,size_arr)

    def dump_TT(self):
        # TODO

class SymbolT:
    def __init__(self, name, parent):
        self.parent = parent
        self.scope = name
        self.vars = dict()
        self.funcs = dict()

    def insert_var(self,id,type_name,arr=False,size_arr=None):
        if id in self.vars.keys():
            raise Exception('Variable %s is already declared before!' %(id))
        p = { 'type':type_name, 'arr':arr, 'size':size_arr }
        self.vars[id]=p

    def insert_func(self,id,type_name,params):
        if id in self.funcs.keys():
            raise Exception('Function %s is already declared before!' %(id))
        p = { 'type':type_name, 'params':params, 'number_params':len(params) }
        self.vars[id]=p

    def dump_T(self):
        # TODO

#     def print_table(self):
#         print("Parent: %s" %(self.parent))
#         print("Scope: %s \nSymbols:" %(self.scope))
#         for key, val in self.symbols.items():
#             print(key,val)
#         print("Functions:")
#         for key, val in self.functions.items():
#             print(key,val)
# print("*************************")
