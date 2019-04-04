from pprint import pprint
class SymbolTmap:
    def __init__(self):
        self.cur_sc='begin'
        self.cur_t=SymbolT(self.cur_sc,parent=None)
        self.map_scope = dict()
        self.map_scope[self.cur_sc] = self.cur_t
        self.id_cnt=0
        self.var_cnt=0

    def create_table(self,name):
        self.map_scope[name] = SymbolT(name,self.cur_sc)
        self.cur_sc = name


    def scope_terminate(self):
        self.cur_sc = self.map_scope[self.cur_sc].parent

    def find(self,name,func=False):
        now_sc = self.cur_sc
        # print(now_sc)
        # print(func)
        # print(name)
        while now_sc != None:
            if func and name in self.map_scope[now_sc].funcs:
                return self.map_scope[now_sc].funcs[name]
            elif not func and name in self.map_scope[now_sc].vars:
                return self.map_scope[now_sc].vars[name]
            now_sc = self.map_scope[now_sc].parent
            # print(now_sc)
        return None

    def ident(self):
        self.id_cnt+=1
        return 'scope__:' + str(self.id_cnt)

    def parent_scope(self):
        return self.map_scope[self.cur_sc].parent

    def temp_var(self):
        self.var_cnt+=1
        return 't__' + str(self.var_cnt)

    def insert(self,id,type_name,func=False,params=None,arr=False,size_arr=None,scope=None):
        if scope == None:
            scope=self.cur_sc
        if func:
            self.map_scope[scope].insert_func(id,type_name,params)
        else:
            self.map_scope[scope].insert_var(id,type_name,arr,size_arr)

    def dump_TT(self):
        for i in self.map_scope.keys():
            pprint(i)
            pprint("Variables-----")
            pprint(self.map_scope[i].vars)
            pprint("Functions----")
            pprint(self.map_scope[i].funcs)
            pprint("-------------------------------")


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
        self.funcs[id]=p