import lexer
import ply.yacc as yacc
import argparse
import sys
from tac import *
from symbolt import SymbolTmap
from pprint import pprint

parser = argparse.ArgumentParser()
parser.add_argument("mode")
parser.parse_args()

tokens = lexer.tokens
ST = SymbolTmap()
TAC = TAC(ST)
rules_store = []
global_return_type = None
global_method = None
offset_stack = []
offset_stack.append(0)

def p_Goal(p):
    '''Goal : CompilationUnit'''
    rules_store.append(p.slice)
def p_Literal(p):
    ''' Literal :   IntConst
                  | FloatConst
                  | CharConst
                  | StringConst
                  | NullConst
    '''
    p[0] = p[1]
    p[0]['idVal'] = str(p[0]['idVal'])
    p[0]['is_var'] = False
    rules_store.append(p.slice)
def p_IntConst(p):
    '''
    IntConst : INT_LITERAL
    '''
    p[0] = {
        'idVal' : p[1],
        'type' : 'INT'
    }
    rules_store.append(p.slice)
def p_FloatConst(p):
    '''
    FloatConst : FLOAT_LITERAL
    '''
    p[0] = {
        'idVal' : p[1],
        'type' : 'FLOAT'
    }
    rules_store.append(p.slice)
def p_CharConst(p):
    '''
    CharConst : CHAR_LITERAL
    '''
    p[0] = {
        'idVal' : p[1],
        'type' : 'CHAR'
    }
    rules_store.append(p.slice)
def p_StringConst(p):
    '''
    StringConst : STRING_LITERAL
    '''
    p[0] = {
        'idVal' : p[1],
        'type' : 'STRING'
    }
    rules_store.append(p.slice)
def p_NullConst(p):
    '''
    NullConst : NULL
    '''
    p[0] = {
        'idVal' : p[1],
        'type' : 'NULL'
    }
    rules_store.append(p.slice)
def p_Type(p):
    ''' Type : PrimitiveType
            | ReferenceType '''
    p[0] = p[1]
    rules_store.append(p.slice)
def p_PrimitiveType(p):
    ''' PrimitiveType :    NumericType
                         | BOOLEAN
    '''
    if type(p[1]) != type({}):
        p[0] = {
            'type' : 'INT'  # treat boolean as integer for now
        }
    else:
        p[0] = p[1]

    rules_store.append(p.slice)
def p_NumericType(p):
    ''' NumericType :   IntegralType
                      | FloatingPointType
    '''
    p[0] = p[1]
    rules_store.append(p.slice)
def p_IntegralType(p):
    ''' IntegralType :    BYTE
                        | SHORT
                        | INT
                        | LONG
                        | CHAR
    '''
    p[0] = {
        'type' : p[1].upper()
    }
    rules_store.append(p.slice)
def p_FloatingPointType(p):
    ''' FloatingPointType :   FLOAT
                            | DOUBLE
    '''
    p[0] = {
        'type' : p[1].upper()
    }

    rules_store.append(p.slice)
def p_ReferenceType(p):
    ''' ReferenceType :   ArrayType
                        | ClassType
    '''
    p[0] = p[1]
    rules_store.append(p.slice)
def p_ClassType(p):
    ''' ClassType : Name
    '''
    p[0] = p[1]
    p[0]['type'] = 'class'
    rules_store.append(p.slice)
def p_ArrayType(p):
    ''' ArrayType :    PrimitiveType Dims
                     | Name Dims
    '''
    if 'place' in p[1].keys():
        p[0] = {
            'type' : p[1]['place']
        }
    else:
        p[0] = {
            'type' : p[1]['type'],
        }
    p[0]['is_array'] = True
    p[0]['arr_size'] = p[2]

    rules_store.append(p.slice)
def p_Name(p):
    ''' Name :    SimpleName
                | QualifiedName '''
    p[0] = p[1]
    p[0]['is_var'] = True
    rules_store.append(p.slice)
def p_SimpleName(p):
    ''' SimpleName : IDENTIFIER'''
    p[0] = {
        'place' : p[1],
    }

    rules_store.append(p.slice)
def p_QualifiedName(p):
    ''' QualifiedName : Name DOT IDENTIFIER'''
    p[0]= {
        'place' : p[1]['place'] + "." + p[3]
    }
    rules_store.append(p.slice)
def p_CompilationUnit(p):
    '''
    CompilationUnit : PackageDeclaration ImportDeclarations TypeDeclarations
    | PackageDeclaration ImportDeclarations
    | PackageDeclaration TypeDeclarations
    | ImportDeclarations TypeDeclarations
    | PackageDeclaration
    | ImportDeclarations
    | TypeDeclarations
    |
    '''

    rules_store.append(p.slice)
def p_ImportDeclarations(p):
    '''
    ImportDeclarations : ImportDeclaration
    | ImportDeclarations ImportDeclaration
    '''

    rules_store.append(p.slice)
def p_TypeDeclarations(p):
    '''
    TypeDeclarations : TypeDeclaration
    | TypeDeclarations TypeDeclaration
    '''

    rules_store.append(p.slice)
def p_PackageDeclaration(p):
    '''
    PackageDeclaration : PACKAGE Name STMT_TERMINATOR
    '''

    rules_store.append(p.slice)
def p_ImportDeclaration(p):
    '''
    ImportDeclaration : SingleTypeImportDeclaration
    | TypeImportOnDemandDeclaration
    '''

    rules_store.append(p.slice)
def p_SingleTypeImportDeclaration(p):
    '''
    SingleTypeImportDeclaration : IMPORT Name STMT_TERMINATOR
    '''

    rules_store.append(p.slice)
def p_TypeImportOnDemandDeclaration(p):
    '''
    TypeImportOnDemandDeclaration : IMPORT Name DOT MULT STMT_TERMINATOR
    '''

    rules_store.append(p.slice)
def p_TypeDeclaration(p):
    '''
    TypeDeclaration : ClassDeclaration
    | STMT_TERMINATOR
    '''

    rules_store.append(p.slice)
def p_Modifiers(p):
    '''
    Modifiers : Modifier
    | Modifiers Modifier
    '''

    rules_store.append(p.slice)
def p_Modifier(p):
    '''
    Modifier : STATIC
    | FINAL
    | PUBLIC
    | PROTECTED
    | PRIVATE
    | ABSTRACT
    | VOLATILE
    | SYNCHRONIZED
    | TRANSIENT
    | NATIVE
    '''
    rules_store.append(p.slice)
def p_ClassDeclaration(p):
    '''
    ClassDeclaration : Modifiers CLASS IDENTIFIER Super ClassBody
    | Modifiers CLASS IDENTIFIER ClassBody
    | CLASS IDENTIFIER Super ClassBody
    | CLASS IDENTIFIER ClassBody
    '''

    rules_store.append(p.slice)
def p_Super(p):
    '''
    Super : EXTENDS ClassType
    '''
    rules_store.append(p.slice)
def p_ClassBody(p):
    '''
    ClassBody : L_CURLYBR R_CURLYBR
    | L_CURLYBR ClassBodyDeclarations R_CURLYBR
    '''

    rules_store.append(p.slice)
def p_ClassBodyDeclarations(p):
    '''
    ClassBodyDeclarations : ClassBodyDeclaration
    | ClassBodyDeclarations ClassBodyDeclaration
    '''

    rules_store.append(p.slice)
def p_ClassBodyDeclaration(p):
    '''
    ClassBodyDeclaration : ClassMemberDeclaration
    | ConstructorDeclaration
    | StaticInitializer
    '''

    rules_store.append(p.slice)
def p_ClassMemberDeclaration(p):
    '''
    ClassMemberDeclaration : FieldDeclaration
    | MethodDeclaration
    '''

    rules_store.append(p.slice)
def p_FieldDeclaration(p):
    '''
    FieldDeclaration : Modifiers Type VariableDeclarators STMT_TERMINATOR
    | Type VariableDeclarators STMT_TERMINATOR
    '''

    rules_store.append(p.slice)
def p_VariableDeclarators(p):
    '''
    VariableDeclarators : VariableDeclarator
    | VariableDeclarators COMMA VariableDeclarator
    '''
    if len(p)==2:
    	p[0]=[p[1]]
    else:
    	p[0] = p[1] + [p[3]]

    rules_store.append(p.slice)
