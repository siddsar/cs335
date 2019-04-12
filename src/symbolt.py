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
        return 'kaizoku_' + str(self.var_cnt)

    def insert(self,id,type_name,func=False,params=None,arr=False,size_arr=None,scope=None,temp=False):
        if scope == None:
            scope=self.cur_sc
        if func:
            self.map_scope[scope].insert_func(id,type_name,params)
        else:
            self.map_scope[scope].insert_var(id,type_name,arr,size_arr,temp)

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
        self.offset = 0

    def find_size(self,type_name):
        type_name = type_name.upper()

        if(type_name == 'INT'):
            return 4
        elif( type_name == 'FLOAT'):
            return 4
        elif(type_name == 'CHAR'):
            return 1
        elif(type_name == 'BYTE'):
            return 1
        elif(type_name == 'SHORT'):
            return 2
        elif( type_name == 'DOUBLE'):
            return 8
        elif( type_name == 'LONG'):
            return 8


    def insert_var(self,id,type_name,arr=False,size_arr=None,temp=False):
        if id in self.vars.keys():
            raise Exception('Variable %s is already declared before!' %(id))

        size = self.find_size(type_name)
        if(arr):
            self.offset += (size_arr * size)
        else:
            self.offset += size

        p = { 'type':type_name, 'arr':arr, 'size_arr':size_arr , 'offset':self.offset, 'temp':temp}
        self.vars[id]=p

    def insert_func(self,id,type_name,params):
        if id in self.funcs.keys():
            raise Exception('Function %s is already declared before!' %(id))
        p = { 'type':type_name, 'params':params, 'number_params':len(params) }
        self.funcs[id]=p
