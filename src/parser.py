import lexer
import ply.yacc as yacc
import argparse
import sys
from tac import *
from symbolt import SymbolTmap

tokens = lexer.tokens

TAC = TAC()
ST = SymbolTmap()


def p_Goal(p):
    '''Goal : CompilationUnit'''

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

def p_IntConst(p):
    '''
    IntConst : INT_LITERAL
    '''
    p[0] = {
        'idVal' : p[1],
        'type' : 'INT'
    }

def p_FloatConst(p):
    '''
    FloatConst : FLOAT_LITERAL
    '''
    p[0] = {
        'idVal' : p[1],
        'type' : 'FLOAT'
    }

def p_CharConst(p):
    '''
    CharConst : CHAR_LITERAL
    '''
    p[0] = {
        'idVal' : p[1],
        'type' : 'CHAR'
    }

def p_StringConst(p):
    '''
    StringConst : STRING_LITERAL
    '''
    p[0] = {
        'idVal' : p[1],
        'type' : 'STRING'
    }

def p_NullConst(p):
    '''
    NullConst : NULL
    '''
    p[0] = {
        'idVal' : p[1],
        'type' : 'NULL'
    }

def p_Type(p):
    ''' Type : PrimitiveType
            | ReferenceType '''
    p[0] = p[1]

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


def p_NumericType(p):
    ''' NumericType :   IntegralType
                      | FloatingPointType
    '''
    p[0] = p[1]

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

def p_FloatingPointType(p):
    ''' FloatingPointType :   FLOAT
                            | DOUBLE
    '''
    p[0] = {
        'type' : p[1].upper()
    }


def p_ReferenceType(p):
    ''' ReferenceType :   ArrayType
                        | ClassType
    '''
    p[0] = p[1]

def p_ClassType(p):
    ''' ClassType : Name
    '''
    p[0] = p[1]


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


def p_Name(p):
    ''' Name :    SimpleName
                | QualifiedName '''
    p[0] = p[1]
    p[0]['is_var'] = True

def p_SimpleName(p):
    ''' SimpleName : IDENTIFIER'''
    p[0] = {
        'place' : p[1],
    }


def p_QualifiedName(p):
    ''' QualifiedName : Name DOT IDENTIFIER'''
    p[0]= {
        'place' : p[1]['place'] + "." + p[3]
    }

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


def p_ImportDeclarations(p):
    '''
    ImportDeclarations : ImportDeclaration
    | ImportDeclarations ImportDeclaration
    '''


def p_TypeDeclarations(p):
    '''
    TypeDeclarations : TypeDeclaration
    | TypeDeclarations TypeDeclaration
    '''


def p_PackageDeclaration(p):
    '''
    PackageDeclaration : PACKAGE Name STMT_TERMINATOR
    '''


def p_ImportDeclaration(p):
    '''
    ImportDeclaration : SingleTypeImportDeclaration
    | TypeImportOnDemandDeclaration
    '''


def p_SingleTypeImportDeclaration(p):
    '''
    SingleTypeImportDeclaration : IMPORT Name STMT_TERMINATOR
    '''


def p_TypeImportOnDemandDeclaration(p):
    '''
    TypeImportOnDemandDeclaration : IMPORT Name DOT MULT STMT_TERMINATOR
    '''


def p_TypeDeclaration(p):
    '''
    TypeDeclaration : ClassDeclaration
    | STMT_TERMINATOR
    '''


def p_Modifiers(p):
    '''
    Modifiers : Modifier
    | Modifiers Modifier
    '''


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

def p_ClassDeclaration(p):
    '''
    ClassDeclaration : Modifiers CLASS IDENTIFIER Super ClassBody
    | Modifiers CLASS IDENTIFIER ClassBody
    | CLASS IDENTIFIER Super ClassBody
    | CLASS IDENTIFIER ClassBody
    '''


def p_Super(p):
    '''
    Super : EXTENDS ClassType
    '''

def p_ClassBody(p):
    '''
    ClassBody : L_CURLYBR R_CURLYBR
    | L_CURLYBR ClassBodyDeclarations R_CURLYBR
    '''


def p_ClassBodyDeclarations(p):
    '''
    ClassBodyDeclarations : ClassBodyDeclaration
    | ClassBodyDeclarations ClassBodyDeclaration
    '''


def p_ClassBodyDeclaration(p):
    '''
    ClassBodyDeclaration : ClassMemberDeclaration
    | ConstructorDeclaration
    | StaticInitializer
    '''


def p_ClassMemberDeclaration(p):
    '''
    ClassMemberDeclaration : FieldDeclaration
    | MethodDeclaration
    '''


def p_FieldDeclaration(p):
    '''
    FieldDeclaration : Modifiers LocalVariableDeclaration STMT_TERMINATOR
    | Type VariableDeclarators STMT_TERMINATOR
    '''