def p_VariableDeclarator(p):
    '''
    VariableDeclarator : VariableDeclaratorId
    | VariableDeclaratorId ASSIGN VariableInitializer
    '''
    p[0] = {}
    to_emit = []
    if len(p) == 2:
        p[0]['place'] = p[1]
        # p[0]['assign'] = None
        return
    elif type(p[3]) != type({}):
        return
    if 'fields' in p[3].keys():
        obj_name = p[1] + "_obj_" + p[3]['name']
        size = p[3]['count']
        # to_emit.append(['declare', p[1], t, p[3]['type'], ST])
        t = ST.temp_var()
        ST.insert(t,'INT',temp=True)
        to_emit.append([t, str(size), '', '='])
        to_emit.append(['declare', obj_name, t, 'INT'])
        p[0]['class_name'] = p[3]['name']
        p[0]['place'] = p[1]
        p[0]['emit_intrs'] = to_emit
        ST.insert(obj_name, 'INT', arr=True, size_arr=size)
        return

    if 'is_array' in p[3].keys() and p[3]['is_array']:
        t = ST.temp_var()
        ST.insert(t,'INT',temp=True)
        # to_emit.append([t, '1', '', '='])
        # for i in p[3]['place']:
        #     to_emit.append([t, t, i, '*'])
        # to_emit.append(['declare', p[1], t, p[3]['type']])
        p[0]['place'] = (p[1], p[3]['place'])
        p[0]['type'] = p[3]['type']
        p[0]['emit_intrs'] = to_emit
    elif 'ret_type' in p[3].keys():
        p[0]['place'] = p[1]
        p[0]['type'] = p[3]['ret_type']
        to_emit.append([p[1], p[3]['place'], '', '='])
        p[0]['emit_intrs'] = to_emit

    else:
        to_emit.append([p[1], p[3]['place'], '', p[2]])
        p[0]['place'] = p[1]
        if 'is_var' not in p[3]:
            attributes = ST.find(p[3]['place'])
            if attributes == None:
                p[0]['type'] = p[3]['type']
                p[0]['emit_intrs'] = to_emit
                return
            if 'is_array' in attributes and attributes['is_array']:
                p[0]['is_array'] = True
                p[0]['arr_size'] = attributes['arr_size']
            else:
                p[0]['is_array'] = False

        p[0]['type'] = p[3]['type']
        p[0]['emit_intrs'] = to_emit
        # p[0]['assign'] = p[3]['place']
        # p[0]['place'] = p[1]
        # if 'is_var' not in p[3]:
        #     pprint(rules_store)
        #     pprint(p[3])
        #     print("-------------------------------++++++++++++++++")
        #     attributes = ST.find(p[3]['place'])
        #     # if 'is_array' in attributes and attributes['is_array']:
        #     #     p[0]['is_array'] = True
        #     #     p[0]['arr_size'] = attributes['arr_size']
        #     # else:
        #     p[0]['is_array'] = False
        #
        # p[0]['type'] = p[3]['type']
    # pprint(p[0])
    # print("lol")
    rules_store.append(p.slice)

def p_VariableDeclaratorId(p):
    '''
    VariableDeclaratorId : IDENTIFIER
    '''
    p[0] = p[1]

    rules_store.append(p.slice)
def p_VariableInitializer(p):
    '''
    VariableInitializer : Expression
    | ArrayInitializer
    '''
    p[0] = p[1]

    rules_store.append(p.slice)
def p_MethodDeclaration(p):
    '''
    MethodDeclaration : MethodHeader MethodAddParentScope MethodBody
    '''
    p[0]=p[1]
    global global_method
    global_method = p[1]['name']
    TAC.emit(['ret','',p[1]['name'],''])
    ST.scope_terminate()
    offset_stack.pop()

    rules_store.append(p.slice)
def p_MethodAddParentScope(p):
    '''
    MethodAddParentScope :
    '''
    par_scope = ST.parent_scope()
    # pprint(p[-1])
    # print(par_scope)
    offset_stack[-1] += ST.insert(p[-1]['name'], p[-1]['type'],func=True, params=p[-1]['args'], scope=par_scope)
    # print(p[-1]['name'], p[-1]['type'],True, p[-1]['args'], par_scope)

    rules_store.append(p.slice)
def p_MethodHeader(p):
    '''
    MethodHeader : Modifiers Type MethodDeclarator Throws
    | Modifiers Type MethodDeclarator
    | Type MethodDeclarator Throws
    | Type MethodDeclarator
    | Modifiers VOID MethodDeclarator Throws
    | Modifiers VOID MethodDeclarator
    | VOID MethodDeclarator Throws
    | VOID MethodDeclarator
    '''
    p[0] = {}
    if len(p) == 5:
        # TODO
        pass
    elif len(p) == 4:
        p[0]['name'] = p[3]['name']
        p[0]['args'] = p[3]['args']
        if type(p[2]) == type({}):
            p[0]['type'] = p[2]['type']############################################################################3
        else:
            p[0]['type'] = 'VOID'
        global global_return_type ###############################################################################
        global_return_type = p[0]['type']
    elif len(p) == 3:
        p[0]['name'] = p[2]['name']
        p[0]['args'] = p[2]['args']
        if type(p[1]) == type({}):
            p[0]['type'] = p[1]['type']############################################################################3
        else:
            p[0]['type'] = 'VOID'
        global global_return_type ###############################################################################
        global_return_type = p[0]['type']
    rules_store.append(p.slice)
def p_MethodDeclarator(p):
    '''
    MethodDeclarator : IDENTIFIER L_ROUNDBR MethodCreateScope R_ROUNDBR
    | IDENTIFIER L_ROUNDBR MethodCreateScope FormalParameterList R_ROUNDBR
    '''
    p[0] = {
        'name' : p[1],
    }
    if len(p) == 6:
        p[0]['args'] = p[4]
    else:
        p[0]['args'] = []

    # stackbegin.append(p[1])
    # stackend.append(p[1])
    if len(p) == 6:
        for i in range(len(p[4])):
            parameter = p[4][i]
            if 'is_array' in parameter and parameter['is_array']:
                try:
                    size = parameter['arr_size']
                    tmp = p[4][i + size]
                    dims = []
                    for j in range(size):
                        dims.append(p[4][i + 1 + j]['place'])
                    offset_stack[-1] += ST.insert(parameter['place'],parameter['type'], arr=True, size_arr=dims)
                except:
                    raise Exception("Array passing guidelines not followed properly for arg %s" %(i))
            else:
                offset_stack[-1] += ST.insert(parameter['place'],parameter['type'])
    TAC.emit(['func', p[1], '', ''])
    for arg in p[0]['args']:
        TAC.emit(['arg', arg['place'], '', ''])
    rules_store.append(p.slice)
def p_MethodCreateScope(p):
    '''
    MethodCreateScope :
    '''
    offset_stack.append(0);
    ST.create_table(p[-2], offset_stack[-1])
    rules_store.append(p.slice)
