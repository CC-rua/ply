import yacc
from protoRule import tokens

def p_expression_defStruct(p):
    'expression : RIPROTO ID LPARAM term'
    p[0] = p[1] + p[3]