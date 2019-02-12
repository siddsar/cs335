import lexer
import ply.yacc as yacc
import argparse
import sys

tokens = lexer.tokens




def p_Goal(p):
    '''Goal : CompilationUnit'''


def p_Type(p):
    ''' Type : PrimitiveType 
            | ReferenceType '''


def p_Literal(p):
    ''' Literal :   INT_LITERAL
                  | FLOAT_LITERAL
                  | CHAR_LITERAL
                  | STRING_LITERAL
                  | NULL
    '''
    
def p_PrimitiveType(p):
    ''' PrimitiveType :    NumericType
                         | BOOLEAN
    '''

def p_NumericType(p):
    ''' NumericType :   IntegralType
                      | FloatingPointType
    '''
    
def p_IntegralType(p):
    ''' IntegralType :    BYTE
                        | SHORT
                        | INT
                        | LONG
                        | CHAR
    '''
    

def p_FloatingPointType(p):
    ''' FloatingPointType :   FLOAT
                            | DOUBLE
    '''
    

def p_ReferenceType(p):
    ''' ReferenceType :   ArrayType
                        | ClassType
    '''
    
def p_ClassType(p):
    ''' ClassType : Name
    '''
    

def p_ArrayType(p):
    ''' ArrayType :    PrimitiveType L_SQBR R_SQBR
                     | Name L_SQBR R_SQBR
                     | ArrayType L_SQBR R_SQBR
    '''

def p_Name(p):
    ''' Name :    SimpleName
                | QualifiedName '''
    

def p_SimpleName(p):
    ''' SimpleName : IDENTIFIER'''
    

def p_QualifiedName(p):
    ''' QualifiedName : Name DOT IDENTIFIER'''
    

# Section 19.6

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
    '''
    
# Section 19.8

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
    FieldDeclaration : Modifiers Type VariableDeclarators STMT_TERMINATOR
    | Type VariableDeclarators STMT_TERMINATOR
    '''
    

def p_VariableDeclarators(p):
    '''
    VariableDeclarators : VariableDeclarator
    | VariableDeclarators COMMA VariableDeclarator
    '''
    

def p_VariableDeclarator(p):
    '''
    VariableDeclarator : VariableDeclaratorId
    | VariableDeclaratorId ASSIGN VariableInitializer
    '''
    

def p_VariableDeclaratorId(p):
    '''
    VariableDeclaratorId : IDENTIFIER
    | VariableDeclaratorId L_SQBR R_SQBR
    '''
    

def p_VariableInitializer(p):
    '''
    VariableInitializer : Expression
    | ArrayInitializer
    '''
    

def p_MethodDeclaration(p):
    '''
    MethodDeclaration : MethodHeader MethodBody
    '''
    

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
    

def p_MethodDeclarator(p):
    '''
    MethodDeclarator : IDENTIFIER L_ROUNDBR R_ROUNDBR
    | IDENTIFIER L_ROUNDBR FormalParameterList R_ROUNDBR
    '''
    

def p_FormalParametersList(p):
    '''
    FormalParameterList : FormalParameter
    | FormalParameterList COMMA FormalParameter
    '''
    

def p_FormalParameter(p):
    '''
    FormalParameter : Type VariableDeclaratorId
    '''
    

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
    

# Section 19.9 is about Interfaces

# Section 19.10
def p_ArrayInitializer(p):
    '''
    ArrayInitializer : L_CURLYBR VariableInitializers R_CURLYBR
    | L_CURLYBR R_CURLYBR
    '''
    

def p_VariableInitializers(p):
    '''
    VariableInitializers : VariableInitializer
    | VariableInitializers COMMA VariableInitializer
    '''
    

# Section 19.11
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
    

def p_LocalVariableDeclarationStatement(p):
    '''
    LocalVariableDeclarationStatement : LocalVariableDeclaration STMT_TERMINATOR
    '''
    

def p_LocalVariableDeclaration(p):
    '''
    LocalVariableDeclaration : Type VariableDeclarators
    '''
    

def p_Statement(p):
    '''
    Statement : StatementWithoutTrailingSubstatement
    | LabeledStatement
    | IfThenStatement
    | IfThenElseStatement
    | WhileStatement
    | ForStatement
    '''
    

def p_StatementNoShortIf(p):
    '''
    StatementNoShortIf : StatementWithoutTrailingSubstatement
    | LabeledStatementNoShortIf
    | IfThenElseStatementNoShortIf
    | WhileStatementNoShortIf
    | ForStatementNoShortIf
    '''
    

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
    

def p_IfThenStatement(p):
    '''
    IfThenStatement : IF L_ROUNDBR Expression R_ROUNDBR Statement
    '''
    

def p_IfThenElseStatement(p):
    '''
    IfThenElseStatement : IF L_ROUNDBR Expression R_ROUNDBR StatementNoShortIf ELSE Statement
    '''
    

def p_IfThenElseStatementNoShortIf(p):
    '''
    IfThenElseStatementNoShortIf : IF L_ROUNDBR Expression R_ROUNDBR StatementNoShortIf ELSE StatementNoShortIf
    '''
    

def p_SwitchStatement(p):
    '''
    SwitchStatement : SWITCH L_ROUNDBR Expression R_ROUNDBR SwitchBlock
    '''
    

def p_SwitchBlock(p):
    '''
    SwitchBlock : L_CURLYBR R_CURLYBR
    | L_CURLYBR SwitchBlockStatementGroups SwitchLabels R_CURLYBR
    | L_CURLYBR SwitchBlockStatementGroups R_CURLYBR
    | L_CURLYBR SwitchLabels R_CURLYBR
    '''
    