def p_FormalParametersList(p):
    '''
    FormalParameterList : FormalParameter
    | FormalParameterList COMMA FormalParameter
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]
    rules_store.append(p.slice)
def p_FormalParameter(p):
    '''
    FormalParameter : Type VariableDeclaratorId
    '''
    p[0] = {
        'place' : p[2],
        'type' : p[1]['type']
    }
    if 'is_array' in p[1].keys() and p[1]['is_array']:
        p[0]['is_array'] = True
        p[0]['arr_size'] = p[1]['arr_size']
    rules_store.append(p.slice)
def p_Throws(p):
    '''
    Throws : THROWS ClassTypeList
    '''

    rules_store.append(p.slice)
def p_ClassTypeList(p):
    '''
    ClassTypeList : ClassType
    | ClassTypeList COMMA ClassType
    '''

    rules_store.append(p.slice)
def p_MethodBody(p):
    '''
    MethodBody : Block
    | STMT_TERMINATOR
    '''

    rules_store.append(p.slice)
def p_StaticInitializer(p):
    '''
    StaticInitializer : STATIC Block
    '''

    rules_store.append(p.slice)
def p_ConstructorDeclaration(p):
    '''
    ConstructorDeclaration : Modifiers ConstructorDeclarator Throws ConstructorBody
    | Modifiers ConstructorDeclarator ConstructorBody
    | ConstructorDeclarator Throws ConstructorBody
    | ConstructorDeclarator ConstructorBody
    '''

    rules_store.append(p.slice)
def p_ConstructorDeclarator(p):
    '''
    ConstructorDeclarator : SimpleName L_ROUNDBR FormalParameterList R_ROUNDBR
    | SimpleName L_ROUNDBR R_ROUNDBR
    '''

    rules_store.append(p.slice)
def p_ConstructorBody(p):
    '''
    ConstructorBody : L_CURLYBR ExplicitConstructorInvocation BlockStatements R_CURLYBR
    | L_CURLYBR ExplicitConstructorInvocation R_CURLYBR
    | L_CURLYBR BlockStatements R_CURLYBR
    | L_CURLYBR R_CURLYBR
    '''

    rules_store.append(p.slice)
def p_ExplicitConstructorInvocation(p):
    '''
    ExplicitConstructorInvocation : THIS L_ROUNDBR ArgumentList R_ROUNDBR STMT_TERMINATOR
    | THIS L_ROUNDBR R_ROUNDBR STMT_TERMINATOR
    | SUPER L_ROUNDBR ArgumentList R_ROUNDBR STMT_TERMINATOR
    | SUPER L_ROUNDBR R_ROUNDBR STMT_TERMINATOR
    '''
    rules_store.append(p.slice)
def p_ArrayInitializer(p):
    '''
    ArrayInitializer : L_CURLYBR VariableInitializers R_CURLYBR
    | L_CURLYBR R_CURLYBR
    '''
    #############################################################################################################################################

    rules_store.append(p.slice)
def p_VariableInitializers(p):
    '''
    VariableInitializers : VariableInitializer
    | VariableInitializers COMMA VariableInitializer
    '''
    rules_store.append(p.slice)
def p_Block(p):
    '''
    Block : L_CURLYBR R_CURLYBR
    | L_CURLYBR BlockStatements R_CURLYBR
    '''

    rules_store.append(p.slice)
def p_BlockStatements(p):
    '''
    BlockStatements : BlockStatement
    | BlockStatements BlockStatement
    '''
    rules_store.append(p.slice)
def p_BlockStatement(p):
    '''
    BlockStatement : LocalVariableDeclarationStatement
    | Statement
    '''
    p[0] = p[1]

    rules_store.append(p.slice)
def p_LocalVariableDeclarationStatement(p):
    '''
    LocalVariableDeclarationStatement : LocalVariableDeclaration STMT_TERMINATOR
    '''
    p[0] = p[1]

    rules_store.append(p.slice)
def p_LocalVariableDeclaration(p):
    '''
    LocalVariableDeclaration : Type VariableDeclarators
    '''
    for symbol in p[2]:
        if 'class_name' in symbol.keys():
            if p[1]['place'] != symbol['class_name']:
                raise Exception("Wrong class assignments")
            offset_stack[-1] += ST.insert(symbol['place'], symbol['class_name'])
            continue
        # pprint(rules_store)
        i = symbol['place']
        # pprint(p[2])
        if 'type' in symbol:
            t = symbol['type']
        else:
            t = None
        if 'is_array' not in p[1].keys():
            if t == None:
                offset_stack[-1] += ST.insert(i, p[1]['type'])
                return
            if len(i) == 2 and type(i)!= type(''):
                raise Exception("Array cannot be assigned to a primitive type")
            if len(t) == 2 and t[1] != 0 and type(i)!= type(''):
                raise Exception("Mismatch in function return: %s" %(i))
            if type(t) == type(tuple([])) and t[0] != p[1]['type']:
                raise Exception("Type mismatch: Expected %s, but got %s" %(p[1]['type'], t[0]))
            if type(t) != type(tuple([])) and t != p[1]['type']:
                raise Exception("Type mismatch: Expected %s, but got %s" %(p[1]['type'], t))
            # print(i)
            # ST.dump_TT()
            offset_stack[-1] += ST.insert(i, p[1]['type'])
            # if 'assign' in symbol.keys():
            #     TAC.emit([symbol['place'], symbol['assign'], '', '='])
        else:
            if type(i) != type(' '):
                if t == None:
                    offset_stack[-1] += ST.insert(i[0], p[1]['type'], arr=True, size_arr=i[1])
                    return
                if len(i) == 1:
                    raise Exception("Primitive types cannot be assigned to array")
                if len(i[1]) != int(p[1]['arr_size']):
                    raise Exception("Dimension mismatch for array: %s" %(i[0]))
                if type(t) != type(tuple([])) and t != p[1]['type']:
                    raise Exception("Type mismatch: Expected %s, but got %s" %(p[1]['type'], t))
                if type(t) == type(tuple([])) and t[0] != p[1]['type']:
                    raise Exception("Type mismatch: Expected %s, but got %s" %(p[1]['type'], t[0]))
                offset_stack[-1] += ST.insert(i[0], p[1]['type'], arr=True, size_arr=i[1])
            else:
                if t == None:
                    offset_stack[-1] += ST.insert(i, p[1]['type'], arr=True, size_arr=0)
                    return
                if type(t) == type(tuple([])) and t[0] != p[1]['type']:
                    raise Exception("%s and %s types are not compatible" %(t[0], p[1]['type']))
                if 'is_array' not in symbol:
                    raise Exception("Array assignment was expected: %s" %(i))
                if 'is_array' in symbol and t != p[1]['type']:
                    raise Exception("%s and %s types are not compatible" %(t, p[1]['type']))
                if 'is_array' in symbol and len(symbol['arr_size']) != p[1]['arr_size']:
                    raise Exception("Array dimensions mismatch: %s" %(i))
                offset_stack[-1] += ST.insert(i, p[1]['type'], arr=True, size_arr=0)
    for symbol in p[2]:
        if "emit_intrs" in symbol.keys():
            for X in symbol["emit_intrs"]:
                TAC.emit(X)

    rules_store.append(p.slice)
def p_Statement(p):
    '''
    Statement : StatementWithoutTrailingSubstatement
    | LabeledStatement
    | IfThenStatement
    | IfThenElseStatement
    | WhileStatement
    | ForStatement
    '''
    p[0] = p[1]

    rules_store.append(p.slice)
def p_StatementNoShortIf(p):
    '''
    StatementNoShortIf : StatementWithoutTrailingSubstatement
    | LabeledStatementNoShortIf
    | IfThenElseStatementNoShortIf
    | WhileStatementNoShortIf
    | ForStatementNoShortIf
    '''
    p[0] = p[1]


    rules_store.append(p.slice)
def p_StatementWithoutTrailingSubstatement(p):
    '''
    StatementWithoutTrailingSubstatement : Block
    | EmptyStatement
    | ExpressionStatement
    | SwitchStatement
    | DoStatement
    | BreakStatement
    | ContinueStatement
    | ReturnStatement
    | ThrowStatement
    | TryStatement
    '''
    p[0] = p[1]

    rules_store.append(p.slice)
def p_EmptyStatement(p):
    '''
    EmptyStatement : STMT_TERMINATOR
    '''

    rules_store.append(p.slice)
def p_LabeledStatement(p):
    '''
    LabeledStatement : IDENTIFIER COLON Statement
    '''

    rules_store.append(p.slice)
def p_LabeledStatementNoShortIf(p):
    '''
    LabeledStatementNoShortIf : IDENTIFIER COLON StatementNoShortIf
    '''

    rules_store.append(p.slice)
def p_ExpressionStatement(p):
    '''
    ExpressionStatement : StatementExpression STMT_TERMINATOR
    '''
    p[0] = p[1]


    rules_store.append(p.slice)
def p_StatementExpression(p):
    '''
    StatementExpression : Assignment
    | PreIncrementExpression
    | PreDecrementExpression
    | PostIncrementExpression
    | PostDecrementExpression
    | MethodInvocation
    | ClassInstanceCreationExpression
    '''
    p[0] = p[1]


    rules_store.append(p.slice)
def p_IfThenStatement(p):
    '''
    IfThenStatement : IF L_ROUNDBR Expression R_ROUNDBR IfstartSc Statement IfendSc
    '''

    rules_store.append(p.slice)
def p_IfThenElseStatement(p):
    '''
    IfThenElseStatement : IF L_ROUNDBR Expression R_ROUNDBR IfstartSc StatementNoShortIf ELSE ElseStartSc Statement ElseEndSc
    '''

    rules_store.append(p.slice)
def p_IfThenElseStatementNoShortIf(p):
    '''
    IfThenElseStatementNoShortIf : IF L_ROUNDBR Expression R_ROUNDBR IfstartSc StatementNoShortIf ELSE ElseStartSc StatementNoShortIf ElseEndSc
    '''

    rules_store.append(p.slice)
def p_IfstartSc(p):
    '''IfstartSc : '''
    labelif = ST.ident()
    labelafterif = ST.ident()
    TAC.emit(['ifgoto', [p[-2]['place'],0], 'eq', labelafterif])
    TAC.emit(['goto', labelif, '', ''])
    TAC.emit(['label', labelif, '', ''])
    ST.create_table(labelif, offset_stack[-1])
    p[0] = [labelif, labelafterif]
    rules_store.append(p.slice)
def p_IfendSc(p):
    '''IfendSc : '''
    ST.scope_terminate()
    TAC.emit(['label', p[-2][1], '', ''])
    rules_store.append(p.slice)
def p_ElseStartSc(p):
    '''ElseStartSc : '''
    ST.scope_terminate()
    labelend = ST.ident()
    TAC.emit(['goto', labelend, '', ''])
    TAC.emit(['label', p[-3][1], '', ''])
    ST.create_table(p[-3][1], offset_stack[-1])
    p[0] = [labelend]
    rules_store.append(p.slice)
def p_ElseEndSc(p):
    '''ElseEndSc : '''
    ST.scope_terminate()
    TAC.emit(['label', p[-2][0], '', ''])


    rules_store.append(p.slice)######################################################################################################3#
def p_SwitchStatement(p):
    '''
    SwitchStatement : SWITCH L_ROUNDBR Expression R_ROUNDBR SwMark2 SwitchBlock SwMark3
    '''
    if not p[3]['type'] == 'INT':
        raise Exception("Switch clause only supports Integer types")
    rules_store.append(p.slice)
#######################################################################################################33

def p_SwMark2(p):
    ''' SwMark2 : '''
    l1 = ST.ident()
    l2 = ST.ident()
    TAC.emit(['goto', l2, '', ''])
    ST.create_table(l2, offset_stack[-1])
    p[0] = [l1, l2]

def p_SwMark3(p):
    ''' SwMark3 : '''
    TAC.emit('goto', p[-2][0], '', '', ST)
    TAC.emit(['label', p[-2][1], '', ''])
    for i in range(len(p[-1]['labels'])):
        label = p[-1]['labels'][i]
        exp = p[-1]['expressions'][i]
        if exp == '':
            TAC.emit(['goto', label, '', ''])
        else:
            TAC.emit(['ifgoto', [p[-4]['place'],exp], 'eq', label])
    TAC.emit(['label', p[-2][0], '', ''])
    ST.scope_terminate()
def p_SwitchBlock(p):
    '''
    SwitchBlock : L_CURLYBR R_CURLYBR
    | L_CURLYBR SwitchBlockStatementGroups R_CURLYBR
    '''
    p[0] = p[2]
    rules_store.append(p.slice)

def p_SwitchBlockStatementGroups(p):
    '''
    SwitchBlockStatementGroups : SwitchBlockStatementGroup
    | SwitchBlockStatementGroups SwitchBlockStatementGroup
    '''
    p[0] = {
        'expressions' : [],
        'labels' : []
    }
    if len(p) == 2:
        p[0]['expressions'].append(p[1]['expression'])
        p[0]['labels'].append(p[1]['label'])
    else:
        p[0]['expressions'] = p[1]['expressions'] + [p[2]['expression']]
        p[0]['labels'] = p[1]['labels'] + [p[2]['label']]
    rules_store.append(p.slice)

def p_SwitchBlockStatementGroup(p):
    '''
    SwitchBlockStatementGroup : SwitchLabel BlockStatements
    '''
    p[0] = p[1]
    rules_store.append(p.slice)#############################################################################################################################################3
def p_SwitchLabel(p):
    '''
    SwitchLabel : SwMark1 CASE ConstantExpression COLON
    | SwMark1 DEFAULT COLON
    '''
    p[0] = {}
    if len(p) == 5:
        if not p[3]['type'] == 'INT':
            raise Exception("Only Integers allowed for case comparisions")
        p[0]['expression'] = p[3]['place']
    else:
        p[0]['expression'] = ''
    p[0]['label'] = p[1]
    rules_store.append(p.slice)

def p_SwMark1(p):
    ''' SwMark1 : '''
    l = ST.ident()
    TAC.emit(['label', l, '', ''])
    p[0] = l

def p_WhileStatement(p):
    '''
    WhileStatement : WHILE WhMark1 L_ROUNDBR Expression R_ROUNDBR WhMark2 Statement WhMark3
    '''
    rules_store.append(p.slice)

def p_WhileStatementNoShortIf(p):
    '''
    WhileStatementNoShortIf : WHILE WhMark1 L_ROUNDBR Expression R_ROUNDBR WhMark2 StatementNoShortIf WhMark3
    '''
    rules_store.append(p.slice)

def p_WhMark1(p):
    '''WhMark1 : '''
    l1 = ST.ident()
    l2 = ST.ident()
    l3 = ST.ident()
    ST.create_table(l1, offset_stack[-1])
    TAC.emit(['label',l1,'',''])
    p[0]=[l1,l2,l3]

def p_WhMark2(p):
    '''WhMark2 : '''
    TAC.emit(['ifgoto',[p[-2]['place'],0],'eq', p[-4][2]])
    TAC.emit(['goto',p[-4][1],'',''])
    TAC.emit(['label',p[-4][1],'',''])

def p_WhMark3(p):
    '''WhMark3 : '''
    TAC.emit(['goto',p[-6][0],'',''])
    TAC.emit(['label',p[-6][2],'',''])
    ST.scope_terminate()

def p_DoStatement(p):
    '''
    DoStatement : DO doWhMark1 Statement WHILE doWhMark2 L_ROUNDBR Expression R_ROUNDBR doWhMark3 STMT_TERMINATOR
    '''
    rules_store.append(p.slice)

def p_doWhMark1(p):
    '''doWhMark1 : '''
    l1 = ST.ident()
    l2 = ST.ident()
    l3 = ST.ident()
    ST.create_table(l1, offset_stack[-1])
    TAC.emit(['label',l1,'',''])
    p[0]=[l1,l2,l3]

def p_doWhMark3(p):
    '''doWhMark3 : '''
    TAC.emit(['ifgoto',[p[-2]['place'],0],'eq', p[-7][2]])
    TAC.emit(['goto',p[-7][1],'',''])
    TAC.emit(['label',p[-7][2],'',''])

def p_doWhMark2(p):
    '''doWhMark2 : '''
    #TAC.emit('goto',p[-3][1],'','')
    TAC.emit(['label',p[-3][1],'',''])
    ST.scope_terminate()

def p_ForStatement(p):
    '''
    ForStatement : FOR FoMark0 L_ROUNDBR ForInit STMT_TERMINATOR FoMark1 ForExpression FoMark6 ForUpdate R_ROUNDBR FoMark2 Statement FoMark3
    | FOR FoMark0 L_ROUNDBR STMT_TERMINATOR FoMark1 ForExpression FoMark6 ForUpdate R_ROUNDBR FoMark2 Statement FoMark3
    | FOR FoMark0 L_ROUNDBR ForInit STMT_TERMINATOR FoMark1 ForExpression R_ROUNDBR FoMark4 Statement FoMark5
    | FOR FoMark0 L_ROUNDBR STMT_TERMINATOR FoMark1 ForExpression R_ROUNDBR FoMark4 Statement FoMark5
    '''
    rules_store.append(p.slice)

def p_ForStatementNoShortIf(p):
    '''
    ForStatementNoShortIf : FOR FoMark0 L_ROUNDBR ForInit STMT_TERMINATOR FoMark1 ForExpression FoMark6 ForUpdate R_ROUNDBR FoMark2 StatementNoShortIf FoMark3
    | FOR FoMark0 L_ROUNDBR STMT_TERMINATOR FoMark1 ForExpression FoMark6 ForUpdate R_ROUNDBR FoMark2 StatementNoShortIf FoMark3
    | FOR FoMark0 L_ROUNDBR ForInit STMT_TERMINATOR FoMark1 ForExpression R_ROUNDBR FoMark4 StatementNoShortIf FoMark5
    | FOR FoMark0 L_ROUNDBR STMT_TERMINATOR FoMark1 ForExpression R_ROUNDBR FoMark4 StatementNoShortIf FoMark5
    '''
    rules_store.append(p.slice)

def p_ForExpression(p):
    '''
    ForExpression : Expression STMT_TERMINATOR
    | STMT_TERMINATOR
    '''
    if len(p)==3:
        p[0]=p[1]

def p_FoMark0(p):
    '''FoMark0 : '''
    l0 = ST.ident()
    ST.create_table(l0, offset_stack[-1])

def p_FoMark1(p):
    '''FoMark1 : '''
    l1 = ST.ident()
    l2 = ST.ident()
    l3 = ST.ident()
    l4 = ST.ident()
    TAC.emit(['label',l1,'',''])
    p[0]=[l1,l2,l3,l4]

def p_FoMark2(p):
    '''FoMark2 : '''
    TAC.emit(['goto',p[-5][0],'',''])
    TAC.emit(['label',p[-5][1],'',''])
    TAC.emit(['ifgoto',[p[-4]['place'],0],'eq', p[-5][3]])

def p_FoMark6(p):
    '''FoMark6 : '''
    TAC.emit(['goto', p[-2][1],'',''])
    TAC.emit(['label',p[-2][2],'',''])

def p_FoMark4(p):
    '''FoMark4 : '''
    TAC.emit(['ifgoto',[p[-2]['place'],0],'eq', p[-3][2]])
    TAC.emit(['goto',p[-3][1],'',''])
    TAC.emit(['label',p[-3][1],'',''])

def p_FoMark3(p):
    '''FoMark3 : '''
    TAC.emit(['goto',p[-7][2],'',''])
    TAC.emit(['label',p[-7][3],'',''])
    ST.scope_terminate()

def p_FoMark5(p):
    '''FoMark5 : '''
    TAC.emit(['goto',p[-5][0],'',''])
    TAC.emit(['label',p[-5][2],'',''])
    ST.scope_terminate()

def p_ForInit(p):
    '''
    ForInit : StatementExpressionList
    | LocalVariableDeclaration
    '''

    rules_store.append(p.slice)
def p_ForUpdate(p):
    '''
    ForUpdate : StatementExpressionList
    '''

    rules_store.append(p.slice)
def p_StatementExpressionList(p):
    '''
    StatementExpressionList : StatementExpression
    | StatementExpressionList COMMA StatementExpression
    '''

    rules_store.append(p.slice)
def p_BreakStatement(p):
    '''
    BreakStatement : BREAK IDENTIFIER STMT_TERMINATOR
    | BREAK STMT_TERMINATOR
    '''
    if(len(p)==3 and p[1]=='break'):
        TAC.emit(['goto', stackend[-1], '', ''])
    rules_store.append(p.slice)

def p_ContinueStatement(p):
    '''
    ContinueStatement : CONTINUE IDENTIFIER STMT_TERMINATOR
    | CONTINUE STMT_TERMINATOR
    '''
    if(len(p)==3 and p[1]=='continue'):
        TAC.emit(['goto', stackbegin[-1], '', ''])
#########################################################################################################################################3

    rules_store.append(p.slice)
def p_ReturnStatement(p):
    '''
    ReturnStatement : RETURN Expression STMT_TERMINATOR
    | RETURN STMT_TERMINATOR
    '''
    if len(p)==3 :
        if global_return_type=='VOID':
            TAC.emit(['ret', '', global_method, ''])
        else :
            raise Exception("Expected return type %s" %(global_return_type))
    else:

        to_return = global_return_type
        curr_returned = ST.find(p[2]['place'])
        # print(to_return)
        # print(curr_returned['type'])
        if curr_returned != None:
            if to_return != curr_returned['type']:
                raise Exception("Wrong return type in %s" %(ST.cur_sc))
            if 'is_array' in curr_returned.keys() and len(curr_returned['arr_size']) != to_return[1]:
                raise Exception("Dimension mismatch in return statement in %s" %(ST.curr_scope))
        else:
            if p[2]['type'] != to_return :
                raise Exception("Wrong return type in %s" %(ST.cur_sc))
        TAC.emit(['ret', p[2]['place'], global_method, ''])

    rules_store.append(p.slice)
def p_ThrowStatement(p):
    '''
    ThrowStatement : THROW Expression STMT_TERMINATOR
    '''
    rules_store.append(p.slice)
def p_TryStatement(p):
    '''
    TryStatement : TRY Block Catches
    | TRY Block Catches Finally
    | TRY Block Finally
    '''
    rules_store.append(p.slice)
def p_Catches(p):
    '''
    Catches : CatchClause
    | Catches CatchClause
    '''
    rules_store.append(p.slice)
def p_CatchClause(p):
    '''
    CatchClause : CATCH L_ROUNDBR FormalParameter R_ROUNDBR Block
    '''
    rules_store.append(p.slice)
def p_Finally(p):
    '''
    Finally : FINALLY Block
    '''
    rules_store.append(p.slice)
def p_Primary(p):
    '''
    Primary : PrimaryNoNewArray
    | ArrayCreationExpression
    '''
    p[0] = p[1]
    rules_store.append(p.slice)
def p_PrimaryNoNewArray(p):
    '''
    PrimaryNoNewArray : Literal
    | THIS
    | L_ROUNDBR Expression R_ROUNDBR
    | ClassInstanceCreationExpression
    | FieldAccess
    | MethodInvocation
    | ArrayAccess
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]
    rules_store.append(p.slice)