def p_VariableDeclarators(p):
    '''
    VariableDeclarators : VariableDeclarator
    | VariableDeclarators COMMA VariableDeclarator
    '''
    if len(p)==2:
    	p[0]=[p[1]]
    else:
    	p[0] = p[1] + [p[3]]


def p_VariableDeclarator(p):
    '''
    VariableDeclarator : VariableDeclaratorId
    | VariableDeclaratorId ASSIGN VariableInitializer
    '''
    p[0] = {}
    if len(p) == 2:
        p[0]['place'] = p[1]
        return
    elif type(p[3]) != type({}):
        return
    if 'ret_type' in p[3].keys():
        p[0]['place'] = p[1]
        p[0]['type'] = p[3]['ret_type']
    else:
        TAC.emit(p[1][0], p[3]['place'], '', p[2])
        p[0]['place'] = p[1]
        if 'is_var' not in p[3]:
            attributes = ST.find(p[3]['place'])
            # if 'is_array' in attributes and attributes['is_array']:
            #     p[0]['is_array'] = True
            #     p[0]['arr_size'] = attributes['arr_size']
            # else:
            p[0]['is_array'] = False

        p[0]['type'] = p[3]['type']


def p_VariableDeclaratorId(p):
    '''
    VariableDeclaratorId : IDENTIFIER
    '''
    p[0] = p[1]



def p_VariableInitializer(p):
    '''
    VariableInitializer : Expression
    | ArrayInitializer
    '''
    p[0] = p[1]


def p_MethodDeclaration(p):
    '''
    MethodDeclaration : MethodHeader MethodAddParentScope MethodBody
    '''
    TAC.emit('ret','','','')
    ST.scope_terminate()


def p_MethodAddParentScope(p):
    '''
    MethodAddParentScope :
    '''
    par_scope = ST.parent_scope()
    ST.insert(p[-1]['name'], p[-1]['type'],func=True, params=p[-1]['args'], scope=par_scope)


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
        # TODO
        pass
    elif len(p) == 3:
        p[0]['name'] = p[2]['name']
        p[0]['args'] = p[2]['args']
        if type(p[1]) == type({}):
            p[0]['type'] = p[1]['type']############################################################################3
        else:
            p[0]['type'] = 'VOID'
        # global global_return_type ###############################################################################
        # global_return_type = p[0]['type']

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
        for parameter in p[4]:
            ST.insert(parameter['place'],parameter['type'])
    TAC.emit(['func', p[1], '', ''])

def p_MethodCreateScope(p):
    '''
    MethodCreateScope :
    '''
    ST.create_table(p[-2])