def p_SwitchBlockStatementGroups(p):
    '''
    SwitchBlockStatementGroups : SwitchBlockStatementGroup
    | SwitchBlockStatementGroups SwitchBlockStatementGroup
    '''
    

def p_SwitchBlockStatementGroup(p):
    '''
    SwitchBlockStatementGroup : SwitchLabels BlockStatements
    '''
    

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
    

def p_ReturnStatement(p):
    '''
    ReturnStatement : RETURN Expression STMT_TERMINATOR
    | RETURN STMT_TERMINATOR
    '''
    

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
    

def p_ArrayCreationExpression(p):
    '''
    ArrayCreationExpression : NEW PrimitiveType DimExprs Dims
    | NEW PrimitiveType DimExprs
    | NEW ClassType DimExprs Dims
    | NEW ClassType DimExprs
    '''
    

def p_DimExprs(p):
    '''
    DimExprs : DimExpr
    | DimExprs DimExpr
    '''
    

def p_DimExpr(p):
    '''
    DimExpr : L_SQBR Expression R_SQBR
    '''
    

def p_Dims(p):
    '''
    Dims : L_SQBR R_SQBR
    | Dims L_SQBR R_SQBR
    '''
    

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
    

def p_ArrayAccess(p):
    '''
    ArrayAccess : Name L_SQBR Expression R_SQBR
    | PrimaryNoNewArray L_SQBR Expression R_SQBR
    '''
    

def p_PostfixExpression(p):
    '''
    PostfixExpression : Primary
    | Name
    | PostIncrementExpression
    | PostDecrementExpression
    '''
    

def p_PostIncrementExpression(p):
    '''
    PostIncrementExpression : PostfixExpression INCREMENT
    '''
    

def p_PostDecrementExpression(p):
    '''
    PostDecrementExpression : PostfixExpression DECREMENT
    '''
    

def p_UnaryExpression(p):
    '''
    UnaryExpression : PreIncrementExpression
    | PreDecrementExpression
    | PLUS UnaryExpression
    | MINUS UnaryExpression
    | UnaryExpressionNotPlusMinus
    '''
    

def p_PreIncrementExpression(p):
    '''
    PreIncrementExpression : INCREMENT UnaryExpression
    '''
    

def p_PreDecrementExpression(p):
    '''
    PreDecrementExpression : DECREMENT UnaryExpression
    '''
    

def p_UnaryExpressionNotPlusMinus(p):
    '''
    UnaryExpressionNotPlusMinus : PostfixExpression
    | BITWISE_NOT UnaryExpression
    | LOGICAL_NOT UnaryExpression
    | CastExpression
    '''
    

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
    

def p_AdditiveExpression(p):
    '''
    AdditiveExpression : MultiplicativeExpression
    | AdditiveExpression PLUS MultiplicativeExpression
    | AdditiveExpression MINUS MultiplicativeExpression
    '''
    

def p_ShiftExpression(p):
    '''
    ShiftExpression : AdditiveExpression
    | ShiftExpression L_SHIFT AdditiveExpression
    | ShiftExpression R_SHIFT AdditiveExpression
    | ShiftExpression RR_SHIFT AdditiveExpression
    '''
    

def p_RelationalExpression(p):
    '''
    RelationalExpression : ShiftExpression
    | RelationalExpression LST ShiftExpression
    | RelationalExpression GRT ShiftExpression
    | RelationalExpression LEQ ShiftExpression
    | RelationalExpression GEQ ShiftExpression
    | RelationalExpression INSTANCEOF ReferenceType
    '''
    

def p_EqualityExpression(p):
    '''
    EqualityExpression : RelationalExpression
    | EqualityExpression EQUALS RelationalExpression
    | EqualityExpression NOT_EQUAL RelationalExpression
    '''
    

def p_AndExpression(p):
    '''
    AndExpression : EqualityExpression
    | AndExpression BITWISE_AND EqualityExpression
    '''
    

def p_ExclusiveOrExpression(p):
    '''
    ExclusiveOrExpression : AndExpression
    | ExclusiveOrExpression BITWISE_XOR AndExpression
    '''
    

def p_InclusiveOrExpression(p):
    '''
    InclusiveOrExpression : ExclusiveOrExpression
    | InclusiveOrExpression BITWISE_OR ExclusiveOrExpression
    '''
    

def p_ConditionalAndExpression(p):
    '''
    ConditionalAndExpression : InclusiveOrExpression
    | ConditionalAndExpression LOGICAL_AND InclusiveOrExpression
    '''
    

def p_ConditionalOrExpression(p):
    '''
    ConditionalOrExpression : ConditionalAndExpression
    | ConditionalOrExpression LOGICAL_OR ConditionalAndExpression
    '''
    

def p_ConditionalExpression(p):
    '''
    ConditionalExpression : ConditionalOrExpression
    | ConditionalOrExpression QMARK Expression COLON ConditionalExpression
    '''
    

def p_AssignmentExpression(p):
    '''
    AssignmentExpression : ConditionalExpression
    | Assignment
    '''
    

def p_Assignment(p):
    '''
    Assignment : LeftHandSide AssignmentOperator AssignmentExpression
    '''
    

def p_LeftHandSide(p):
    '''
    LeftHandSide : Name
    | FieldAccess
    | ArrayAccess
    '''
    

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
    '''
    
    #To check if I missed something

def p_Expression(p):
    '''
    Expression : AssignmentExpression
    '''


def p_ConstantExpression(p):
    '''
    ConstantExpression : Expression
    '''
    

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