def p_ClassInstanceCreationExpression(p):
    '''
    ClassInstanceCreationExpression : NEW ClassType L_ROUNDBR R_ROUNDBR
    | NEW ClassType L_ROUNDBR ArgumentList R_ROUNDBR
    '''

    rules_store.append(p.slice)
def p_ArgumentList(p):
    '''
    ArgumentList : Expression
    | ArgumentList COMMA Expression
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

    rules_store.append(p.slice)
def p_ArrayCreationExpression(p):
    '''
    ArrayCreationExpression : NEW PrimitiveType DimExprs Dims
    | NEW PrimitiveType DimExprs
    | NEW ClassType DimExprs Dims
    | NEW ClassType DimExprs
    '''
    if len(p) == 4:
        p[0] = {
            'type' : p[2]['type'],
            'arr_size' : p[3],
            'is_array' : True,
        }
    # pprint(p[0])
    rules_store.append(p.slice)
def p_DimExprs(p):
    '''
    DimExprs : DimExpr
    | DimExprs DimExpr
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]
    rules_store.append(p.slice)
def p_DimExpr(p):
    '''
    DimExpr : L_SQBR Expression R_SQBR
    '''
    if p[2]['type'] == 'INT':
        p[0] = p[2]['place']
    else:
        raise Exception("Array declaration requires a size as integer : " + p[2]['place'])
    # pprint(p[0])
    rules_store.append(p.slice)