def p_FormalParametersList(p):
    '''
    FormalParameterList : FormalParameter
    | FormalParameterList COMMA FormalParameter
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]    

def p_FormalParameter(p):
    '''
    FormalParameter : Type VariableDeclaratorId
    '''
    p[0] = {
        'place' : p[2][0],
        'type' : p[1]['type']
    }


def p_Throws(p):
    '''
    Throws : THROWS ClassTypeList
    '''


def p_ClassTypeList(p):
    '''
    ClassTypeList : ClassType
    | ClassTypeList COMMA ClassType
    '''


def p_MethodBody(p):
    '''
    MethodBody : Block
    | STMT_TERMINATOR
    '''


def p_StaticInitializer(p):
    '''
    StaticInitializer : STATIC Block
    '''


def p_ConstructorDeclaration(p):
    '''
    ConstructorDeclaration : Modifiers ConstructorDeclarator Throws ConstructorBody
    | Modifiers ConstructorDeclarator ConstructorBody
    | ConstructorDeclarator Throws ConstructorBody
    | ConstructorDeclarator ConstructorBody
    '''


def p_ConstructorDeclarator(p):
    '''
    ConstructorDeclarator : SimpleName L_ROUNDBR FormalParameterList R_ROUNDBR
    | SimpleName L_ROUNDBR R_ROUNDBR
    '''


def p_ConstructorBody(p):
    '''
    ConstructorBody : L_CURLYBR ExplicitConstructorInvocation BlockStatements R_CURLYBR
    | L_CURLYBR ExplicitConstructorInvocation R_CURLYBR
    | L_CURLYBR BlockStatements R_CURLYBR
    | L_CURLYBR R_CURLYBR
    '''


def p_ExplicitConstructorInvocation(p):
    '''
    ExplicitConstructorInvocation : THIS L_ROUNDBR ArgumentList R_ROUNDBR STMT_TERMINATOR
    | THIS L_ROUNDBR R_ROUNDBR STMT_TERMINATOR
    | SUPER L_ROUNDBR ArgumentList R_ROUNDBR STMT_TERMINATOR
    | SUPER L_ROUNDBR R_ROUNDBR STMT_TERMINATOR
    '''

def p_ArrayInitializer(p):
    '''
    ArrayInitializer : L_CURLYBR VariableInitializers R_CURLYBR
    | L_CURLYBR R_CURLYBR
    '''
    #############################################################################################################################################


def p_VariableInitializers(p):
    '''
    VariableInitializers : VariableInitializer
    | VariableInitializers COMMA VariableInitializer
    '''

def p_Block(p):
    '''
    Block : L_CURLYBR R_CURLYBR
    | L_CURLYBR BlockStatements R_CURLYBR
    '''


def p_BlockStatements(p):
    '''
    BlockStatements : BlockStatement
    | BlockStatements BlockStatement
    '''

def p_BlockStatement(p):
    '''
    BlockStatement : LocalVariableDeclarationStatement
    | Statement
    '''
    p[0] = p[1]


def p_LocalVariableDeclarationStatement(p):
    '''
    LocalVariableDeclarationStatement : LocalVariableDeclaration STMT_TERMINATOR
    '''
    p[0] = p[1]


def p_LocalVariableDeclaration(p):
    '''
    LocalVariableDeclaration : Type VariableDeclarators
    '''
    for symbol in p[2]:
        i = symbol['place']
        if 'type' in symbol:
            t = symbol['type']
        else:
            t = None
        if 'is_array' not in p[1].keys():
            if t == None:
                ST.insert(i, p[1]['type'])
                return
            if len(i) == 2:
                raise Exception("Array cannot be assigned to a primitive type")
            if len(t) == 2 and t[1] != 0:
                raise Exception("Mismatch in function return: %s" %(i))
            if type(t) == type(tuple([])) and t[0] != p[1]['type']:
                raise Exception("Type mismatch: Expected %s, but got %s" %(p[1]['type'], t[0]))
            if type(t) != type(tuple([])) and t != p[1]['type']:
                raise Exception("Type mismatch: Expected %s, but got %s" %(p[1]['type'], t))
            ST.insert(i, p[1]['type'])
        else:
            if type(i) != type(' '):
                if t == None:
                    ST.insert(i[0], p[1]['type'], is_array=True, arr_size=i[1])
                    return
                if len(i) == 1:
                    raise Exception("Primitive types cannot be assigned to array")
                if len(i[1]) != int(p[1]['arr_size']):
                    raise Exception("Dimension mismatch for array: %s" %(i[0]))
                if type(t) != type(tuple([])) and t != p[1]['type']:
                    raise Exception("Type mismatch: Expected %s, but got %s" %(p[1]['type'], t))
                if type(t) == type(tuple([])) and t[0] != p[1]['type']:
                    raise Exception("Type mismatch: Expected %s, but got %s" %(p[1]['type'], t[0]))
                ST.insert(i[0], p[1]['type'], is_array=True, arr_size=i[1])
            else:
                if t == None:
                    ST.insert(i, p[1]['type'], is_array=True, arr_size=0)
                    return
                if type(t) == type(tuple([])) and t[0] != p[1]['type']:
                    raise Exception("%s and %s types are not compatible" %(t[0], p[1]['type']))
                if 'is_array' not in symbol:
                    raise Exception("Array assignment was expected: %s" %(i))
                if 'is_array' in symbol and t != p[1]['type']:
                    raise Exception("%s and %s types are not compatible" %(t, p[1]['type']))
                if 'is_array' in symbol and len(symbol['arr_size']) != p[1]['arr_size']:
                    raise Exception("Array dimensions mismatch: %s" %(i))
                ST.insert(i, p[1]['type'], is_array=True, arr_size=0)
    


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


def p_StatementNoShortIf(p):
    '''
    StatementNoShortIf : StatementWithoutTrailingSubstatement
    | LabeledStatementNoShortIf
    | IfThenElseStatementNoShortIf
    | WhileStatementNoShortIf
    | ForStatementNoShortIf
    '''
    p[0] = p[1]



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


def p_EmptyStatement(p):
    '''
    EmptyStatement : STMT_TERMINATOR
    '''


def p_LabeledStatement(p):
    '''
    LabeledStatement : IDENTIFIER COLON Statement
    '''


def p_LabeledStatementNoShortIf(p):
    '''
    LabeledStatementNoShortIf : IDENTIFIER COLON StatementNoShortIf
    '''


def p_ExpressionStatement(p):
    '''
    ExpressionStatement : StatementExpression STMT_TERMINATOR
    '''
    p[0] = p[1]



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



def p_IfThenStatement(p):
    '''
    IfThenStatement : IF L_ROUNDBR Expression R_ROUNDBR IfstartSc Statement IfendSc
    '''


def p_IfThenElseStatement(p):
    '''
    IfThenElseStatement : IF L_ROUNDBR Expression R_ROUNDBR IfstartSc StatementNoShortIf ELSE ElseStartSc Statement ElseEndSc
    '''


def p_IfThenElseStatementNoShortIf(p):
    '''
    IfThenElseStatementNoShortIf : IF L_ROUNDBR Expression R_ROUNDBR IfstartSc StatementNoShortIf ELSE ElseStartSc StatementNoShortIf ElseEndSc
    '''


def p_IfstartSc(p):
    '''IfstartSc : '''
    labelif = ST.ident()
    labelafterif = ST.ident()
    TAC.emit(['ifgoto', p[-2]['place'], 'eq 0', labelafterif])
    TAC.emit(['goto', labelif, '', ''])
    TAC.emit(['label', labelif, '', ''])
    ST.create_table(labelif)
    p[0] = [labelif, labelafterif]

def p_IfendSc(p):
    '''IfendSc : '''
    ST.scope_terminate()
    TAC.emit(['label', p[-2][1], '', ''])

def p_ElseStartSc(p):
    '''ElseStartSc : '''
    ST.scope_terminate()
    labelend = ST.ident()
    TAC.emit(['goto', labelend, '', ''])
    TAC.emit(['label', p[-3][1], '', ''])
    ST.create_table(p[-3][1])
    p[0] = [labelend]

def p_ElseEndSc(p):
    '''ElseEndSc : '''
    ST.scope_terminate()
    TAC.emit(['label', p[-2][0], '', ''])


######################################################################################################3#
def p_SwitchStatement(p):
    '''
    SwitchStatement : SWITCH L_ROUNDBR Expression R_ROUNDBR SwitchBlock
    '''
#######################################################################################################33



def p_SwitchBlock(p):
    '''
    SwitchBlock : L_CURLYBR R_CURLYBR
    | L_CURLYBR SwitchBlockStatementGroups SwitchLabels R_CURLYBR
    | L_CURLYBR SwitchBlockStatementGroups R_CURLYBR
    | L_CURLYBR SwitchLabels R_CURLYBR
    '''
    p[0] = p[2]


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


def p_SwitchBlockStatementGroup(p):
    '''
    SwitchBlockStatementGroup : SwitchLabels BlockStatements
    '''
    p[0] = p[1]

#############################################################################################################################################3
def p_SwitchLabels(p):
    '''
    SwitchLabels : SwitchLabel
    | SwitchLabels SwitchLabel
    '''


def p_SwitchLabel(p):
    '''
    SwitchLabel : CASE ConstantExpression COLON
    | DEFAULT COLON
    '''


def p_WhileStatement(p):
    '''
    WhileStatement : WHILE L_ROUNDBR Expression R_ROUNDBR Statement
    '''


def p_WhileStatementNoShortIf(p):
    '''
    WhileStatementNoShortIf : WHILE L_ROUNDBR Expression R_ROUNDBR StatementNoShortIf
    '''


def p_DoStatement(p):
    '''
    DoStatement : DO Statement WHILE L_ROUNDBR Expression R_ROUNDBR STMT_TERMINATOR
    '''


def p_ForStatement(p):
    '''
    ForStatement : FOR L_ROUNDBR ForInit STMT_TERMINATOR Expression STMT_TERMINATOR ForUpdate R_ROUNDBR Statement
    | FOR L_ROUNDBR STMT_TERMINATOR Expression STMT_TERMINATOR ForUpdate R_ROUNDBR Statement
    | FOR L_ROUNDBR ForInit STMT_TERMINATOR STMT_TERMINATOR ForUpdate R_ROUNDBR Statement
    | FOR L_ROUNDBR ForInit STMT_TERMINATOR Expression STMT_TERMINATOR R_ROUNDBR Statement
    | FOR L_ROUNDBR ForInit STMT_TERMINATOR STMT_TERMINATOR R_ROUNDBR Statement
    | FOR L_ROUNDBR STMT_TERMINATOR Expression STMT_TERMINATOR R_ROUNDBR Statement
    | FOR L_ROUNDBR STMT_TERMINATOR STMT_TERMINATOR ForUpdate R_ROUNDBR Statement
    | FOR L_ROUNDBR STMT_TERMINATOR STMT_TERMINATOR R_ROUNDBR Statement
    '''


def p_ForStatementNoShortIf(p):
    '''
    ForStatementNoShortIf : FOR L_ROUNDBR ForInit STMT_TERMINATOR Expression STMT_TERMINATOR ForUpdate R_ROUNDBR StatementNoShortIf
    | FOR L_ROUNDBR STMT_TERMINATOR Expression STMT_TERMINATOR ForUpdate R_ROUNDBR StatementNoShortIf
    | FOR L_ROUNDBR ForInit STMT_TERMINATOR STMT_TERMINATOR ForUpdate R_ROUNDBR StatementNoShortIf
    | FOR L_ROUNDBR ForInit STMT_TERMINATOR Expression STMT_TERMINATOR R_ROUNDBR StatementNoShortIf
    | FOR L_ROUNDBR ForInit STMT_TERMINATOR STMT_TERMINATOR R_ROUNDBR StatementNoShortIf
    | FOR L_ROUNDBR STMT_TERMINATOR Expression STMT_TERMINATOR R_ROUNDBR StatementNoShortIf
    | FOR L_ROUNDBR STMT_TERMINATOR STMT_TERMINATOR ForUpdate R_ROUNDBR StatementNoShortIf
    | FOR L_ROUNDBR STMT_TERMINATOR STMT_TERMINATOR R_ROUNDBR StatementNoShortIf
    '''


def p_ForInit(p):
    '''
    ForInit : StatementExpressionList
    | LocalVariableDeclaration
    '''


def p_ForUpdate(p):
    '''
    ForUpdate : StatementExpressionList
    '''


def p_StatementExpressionList(p):
    '''
    StatementExpressionList : StatementExpression
    | StatementExpressionList COMMA StatementExpression
    '''


def p_BreakStatement(p):
    '''
    BreakStatement : BREAK IDENTIFIER STMT_TERMINATOR
    | BREAK STMT_TERMINATOR
    '''


def p_ContinueStatement(p):
    '''
    ContinueStatement : CONTINUE IDENTIFIER STMT_TERMINATOR
    | CONTINUE STMT_TERMINATOR
    '''

#########################################################################################################################################3


def p_ReturnStatement(p):
    '''
    ReturnStatement : RETURN Expression STMT_TERMINATOR
    | RETURN STMT_TERMINATOR
    '''
    if len(p)==3 :
        TAC.emit(['ret', '', '', ''])
    else:
        to_return = ST.find(ST.cur_sc,func=True)['type']
        curr_returned = ST.find(p[2]['place'])
        if curr_returned != None:
            # if to_return[0] != curr_returned['type']:
            if to_return != curr_returned['type']:
                raise Exception("Wrong return type in %s" %(ST.cur_sc))
            # if 'is_array' in curr_returned.keys() and len(curr_returned['arr_size']) != to_return[1]:
                # raise Exception("Dimension mismatch in return statement in %s" %(ST.curr_scope))
        else:
            # if p[2]['type'] != to_return[0] or to_return[1] != 0:
            if p[2]['type'] != to_return :
                raise Exception("Wrong return type in %s" %(ST.cur_sc))
        TAC.emit(['ret', p[2]['place'], '', ''])


def p_ThrowStatement(p):
    '''
    ThrowStatement : THROW Expression STMT_TERMINATOR
    '''


def p_TryStatement(p):
    '''
    TryStatement : TRY Block Catches
    | TRY Block Catches Finally
    | TRY Block Finally
    '''


def p_Catches(p):
    '''
    Catches : CatchClause
    | Catches CatchClause
    '''


def p_CatchClause(p):
    '''
    CatchClause : CATCH L_ROUNDBR FormalParameter R_ROUNDBR Block
    '''


def p_Finally(p):
    '''
    Finally : FINALLY Block
    '''



			# Section 19.12

def p_Primary(p):
    '''
    Primary : PrimaryNoNewArray
    | ArrayCreationExpression
    '''
    p[0] = p[1]


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


def p_ClassInstanceCreationExpression(p):
    '''
    ClassInstanceCreationExpression : NEW ClassType L_ROUNDBR R_ROUNDBR
    | NEW ClassType L_ROUNDBR ArgumentList R_ROUNDBR
    '''


def p_ArgumentList(p):
    '''
    ArgumentList : Expression
    | ArgumentList COMMA Expression
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]


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

