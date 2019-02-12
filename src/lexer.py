import ply.lex as lex
import argparse
import sys

# parser = argparse.ArgumentParser()
# parser.add_argument("--cfg", help="color config file", type=str)
# parser.add_argument("--output", help="HTML file")
# args = vars(parser.parse_args())
# print(args['cfg'])
# print(args['output'])
cconfig = sys.argv[1]
cconfig = cconfig[6:]
outfile = sys.argv[3]
outfile = outfile[9:]
infile = sys.argv[2]

keywords = ['abstract','assert','boolean','break','byte','case','catch','char','class','const','continue',
			'default','do','double','else','enum','extends','final','finally','float','for','goto','if',
			'implements','import','instanceof','int','interface','long','native','new','package',
			'private','protected','public','return','short','static','strictfp','super','switch',
			'synchronized','this','throw','throws','transient','try','void','volatile','while'
			]



tokens = [

 				'EQUALS',
                'ASSIGN',
                'GRT',
                'LST',
                'GEQ',
                'LEQ',
				'QMARK',
				'COLON',
				'AT',
                'PLUS',
                'MINUS',
                'MULT',
                'DIVIDE',
                'LOGICAL_AND',
                'LOGICAL_OR',
                'LOGICAL_NOT',
                'NOT_EQUAL',
                'BITWISE_AND',
                'BITWISE_OR',
                'BITWISE_NOT',
                'BITWISE_XOR',
                'MODULO',
                'INCREMENT',
                'DECREMENT',
                'DOT',
                'PLUS_ASSIGN',
                'MINUS_ASSIGN',
                'MULT_ASSIGN',
                'DIVIDE_ASSIGN',
                'MOD_ASSIGN',
                'L_SHIFT',
                'R_SHIFT',
                'RR_SHIFT',
                'LSHIFT_ASSIGN',
                'RSHIFT_ASSIGN',
                'RRSHIFT_ASSIGN',


                'STMT_TERMINATOR',
                'COMMA',
                'L_ROUNDBR',
                'R_ROUNDBR',
                'L_CURLYBR',
                'R_CURLYBR',
                'L_SQBR',
                'R_SQBR',

                'IDENTIFIER',
                'INT_LITERAL',
                'FLOAT_LITERAL',
                'CHAR_LITERAL',
                'STRING_LITERAL',
                'LINE_COMMENT',
                'BLOCK_COMMENT',
                #'UNMATCHED'
		] + [k.upper() for k in keywords]



def t_FLOAT_LITERAL(t):
        r'[+-]?([0-9]+([.][0-9]*)?|[.][0-9]+)'
        #t.value = float(t.value)
        return t


def t_INT_LITERAL(t):
		r'[+-]?\d+'
		#t.value = int(t.value);
		return t;


t_STRING_LITERAL = r'\"([^\\\n]|(\\.))*?\"'
t_CHAR_LITERAL =  r"\'([^\\\n]|(\\.))?\'"

t_STMT_TERMINATOR = r';'
t_COMMA = r','
t_L_ROUNDBR = r'\('
t_R_ROUNDBR = r'\)'
t_L_CURLYBR = r'\{'
t_R_CURLYBR = r'\}'
t_L_SQBR = r'\['
t_R_SQBR = r'\]'

t_QMARK = r'\?'
t_AT = r'@'
t_COLON = r':'
t_EQUALS = r'=='
t_ASSIGN = r'='
t_GRT = r'>'
t_LST = r'<'
t_GEQ = r'>='
t_LEQ = r'<='
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULT = r'\*'
t_DIVIDE = r'/'
t_LOGICAL_AND = r'&&'
t_LOGICAL_OR = r'\|\|'
t_LOGICAL_NOT = r'!'
t_NOT_EQUAL = r'!='
t_BITWISE_AND = r'&'
t_BITWISE_OR = r'\|'
t_BITWISE_NOT = r'~'
t_BITWISE_XOR = r'\^'
t_MODULO = r'%'
t_INCREMENT = r'\+\+'
t_DECREMENT = r'\-\-'
t_DOT = r'\.'
t_PLUS_ASSIGN = r'\+= '
t_MINUS_ASSIGN = r'-='
t_MULT_ASSIGN = r'\*='
t_DIVIDE_ASSIGN = r'/='
t_MOD_ASSIGN = r'%='
t_L_SHIFT = r'<<'
t_R_SHIFT = r'>>'
t_RR_SHIFT = r'>>>'
t_LSHIFT_ASSIGN = r'<<='
t_RSHIFT_ASSIGN = r'>>='
t_RRSHIFT_ASSIGN = r'>>>='

t_ignore = ' \t'


def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in keywords:
        t.type = t.value.upper()
    return t



t_LINE_COMMENT = r'//.*'

def t_BLOCK_COMMENT(t):
        r'/\*(.|\n)*?\*/'
        t.lexer.lineno += t.value.count('\n')
        return t

def t_newline(t):
        r'\n+'
        t.lexer.lineno += len(t.value)
#t_UNMATCHED = r'.+'
def t_error(t):
        print("Character does not fit into any token '%s'" % t.value[0])
        t.lexer.skip(1)

lexer = lex.lex()
colors = {}
with open(cconfig) as f:
    for line in f:
       (key, val) = line.split()
       colors[key] = val
#print(colors)
inp = open(infile,"r").read();
#print(inp)
lexer.input(inp);
html = "<html>"
current_line = 1;
current_pos = 0;
while True:
        tok = lexer.token()
        if not tok:
                break;
        color = 'black'
        if(tok.type in [k.upper() for k in keywords]):
                color = colors['keywords']
        elif(tok.type in colors.keys()):
                color = colors[tok.type]
        #print(tok,color)

        if(tok.lineno > current_line):
                html+=("<br>"*(tok.lineno - current_line))
                current_pos+=(tok.lineno-current_line)
                current_line=tok.lineno


        if(tok.lexpos > current_pos):
                html+=("&nbsp;"*(tok.lexpos-current_pos))
                current_pos = tok.lexpos

        if(str(tok.type) == "BLOCK_COMMENT"):
                html+="<font color="+color+">"
                l = tok.value.split("\n")
                for x in l:
                        html+=x
                        html+="<br>"
                        current_line+=1
                        #current_pos+=1
                html+="</font>"
        else:
                html+="<font color="+color+">"+str(tok.value)+"</font>"


        current_pos+=len(str(tok.value))

html+="</html>"
out= open(outfile,'w')
out.write(html)
out.close()