def p_Dims(p):
    '''
    Dims : L_SQBR R_SQBR
    | Dims L_SQBR R_SQBR
    '''
    if len(p) == 3:
        p[0] = 1
    else:
        p[0] = 1 + p[1]
    rules_store.append(p.slice)
def p_FieldAccess(p):
    '''
    FieldAccess : Primary DOT IDENTIFIER
    | SUPER DOT IDENTIFIER
    '''

    rules_store.append(p.slice)
def p_MethodInvocation(p):
    '''
    MethodInvocation : Name L_ROUNDBR ArgumentList R_ROUNDBR
    | Name L_ROUNDBR R_ROUNDBR
    | Primary DOT IDENTIFIER L_ROUNDBR ArgumentList R_ROUNDBR
    | Primary DOT IDENTIFIER L_ROUNDBR R_ROUNDBR
    | SUPER DOT IDENTIFIER L_ROUNDBR ArgumentList R_ROUNDBR
    | SUPER DOT IDENTIFIER L_ROUNDBR R_ROUNDBR
    '''
    if p[2] == '(' and flag_mr:
        attributes = ST.find(p[1]['place'], func=True)
        if attributes == None and p[1]['place'] != "System.out.println" and p[1]['place'] != "System.in.scanln":
            raise Exception("Undeclared function used: %s" %(p[1]['place']))

        if p[1]['place'] == 'System.out.println':
            if len(p) == 5:
                for parameter in p[3]:
                    if 'type' in parameter.keys():
                        TAC.emit(['print',parameter['place'],'','_' + parameter['type']])
                    else:
                        TAC.emit(['print',parameter['place'],'','_INT'])
        elif p[1]['place'] == 'System.in.scanln':
            if len(p) == 5:
                for parameter in p[3]:
                    if 'type' in parameter.keys():
                        TAC.emit(['scan',parameter['place'],'','_' + parameter['type']])
                    else:
                        TAC.emit(['scan',parameter['place'],'','_INT'])
        else:
            temp_var = ST.temp_var()
            if len(p) == 5:
                prototype = attributes['params']
                if len(prototype) != len(p[3]):
                    raise Exception("Wrong number of arguments to function call: %s" %(p[1]['place']))
                if 'this' in p[1].keys():
                    TAC.emit(['param', p[1]['this'], '', ''])
                p[3].reverse()
                for i in range(len(p[3])):
                    parameter = p[3][i]
                    proto = prototype[i]
                    if parameter['type'] != proto['type']:
                        raise Exception("Wrong type of arg passed to function %s; got %s but expected %s" %(p[1]['place'], parameter['type'], proto['type']))
                    TAC.emit(['param',parameter['place'],'',''])
            elif 'this' in p[1].keys():
                TAC.emit(['param', p[1]['this'], '', ''])

            offset_stack[-1] += ST.insert(temp_var,attributes['type'],temp=True)
            if attributes['type'] == 'VOID':
                TAC.emit(['call',p[1]['place'],'',''])
            else:
                TAC.emit(['call',p[1]['place'],temp_var,''])
            TAC.emit(['adjust_rsp',attributes['number_params']*4,'',''])
            p[0] = {
                'place' : temp_var,
                'ret_type' : attributes['type']
            }
    elif p[2] == '(':
        if p[1]['place'] == 'System.out.println':
            if len(p) == 5:
                for parameter in p[3]:
                    if 'type' in parameter.keys():
                        TAC.emit(['print',parameter['place'],'','_' + parameter['type']])
                    else:
                        TAC.emit(['print',parameter['place'],'','_INT'])
        elif p[1]['place'] == 'System.in.scanln':
            if len(p) == 5:
                for parameter in p[3]:
                    if 'type' in parameter.keys():
                        TAC.emit(['scan',parameter['place'],'','_' + parameter['type']])
                    else:
                        TAC.emit(['scan',parameter['place'],'','_INT'])
        else:
            temp_var = ST.temp_var()
            if len(p) == 5:
                p[3].reverse()
                for i in range(len(p[3])):
                    parameter = p[3][i]
                    proto = prototype[i]
                    TAC.emit(['param',parameter['place'],'',''])

            offset_stack[-1] += ST.insert(temp_var,'INT',temp=True)
            TAC.emit(['call',p[1]['place'],temp_var,''])
            TAC.emit(['adjust_rsp',len(p[3])*4,'',''])
            p[0] = {
                'place' : temp_var,
                'ret_type' : 'INT'
            }


    rules_store.append(p.slice)