def p_DimExprs(p):
    '''
    DimExprs : DimExpr
    | DimExprs DimExpr
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_DimExpr(p):
    '''
    DimExpr : L_SQBR Expression R_SQBR
    '''
    if p[2]['type'] == 'INT':
        p[0] = p[2]['place']
    else:
        raise Exception("Array declaration requires a size as integer : " + p[2]['place'])


def p_Dims(p):
    '''
    Dims : L_SQBR R_SQBR
    | Dims L_SQBR R_SQBR
    '''
    if len(p) == 3:
        p[0] = 1
    else:
        p[0] = 1 + p[1]


def p_FieldAccess(p):
    '''
    FieldAccess : Primary DOT IDENTIFIER
    | SUPER DOT IDENTIFIER
    '''


def p_MethodInvocation(p):
    '''
    MethodInvocation : Name L_ROUNDBR ArgumentList R_ROUNDBR
    | Name L_ROUNDBR R_ROUNDBR
    | Primary DOT IDENTIFIER L_ROUNDBR ArgumentList R_ROUNDBR
    | Primary DOT IDENTIFIER L_ROUNDBR R_ROUNDBR
    | SUPER DOT IDENTIFIER L_ROUNDBR ArgumentList R_ROUNDBR
    | SUPER DOT IDENTIFIER L_ROUNDBR R_ROUNDBR
    '''
    if p[2] == '(':
        attributes = ST.find(p[1]['place'], is_func=True)
        if attributes == None and p[1]['place'] != "System.out.println":
            raise Exception("Undeclared function used: %s" %(p[1]['place']))

        if p[1]['place'] == 'System.out.println':
            if len(p) == 5:
                for parameter in p[3]:
                    TAC.emit(['print',parameter['place'],'',''])
        else:
            temp_var = ST.Temp_var()
            if len(p) == 5:
                prototype = attributes['params']
                if len(prototype) != len(p[3]):
                    raise Exception("Wrong number of arguments to function call: %s" %(p[1]['place']))
                for i in range(len(p[3])):
                    parameter = p[3][i]
                    proto = prototype[i]
                    if parameter['type'] != proto['type']:
                        raise Exception("Wrong type of arg passed to function %s; got %s but expected %s" %(p[1]['place'], parameter['type'], proto['type']))
                    TAC.emit(['param',parameter['place'],'',''])
            TAC.emit(['call',p[1]['place'],temp_var,''])
            p[0] = {
                'place' : temp_var,
                'ret_type' : attributes['type']
            }


def p_ArrayAccess(p):
    '''
    ArrayAccess : Name L_SQBR Expression R_SQBR
    | PrimaryNoNewArray L_SQBR Expression R_SQBR
    '''
    p[0] = {}
    attributes = ST.find(p[1]['place'])
    if attributes == None:
        raise Exception("Undeclared Symbol Used: %s" %(p[1]['place']))
    if not 'is_array' in attributes or not attributes['is_array']:
        raise Exception("Only array type can be indexed : %s" %(p[1]['place']))

    indexes = p[2]
    if not len(indexes) == len(attributes['arr_size']):
        raise Exception("Not a valid indexing for array %s" %(p[1]['place']))

    arr_size = attributes['arr_size']
    address_indices = p[2]
    t2 = ST.get_temp_var()
    TAC.emit([t2, address_indices[0], '', '='])
    for i in range(1, len(address_indices)):
        TAC.emit([t2, t2, arr_size[i], '*'])
        TAC.emit([t2, t2, address_indices[i], '+'])
    index = t2

    src = p[1]['place'] + '[' + str(index) + ']'
    t1 = ST.temp_var()
    TAC.emit([t1, src, '', '='])

    p[0]['type'] = attributes['type']
    p[0]['place'] = t1
    p[0]['access_type'] = 'array'
    p[0]['name'] = p[1]['place']
    p[0]['index'] = str(index)


def p_PostfixExpression(p):
    '''
    PostfixExpression : Primary
    | Name
    | PostIncrementExpression
    | PostDecrementExpression
    '''
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
        #TODO: Temporarily removing to run method invocation
        # p[0]['type'] = p[1]['type']
        # p[0]['place'] = p[1]['place']


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


def p_UnaryExpression(p):
    '''
    UnaryExpression : PreIncrementExpression
    | PreDecrementExpression
    | PLUS UnaryExpression
    | MINUS UnaryExpression
    | UnaryExpressionNotPlusMinus
    '''
    p[0] = p[1]


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
        TAC.emit([t, p[2]['place'], '', p[1]])
        p[0] = p[2]
        p[0]['place'] = t


def p_CastExpression(p):
    '''
    CastExpression : L_ROUNDBR PrimitiveType Dims R_ROUNDBR UnaryExpression
    | L_ROUNDBR PrimitiveType R_ROUNDBR UnaryExpression
    | L_ROUNDBR Expression R_ROUNDBR UnaryExpressionNotPlusMinus
    | L_ROUNDBR Name Dims R_ROUNDBR UnaryExpressionNotPlusMinus
    '''


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
        'type' : 'TYPE_ERROR'
    }
    if p[1]['type'] == 'TYPE_ERROR' or p[3]['type'] == 'TYPE_ERROR':
        return
    if p[2] == '*':
        if p[1]['type'] == 'INT' and p[3]['type'] == 'INT' :
            TAC.emit([newPlace,p[1]['place'], p[3]['place'], p[2]])
            p[0]['type'] = 'INT'
        else:
            raise Exception('Error: Type is not compatible'+p[1]['place']+','+p[3]['place']+'.')
    elif p[2] == '/' :
        if p[1]['type'] == 'INT' and p[3]['type'] == 'INT' :
            TAC.emit([newPlace, p[1]['place'], p[3]['place'], p[2]])
            p[0]['type'] = 'INT'
        else:
            raise Exception('Error: Type is not compatible' + p[1]['place'] + ',' + p[3]['place'] + '.')
    elif p[2] == '%':
        if p[1]['type'] == 'INT' and p[3]['type'] == 'INT' :
            TAC.emit([newPlace,p[1]['place'],p[3]['place'],p[2]])
            p[0]['type'] = 'INT'
        else:
            raise Exception('Error: Type is not compatible' + p[1]['place'] + ',' + p[3]['place'] + '.')


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
        'type' : 'TYPE_ERROR'
    }
    if p[1]['type'] == 'TYPE_ERROR' or p[3]['type'] == 'TYPE_ERROR':
        return

    if p[1]['type'] == 'INT' and p[3]['type'] == 'INT':
        TAC.emit([newPlace, p[1]['place'], p[3]['place'], p[2]])
        p[0]['type'] = 'INT'
    else:
        raise Exception("Error: integer value is needed")

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
        'type' : 'TYPE_ERROR'
    }
    if p[1]['type'] == 'TYPE_ERROR' or p[3]['type'] == 'TYPE_ERROR':
        return

    if p[1]['type'] == 'INT' and p[3]['type'] == 'INT':
        TAC.emit([newPlace, p[1]['place'], p[3]['place'], p[2]])
        p[0]['type'] = 'INT'
    else:
        raise Exception("Error: integer value is needed")


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
        'type' : 'TYPE_ERROR'
    }
    if p[1]['type']=='TYPE_ERROR' or p[3]['type']=='TYPE_ERROR':
        return

    if p[1]['type'] == 'INT' and p[3]['type'] == 'INT' :
        if p[2]=='>':
            TAC.emit(['ifgoto', p[1]['place'], 'gt ' + p[3]['place'], l2])
            TAC.emit(['label', l1, '', ''])
            TAC.emit([newPlace, '0', '', '='])
            TAC.emit(['goto', l3, '', ''])
            TAC.emit(['label', l2, '', ''])
            TAC.emit([newPlace, '1', '', '='])
            TAC.emit(['label', l3, '', ''])
            p[0]['type'] = 'INT'
        elif p[2]=='>=':
            TAC.emit(['ifgoto', p[1]['place'], 'geq ' + p[3]['place'], l2])
            TAC.emit(['label', l1, '', ''])
            TAC.emit([newPlace, '0', '', '='])
            TAC.emit(['goto', l3, '', ''])
            TAC.emit(['label', l2, '', ''])
            TAC.emit([newPlace, '1', '', '='])
            TAC.emit(['label', l3, '', ''])
            p[0]['type'] = 'INT'
        elif p[2]=='<':
            TAC.emit(['ifgoto', p[1]['place'], 'lt ' + p[3]['place'], l2])
            TAC.emit(['label', l1, '', ''])
            TAC.emit([newPlace, '0', '', '='])
            TAC.emit(['goto', l3, '', ''])
            TAC.emit(['label', l2, '', ''])
            TAC.emit([newPlace, '1', '', '='])
            TAC.emit(['label', l3, '', ''])
            p[0]['type'] = 'INT'
        elif p[2]=='<=':
            TAC.emit(['ifgoto', p[1]['place'], 'leq ' + p[3]['place'], l2])
            TAC.emit(['label', l1, '', ''])
            TAC.emit([newPlace, '0', '', '='])
            TAC.emit(['goto', l3, '', ''])
            TAC.emit(['label', l2, '', ''])
            TAC.emit([newPlace, '1', '', '='])
            TAC.emit(['label', l3, '', ''])
            p[0]['type'] = 'INT'
    else:
        raise Exception('Error: Type is not compatible' + p[1]['place'] + ',' + p[3]['place'] + '.')
    


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
        'type' : 'TYPE_ERROR'
    }
    if p[1]['type']=='TYPE_ERROR' or p[3]['type']=='TYPE_ERROR':
        return
    if p[1]['type'] == 'INT' and p[3]['type'] == 'INT' :
        if(p[2][0]=='='):
            TAC.emit(['ifgoto', p[1]['place'], 'eq ' + p[3]['place'], l2])
            TAC.emit(['label', l1, '', ''])
            TAC.emit([newPlace, '0', '', '='])
            TAC.emit(['goto', l3, '', ''])
            TAC.emit(['label', l2, '', ''])
            TAC.emit([newPlace, '1', '', '='])
            TAC.emit(['label', l3, '', ''])
            p[0]['type'] = 'INT'
        else:
            TAC.emit(['ifgoto', p[1]['place'], 'neq '+ p[3]['place'], l2])
            TAC.emit(['label', l1, '', ''])
            TAC.emit([newPlace, '0', '', '='])
            TAC.emit(['goto', l3, '', ''])
            TAC.emit(['label', l2, '', ''])
            TAC.emit([newPlace, '1', '', '='])
            TAC.emit(['label', l3, '', ''])
            p[0]['type'] = 'INT'
    else:
        raise Exception('Only INT type comparisions supported: ' + p[1]['place'] + ' and' + p[3]['place'])
    


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
        'type' : 'TYPE_ERROR'
    }
    if p[1]['type']=='TYPE_ERROR' or p[3]['type']=='TYPE_ERROR':
        return
    if p[1]['type'] == 'INT' and p[3]['type'] == 'INT' :
        TAC.emit([newPlace,p[1]['place'],p[3]['place'],'&'])
        p[0]['type'] = 'INT'
    else:
        raise Exception('Error: Type is not compatible' + p[1]['place'] + ',' + p[3]['place'] + '.')

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
        'type' : 'TYPE_ERROR'
    }
    if p[1]['type']=='TYPE_ERROR' or p[3]['type']=='TYPE_ERROR':
        return
    if p[1]['type'] == 'INT' and p[3]['type'] == 'INT' :
        TAC.emit([newPlace,p[1]['place'],p[3]['place'],'^'])
        p[0]['type'] = 'INT'
    else:
        raise Exception('Error: Type is not compatible' + p[1]['place'] + ',' + p[3]['place'] + '.')


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
        'type' : 'TYPE_ERROR'
    }
    if p[1]['type']=='TYPE_ERROR' or p[3]['type']=='TYPE_ERROR':
        return
    if p[1]['type'] == 'INT' and p[3]['type'] == 'INT' :
        TAC.emit([newPlace, p[1]['place'], p[3]['place'], '|'])
        p[0]['type'] = 'INT'
    else:
        raise Exception('Error: Type is not compatible' + p[1]['place'] + ',' + p[3]['place'] + '.')
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
        'type' : 'TYPE_ERROR'
    }
    if p[1]['type']=='TYPE_ERROR' or p[3]['type']=='TYPE_ERROR':
        p[0]=p[1]
        return
    if p[1]['type'] == 'INT' and p[3]['type'] == 'INT' :
        l1 = ST.ident()
        TAC.emit([newPlace,p[1]['place'],'','='])
        TAC.emit(['ifgoto',p[1]['place'],'eq 0',l1])
        TAC.emit([newPlace, p[1]['place'], p[3]['place'], '&'])
        TAC.emit(['label',l1,'',''])
        p[0]['type'] = 'INT'
    else:
        raise Exception('Error: Type is not compatible' + p[1]['place'] + ',' + p[3]['place'] + '.')

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
        'type' : 'TYPE_ERROR'
    }
    if p[1]['type']=='TYPE_ERROR' or p[3]['type']=='TYPE_ERROR':
        return
    if p[1]['type'] == 'INT' and p[3]['type'] == 'INT' :
        l1 = ST.ident()
        TAC.emit([newPlace,p[1]['place'],'','='])
        TAC.emit(['ifgoto',p[1]['place'],'eq 1',l1])
        TAC.emit([newPlace, p[1]['place'], p[3]['place'], '|'])
        TAC.emit(['label',l1,'',''])
        p[0]['type'] = 'INT'
    else:
        raise Exception('Error: Type is not compatible' + p[1]['place'] + ',' + p[3]['place'] + '.')
    rules_store.append(p.slice)


def p_ConditionalExpression(p):
    '''
    ConditionalExpression : ConditionalOrExpression
    | ConditionalOrExpression QMARK Expression COLON ConditionalExpression
    '''
    if len(p) == 2:
        p[0] = p[1]


def p_AssignmentExpression(p):
    '''
    AssignmentExpression : ConditionalExpression
    | Assignment
    '''
    if len(p) == 2:
        p[0] = p[1]


def p_Assignment(p):
    '''
    Assignment : LeftHandSide AssignmentOperator AssignmentExpression
    '''
    if 'access_type' not in p[1].keys():
        attributes = ST.find(p[1]['place'])
        if attributes == None:
            raise Exception("Undeclared variable used: "+str(p[1]['place']))
        if 'is_array' in attributes and attributes['is_array']:
            raise Exception("Array '%s' not indexed properly" +str(p[1]['place']))
        if attributes['type'] == p[3]['type']:
            TAC.emit([p[1]['place'], p[3]['place'], '', p[2]])
        else:
            raise Exception("Type Mismatch for symbol: "+str(p[3]['place']))
    else:
        dest = p[1]['name'] + '[' + p[1]['index'] + ']'
        TAC.emit([dest, p[3]['place'], '', '='])


def p_LeftHandSide(p):
    '''
    LeftHandSide : Name
    | FieldAccess
    | ArrayAccess
    '''
    p[0] = p[1]

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

def p_Expression(p):
    '''
    Expression : AssignmentExpression
    '''
    p[0] = p[1]

def p_ConstantExpression(p):
    '''
    ConstantExpression : Expression
    '''
    p[0] = p[1]

def p_error(p):
    print("Syntax Error in line %d" %(p.lineno))


def main():
    tokens = lexer.tokens
    parser = yacc.yacc()
    inputfile = sys.argv[1]
    # file_out = inputfile.split('/')[-1].split('.')[0]
    code = open(inputfile, 'r').read()
    code += "\n"
    t = yacc.parse(code)
    print(t)
    #sys.stdout = open(file_out + ".html", 'w')
    #html_output( t(i)


if __name__ == "__main__":
    main()