def p_ArrayAccess(p):
    '''
    ArrayAccess : Name DimExprs
    '''
    p[0] = {}
    attributes = ST.find(p[1]['place'])
    # pprint(p[1])
    # pprint(attributes)
    if attributes == None:
        raise Exception("Undeclared Symbol Used: %s" %(p[1]['place']))
    if not 'arr' in attributes or not attributes['arr']:
        raise Exception("Only array type can be indexed : %s" %(p[1]['place']))

    indexes = p[2]
    if not len(indexes) == len(attributes['size_arr']):
        raise Exception("Not a valid indexing for array %s" %(p[1]['place']))

    arr_size = attributes['size_arr']
    address_indices = p[2]
    t2 = ST.temp_var()
    offset_stack[-1] += ST.insert(t2,attributes['type'],temp=True)
    TAC.emit([t2, address_indices[0], '', '='])
    for i in range(1, len(address_indices)):
        TAC.emit([t2, t2, arr_size[i], '*'])
        TAC.emit([t2, t2, address_indices[i], '+'])
    index = t2

    src = p[1]['place'] + '[' + str(index) + ']'
    t1 = ST.temp_var()
    offset_stack[-1] += ST.insert(t1,attributes['type'],temp=True)
    TAC.emit([t1, p[1]['place'], str(index), '=arr'])
    p[0]['type'] = attributes['type']
    p[0]['place'] = t1
    p[0]['access_type'] = 'array'
    p[0]['name'] = p[1]['place']
    p[0]['index'] = str(index)
    rules_store.append(p.slice)
def p_PostfixExpression(p):
    '''
    PostfixExpression : Primary
    | Name
    | PostIncrementExpression
    | PostDecrementExpression
    '''
    if 'fields' in p[1].keys():
        p[0] = p[1]
        return
    p[0] = {}
    if 'idVal' in p[1].keys():
        p[0]['place'] = p[1]['idVal']
        p[0]['type'] = p[1]['type']
        p[0]['is_var'] = False

    elif 'place' in p[1].keys() and 'is_var' in p[1].keys() and p[1]['is_var']:
        attributes = ST.find(p[1]['place'])
        if attributes == None:
            raise Exception("Undeclared Variable Used: %s" %(p[1]['place']))
        else:
            p[0]['type'] = attributes['type']
            p[0]['place'] = p[1]['place']

    elif 'place' in p[1].keys():
        p[0] = p[1]
    elif 'name' in p[1].keys() and p[1]['name'].find('_obj_') != -1:
        p[0]['type'] = p[1]['type']
        p[0]['place'] = ST.get_temp_var()
        p[0]['access_type'] = 'array'
        p[0]['name'] = p[1]['name']
        p[0]['index'] = p[1]['index']

        TAC.emit(p[0]['place'], p[0]['name'],p[0]['index'] , '=arr')

    elif 'is_array' in p[1].keys():
        p[0]['place'] = p[1]['arr_size']
        p[0]['type'] = p[1]['type']
        p[0]['is_array'] = True

    rules_store.append(p.slice)
def p_PostIncrementExpression(p):
    '''
    PostIncrementExpression : PostfixExpression INCREMENT
    '''
    if p[1]['type'] == 'INT':
        TAC.emit([p[1]['place'], p[1]['place'], '1', '+'])
        p[0] = {
            'place' : p[1]['place'],
            'type' : 'INT'
        }
    else:
        raise Exception("Error: increment operator can be used with integers only")
    rules_store.append(p.slice)
def p_PostDecrementExpression(p):
    '''
    PostDecrementExpression : PostfixExpression DECREMENT
    '''
    if p[1]['type'] == 'INT':
        TAC.emit([p[1]['place'], p[1]['place'], '1', '-'])
        p[0] = {
            'place' : p[1]['place'],
            'type' : 'INT'
        }
    else:
        raise Exception("Error: decrement operator can be used with integers only")

    rules_store.append(p.slice)
def p_UnaryExpression(p):
    '''
    UnaryExpression : PreIncrementExpression
    | PreDecrementExpression
    | PLUS UnaryExpression
    | MINUS UnaryExpression
    | UnaryExpressionNotPlusMinus
    '''
    if len(p) == 2:
        p[0] = p[1]
        return
    elif p[1] == '-':
        p[0] = p[2]
        p[0]['place'] = '-' + p[2]['place']

    rules_store.append(p.slice)
def p_PreIncrementExpression(p):
    '''
    PreIncrementExpression : INCREMENT UnaryExpression
    '''
    if(p[2]['type'] == 'INT'):
        TAC.emit([p[2]['place'],p[2]['place'],'1','+'])
        p[0] = {
            'place' : p[2]['place'],
            'type' : 'INT'
        }
    else:
        raise Exception("Error: increment operator can be used with integers only")
    rules_store.append(p.slice)
def p_PreDecrementExpression(p):
    '''
    PreDecrementExpression : DECREMENT UnaryExpression
    '''
    if(p[2]['type']=='INT'):
        TAC.emit([p[2]['place'],p[2]['place'],'1','-'])
        p[0] = {
            'place' : p[2]['place'],
            'type' : 'INT'
        }
    else:
        raise Exception("Error: decrement operator can be used with integers only")

    rules_store.append(p.slice)
def p_UnaryExpressionNotPlusMinus(p):
    '''
    UnaryExpressionNotPlusMinus : PostfixExpression
    | BITWISE_NOT UnaryExpression
    | LOGICAL_NOT UnaryExpression
    | CastExpression
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        t = ST.temp_var()
        offset_stack[-1] += ST.insert(t,p[2]['type'],temp=True)
        TAC.emit([t, p[2]['place'], '', p[1]])
        p[0] = p[2]
        p[0]['place'] = t

    rules_store.append(p.slice)
def p_CastExpression(p):
    '''
    CastExpression : L_ROUNDBR PrimitiveType Dims R_ROUNDBR UnaryExpression
    | L_ROUNDBR PrimitiveType R_ROUNDBR UnaryExpression
    | L_ROUNDBR Expression R_ROUNDBR UnaryExpressionNotPlusMinus
    | L_ROUNDBR Name Dims R_ROUNDBR UnaryExpressionNotPlusMinus
    '''

    rules_store.append(p.slice)
def p_MultiplicativeExpression(p):
    '''
    MultiplicativeExpression : UnaryExpression
    | MultiplicativeExpression MULT UnaryExpression
    | MultiplicativeExpression DIVIDE UnaryExpression
    | MultiplicativeExpression MODULO UnaryExpression
    '''
    if(len(p)==2):
        p[0] = p[1]
        return
    newPlace = ST.temp_var()
    p[0] = {
        'place' : newPlace,
    }
    # pprint(p[1])
    # pprint(p[3])
    if 'ret_type' in p[1].keys():
        type1 = p[1]['ret_type']
    else:
        type1 = p[1]['type']

    if 'ret_type' in p[3].keys():
        type2 = p[3]['ret_type']
    else:
        type2 = p[3]['type']
    if p[2] == '*':
        if type1 == "INT" and type2 == "INT":
            p[0]['type'] = 'INT'
            offset_stack[-1] += ST.insert(newPlace,p[0]['type'],temp=True)
            TAC.emit([newPlace,p[1]['place'], p[3]['place'], p[2]])
        else:
            raise Exception('Error: Type is not compatible'+p[1]['place']+','+p[3]['place']+'.')
    elif p[2] == '/' :
        if type1 == "INT" and type2 == "INT":
            p[0]['type'] = 'INT'
            offset_stack[-1] += ST.insert(newPlace,p[0]['type'],temp=True)
            TAC.emit([newPlace, p[1]['place'], p[3]['place'], p[2]])
        else:
            raise Exception('Error: Type is not compatible' + p[1]['place'] + ',' + p[3]['place'] + '.')
    elif p[2] == '%':
        if type1 == "INT" and type2 == "INT":
            p[0]['type'] = 'INT'
            offset_stack[-1] += ST.insert(newPlace,p[0]['type'],temp=True)
            TAC.emit([newPlace,p[1]['place'],p[3]['place'],p[2]])
        else:
            raise Exception('Error: Type is not compatible' + p[1]['place'] + ',' + p[3]['place'] + '.')
    rules_store.append(p.slice)
def p_AdditiveExpression(p):
    '''
    AdditiveExpression : MultiplicativeExpression
    | AdditiveExpression PLUS MultiplicativeExpression
    | AdditiveExpression MINUS MultiplicativeExpression
    '''
    if len(p) == 2:
        p[0] = p[1]
        return
    newPlace = ST.temp_var()
    p[0] = {
        'place' : newPlace,
    }
    if 'ret_type' in p[1].keys():
        type1 = p[1]['ret_type'][0]
        if p[1]['ret_type'][1] != 0:
            raise Exception("Error")
    else:
        type1 = p[1]['type']

    if 'ret_type' in p[3].keys():
        type2 = p[3]['ret_type'][0]
        if p[3]['ret_type'][1] != 0:
            raise Exception("Error")
    else:
        type2 = p[3]['type']

    if type1 == "INT" and type2 == "INT":
        p[0]['type'] = 'INT'
        offset_stack[-1] += ST.insert(newPlace,p[0]['type'],temp=True)
        TAC.emit([newPlace, p[1]['place'], p[3]['place'], p[2]])
    elif type1 == "CHAR" and type2 == "INT":
        p[0]['type'] = 'CHAR'
        offset_stack[-1] += ST.insert(newPlace,p[0]['type'],temp=True)
        TAC.emit([newPlace, p[1]['place'], p[3]['place'], p[2]])
    elif type1 == "INT" and type2 == "CHAR":
        p[0]['type'] = 'CHAR'
        offset_stack[-1] += ST.insert(newPlace,p[0]['type'],temp=True)
        TAC.emit([newPlace, p[1]['place'], p[3]['place'], p[2]])
    elif type1 == "CHAR" and type2 == "CHAR":
        p[0]['type'] = 'CHAR'
        offset_stack[-1] += ST.insert(newPlace,p[0]['type'],temp=True)
        TAC.emit([newPlace, p[1]['place'], p[3]['place'], p[2]])
    else:
        raise Exception("Error: integer value is needed")
    rules_store.append(p.slice)

def p_ShiftExpression(p):
    '''
    ShiftExpression : AdditiveExpression
    | ShiftExpression L_SHIFT AdditiveExpression
    | ShiftExpression R_SHIFT AdditiveExpression
    | ShiftExpression RR_SHIFT AdditiveExpression
    '''
    if len(p) == 2:
        p[0] = p[1]
        return

    newPlace = ST.temp_var()
    p[0] = {
        'place' : newPlace,
    }
    if 'ret_type' in p[1].keys():
        type1 = p[1]['ret_type'][0]
        if p[1]['ret_type'][1] != 0:
            raise Exception("Error")
    else:
        type1 = p[1]['type']

    if 'ret_type' in p[3].keys():
        type2 = p[3]['ret_type'][0]
        if p[3]['ret_type'][1] != 0:
            raise Exception("Error")
    else:
        type2 = p[3]['type']

    if type1 == "INT" and type2 == "INT":
        p[0]['type'] = 'INT'
        offset_stack[-1] += ST.insert(newPlace,p[0]['type'],temp=True)
        TAC.emit([newPlace, p[1]['place'], p[3]['place'], p[2]])
    else:
        raise Exception("Error: integer value is needed")

    rules_store.append(p.slice)
def p_RelationalExpression(p):
    '''
    RelationalExpression : ShiftExpression
    | RelationalExpression LST ShiftExpression
    | RelationalExpression GRT ShiftExpression
    | RelationalExpression LEQ ShiftExpression
    | RelationalExpression GEQ ShiftExpression
    | RelationalExpression INSTANCEOF ReferenceType
    '''
    if len(p) == 2:
        p[0] = p[1]
        return
    l1 = ST.ident()
    l2 = ST.ident()
    l3 = ST.ident()
    newPlace = ST.temp_var()
    p[0] = {
        'place' : newPlace,
    }
    if 'ret_type' in p[1].keys():
        type1 = p[1]['ret_type'][0]
        if p[1]['ret_type'][1] != 0:
            raise Exception("Error")
    else:
        type1 = p[1]['type']

    if 'ret_type' in p[3].keys():
        type2 = p[3]['ret_type'][0]
        if p[3]['ret_type'][1] != 0:
            raise Exception("Error")
    else:
        type2 = p[3]['type']

    if type1 == "INT" and type2 == "INT":
        if p[2]=='>':
            p[0]['type'] = 'INT'
            offset_stack[-1] += ST.insert(newPlace,p[0]['type'],temp=True)
            TAC.emit(['ifgoto', [p[1]['place'], p[3]['place']], 'gt', l2])
            TAC.emit(['label', l1, '', ''])
            TAC.emit([newPlace, '0', '', '='])
            TAC.emit(['goto', l3, '', ''])
            TAC.emit(['label', l2, '', ''])
            TAC.emit([newPlace, '1', '', '='])
            TAC.emit(['label', l3, '', ''])
        elif p[2]=='>=':
            p[0]['type'] = 'INT'
            offset_stack[-1] += ST.insert(newPlace,p[0]['type'],temp=True)
            TAC.emit(['ifgoto', [p[1]['place'],p[3]['place']], 'geq', l2])
            TAC.emit(['label', l1, '', ''])
            TAC.emit([newPlace, '0', '', '='])
            TAC.emit(['goto', l3, '', ''])
            TAC.emit(['label', l2, '', ''])
            TAC.emit([newPlace, '1', '', '='])
            TAC.emit(['label', l3, '', ''])
        elif p[2]=='<':
            p[0]['type'] = 'INT'
            offset_stack[-1] += ST.insert(newPlace,p[0]['type'],temp=True)
            TAC.emit(['ifgoto', [p[1]['place'], p[3]['place']], 'lt', l2])
            TAC.emit(['label', l1, '', ''])
            TAC.emit([newPlace, '0', '', '='])
            TAC.emit(['goto', l3, '', ''])
            TAC.emit(['label', l2, '', ''])
            TAC.emit([newPlace, '1', '', '='])
            TAC.emit(['label', l3, '', ''])
        elif p[2]=='<=':
            p[0]['type'] = 'INT'
            offset_stack[-1] += ST.insert(newPlace,p[0]['type'],temp=True)
            TAC.emit(['ifgoto', [p[1]['place'],p[3]['place']], 'leq', l2])
            TAC.emit(['label', l1, '', ''])
            TAC.emit([newPlace, '0', '', '='])
            TAC.emit(['goto', l3, '', ''])
            TAC.emit(['label', l2, '', ''])
            TAC.emit([newPlace, '1', '', '='])
            TAC.emit(['label', l3, '', ''])
    else:
        raise Exception('Error: Type is not compatible' + p[1]['place'] + ',' + p[3]['place'] + '.')


    rules_store.append(p.slice)
def p_EqualityExpression(p):
    '''
    EqualityExpression : RelationalExpression
    | EqualityExpression EQUALS RelationalExpression
    | EqualityExpression NOT_EQUAL RelationalExpression
    '''
    if(len(p)==2):
        p[0] = p[1]
        return
    l1 = ST.ident()
    l2 = ST.ident()
    l3 = ST.ident()
    newPlace = ST.temp_var()
    p[0]={
        'place' : newPlace,
    }
    if 'ret_type' in p[1].keys():
        type1 = p[1]['ret_type'][0]
        if p[1]['ret_type'][1] != 0:
            raise Exception("Error")
    else:
        type1 = p[1]['type']

    if 'ret_type' in p[3].keys():
        type2 = p[3]['ret_type'][0]
        if p[3]['ret_type'][1] != 0:
            raise Exception("Error")
    else:
        type2 = p[3]['type']
    if type1 == "INT" and type2 == "INT":
        if(p[2][0]=='='):
            p[0]['type'] = 'INT'
            offset_stack[-1] += ST.insert(newPlace,p[0]['type'],temp=True)
            TAC.emit(['ifgoto', [p[1]['place'],p[3]['place']], 'eq' , l2])
            TAC.emit(['label', l1, '', ''])
            TAC.emit([newPlace, '0', '', '='])
            TAC.emit(['goto', l3, '', ''])
            TAC.emit(['label', l2, '', ''])
            TAC.emit([newPlace, '1', '', '='])
            TAC.emit(['label', l3, '', ''])
        else:
            p[0]['type'] = 'INT'
            ST.insert(newPlace,p[0]['type'],temp=True)
            TAC.emit(['ifgoto', [p[1]['place'],p[3]['place']], 'neq', l2])
            TAC.emit(['label', l1, '', ''])
            TAC.emit([newPlace, '0', '', '='])
            TAC.emit(['goto', l3, '', ''])
            TAC.emit(['label', l2, '', ''])
            TAC.emit([newPlace, '1', '', '='])
            TAC.emit(['label', l3, '', ''])
    else:
        raise Exception('Only INT type comparisions supported: ' + p[1]['place'] + ' and' + p[3]['place'])


    rules_store.append(p.slice)
def p_AndExpression(p):
    '''
    AndExpression : EqualityExpression
    | AndExpression BITWISE_AND EqualityExpression
    '''
    if(len(p)==2):
        p[0] = p[1]
        return
    newPlace = ST.temp_var()
    p[0] = {
        'place' : newPlace,
    }
    if 'ret_type' in p[1].keys():
        type1 = p[1]['ret_type'][0]
        if p[1]['ret_type'][1] != 0:
            raise Exception("Error")
    else:
        type1 = p[1]['type']

    if 'ret_type' in p[3].keys():
        type2 = p[3]['ret_type'][0]
        if p[3]['ret_type'][1] != 0:
            raise Exception("Error")
    else:
        type2 = p[3]['type']
    if type1 == "INT" and type2 == "INT":
        p[0]['type'] = 'INT'
        offset_stack[-1] += ST.insert(newPlace,p[0]['type'],temp=True)
        TAC.emit([newPlace,p[1]['place'],p[3]['place'],'&'])
    else:
        raise Exception('Error: Type is not compatible' + p[1]['place'] + ',' + p[3]['place'] + '.')
    rules_store.append(p.slice)
def p_ExclusiveOrExpression(p):
    '''
    ExclusiveOrExpression : AndExpression
    | ExclusiveOrExpression BITWISE_XOR AndExpression
    '''
    if(len(p)==2):
        p[0] = p[1]
        return
    newPlace = ST.temp_var()
    p[0] = {
        'place' : newPlace,
    }
    if 'ret_type' in p[1].keys():
        type1 = p[1]['ret_type'][0]
        if p[1]['ret_type'][1] != 0:
            raise Exception("Error")
    else:
        type1 = p[1]['type']

    if 'ret_type' in p[3].keys():
        type2 = p[3]['ret_type'][0]
        if p[3]['ret_type'][1] != 0:
            raise Exception("Error")
    else:
        type2 = p[3]['type']
    if type1 == "INT" and type2 == "INT":
        p[0]['type'] = 'INT'
        offset_stack[-1] += ST.insert(newPlace,p[0]['type'],temp=True)
        TAC.emit([newPlace,p[1]['place'],p[3]['place'],'^'])
    else:
        raise Exception('Error: Type is not compatible' + p[1]['place'] + ',' + p[3]['place'] + '.')

    rules_store.append(p.slice)
def p_InclusiveOrExpression(p):
    '''
    InclusiveOrExpression : ExclusiveOrExpression
    | InclusiveOrExpression BITWISE_OR ExclusiveOrExpression
    '''
    if(len(p)==2):
        p[0] = p[1]
        return
    newPlace = ST.temp_var()
    p[0] = {
        'place' : newPlace,
    }
    if 'ret_type' in p[1].keys():
        type1 = p[1]['ret_type'][0]
        if p[1]['ret_type'][1] != 0:
            raise Exception("Error")
    else:
        type1 = p[1]['type']

    if 'ret_type' in p[3].keys():
        type2 = p[3]['ret_type'][0]
        if p[3]['ret_type'][1] != 0:
            raise Exception("Error")
    else:
        type2 = p[3]['type']
    if type1 == "INT" and type2 == "INT":
        p[0]['type'] = 'INT'
        offset_stack[-1] += ST.insert(newPlace,p[0]['type'],temp=True)
        TAC.emit([newPlace, p[1]['place'], p[3]['place'], '|'])
    else:
        raise Exception('Error: Type is not compatible' + p[1]['place'] + ',' + p[3]['place'] + '.')
    rules_store.append(p.slice)
    rules_store.append(p.slice)
def p_ConditionalAndExpression(p):
    '''
    ConditionalAndExpression : InclusiveOrExpression
    | ConditionalAndExpression LOGICAL_AND InclusiveOrExpression
    '''
    if(len(p)==2):
        p[0] = p[1]
        return
    newPlace = ST.temp_var()
    p[0] = {
        'place' : newPlace,
    }
    if 'ret_type' in p[1].keys():
        type1 = p[1]['ret_type'][0]
        if p[1]['ret_type'][1] != 0:
            raise Exception("Error")
    else:
        type1 = p[1]['type']

    if 'ret_type' in p[3].keys():
        type2 = p[3]['ret_type'][0]
        if p[3]['ret_type'][1] != 0:
            raise Exception("Error")
    else:
        type2 = p[3]['type']
    if type1 == "INT" and type2 == "INT":
        l1 = ST.ident()
        p[0]['type'] = 'INT'
        offset_stack[-1] += ST.insert(newPlace,p[0]['type'],temp=True)
        TAC.emit([newPlace,p[1]['place'],'','='])
        TAC.emit(['ifgoto',[p[1]['place'],0],'eq',l1])
        TAC.emit([newPlace, p[1]['place'], p[3]['place'], '&'])
        TAC.emit(['label',l1,'',''])
    else:
        raise Exception('Error: Type is not compatible' + p[1]['place'] + ',' + p[3]['place'] + '.')
    rules_store.append(p.slice)
def p_ConditionalOrExpression(p):
    '''
    ConditionalOrExpression : ConditionalAndExpression
    | ConditionalOrExpression LOGICAL_OR ConditionalAndExpression
    '''
    if(len(p)==2):
        p[0] = p[1]
        return
    newPlace = ST.temp_var()
    p[0] = {
        'place' : newPlace,
    }
    if 'ret_type' in p[1].keys():
        type1 = p[1]['ret_type'][0]
        if p[1]['ret_type'][1] != 0:
            raise Exception("Error")
    else:
        type1 = p[1]['type']

    if 'ret_type' in p[3].keys():
        type2 = p[3]['ret_type'][0]
        if p[3]['ret_type'][1] != 0:
            raise Exception("Error")
    else:
        type2 = p[3]['type']
    if type1 == "INT" and type2 == "INT":
        l1 = ST.ident()
        p[0]['type'] = 'INT'
        ST.insert(newPlace,p[0]['type'],temp=True)
        TAC.emit([newPlace,p[1]['place'],'','='])
        TAC.emit(['ifgoto',[p[1]['place'],1],'eq',l1])
        TAC.emit([newPlace, p[1]['place'], p[3]['place'], '|'])
        TAC.emit(['label',l1,'',''])
    else:
        raise Exception('Error: Type is not compatible' + p[1]['place'] + ',' + p[3]['place'] + '.')
    rules_store.append(p.slice)

    rules_store.append(p.slice)
def p_ConditionalExpression(p):
    '''
    ConditionalExpression : ConditionalOrExpression
    | ConditionalOrExpression QMARK Expression COLON ConditionalExpression
    '''
    if len(p) == 2:
        p[0] = p[1]

    rules_store.append(p.slice)
def p_AssignmentExpression(p):
    '''
    AssignmentExpression : ConditionalExpression
    | Assignment
    '''
    if len(p) == 2:
        p[0] = p[1]

    rules_store.append(p.slice)
def p_Assignment(p):
    '''
    Assignment : LeftHandSide AssignmentOperator AssignmentExpression
    '''
    if 'access_type' not in p[1].keys():
        attributes = ST.find(p[1]['place'])
        if attributes == None:
            raise Exception("Undeclared variable used: "+str(p[1]['place']))
        elif 'is_array' in attributes and attributes['is_array']:
            raise Exception("Array not indexed properly" +str(p[1]['place']))
        elif 'ret_type' in p[3].keys() and p[3]['ret_type'] == attributes['type']:
            TAC.emit([p[1]['place'], p[3]['place'], '', p[2]])
        elif attributes['type'] == p[3]['type']:
            TAC.emit([p[1]['place'], p[3]['place'], '', p[2]])
        else:
            raise Exception("Type Mismatch for symbol: "+ str(p[3]['place'])+str(p[3]['type']))
    else:
        # dest = p[1]['name'] + '[' + p[1]['index'] + ']'
        TAC.emit([p[1]['name'],p[1]['index'] , p[3]['place'], 'arr='])

    rules_store.append(p.slice)
def p_LeftHandSide(p):
    '''
    LeftHandSide : Name
    | FieldAccess
    | ArrayAccess
    '''
    p[0] = p[1]
    rules_store.append(p.slice)
def p_AssignmentOperator(p):
    '''
    AssignmentOperator : ASSIGN
    | MULT_ASSIGN
    | DIVIDE_ASSIGN
    | MOD_ASSIGN
    | PLUS_ASSIGN
    | MINUS_ASSIGN
    | LSHIFT_ASSIGN
    | RSHIFT_ASSIGN
    | RRSHIFT_ASSIGN
    '''
    p[0] = p[1]

    #To check if I missed something
    rules_store.append(p.slice)
def p_Expression(p):
    '''
    Expression : AssignmentExpression
    '''
    p[0] = p[1]
    rules_store.append(p.slice)
def p_ConstantExpression(p):
    '''
    ConstantExpression : Expression
    '''
    p[0] = p[1]
    rules_store.append(p.slice)
def p_error(p):
    print("Syntax Error in line %d" %(p.lineno))

def main():
    tokens = lexer.tokens
    parser = yacc.yacc()
    global flag_mr
    flag_mr = True
    inputfile = sys.argv[1]
    # file_out = inputfile.split('/')[-1].split('.')[0]
    code = open(inputfile, 'r').read()
    code += "\n"
    print("\t.data")
    print("\toutFormatInt:")
    print("\t.string \"%d\\n\"")
    print("\toutFormatStr:")
    print("\t.string \"%s\\n\"")
    print("\tinFormat:")
    print("\t.string \"%d\\n\"")
    print("\t.global main")
    t = yacc.parse(code)
    print("\tmov $1, %eax")
    print("\tint $0x80")

    # print("...........................")
    # print(t)
    # TAC.print_tac()
    # print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    # ST.dump_TT()
    # print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    # pprint(rules_store)

    #sys.stdout = open(file_out + ".html", 'w')
    #html_output( t(i)


if __name__ == "__main__":
    main()
