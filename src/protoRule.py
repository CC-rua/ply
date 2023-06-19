# 描述proto
# RiProto protoDemo{
#     Int number;
# }
from ply import lex

reserved = {
    'RiProto': 'RIPROTO',
    'Int': 'INT',
    'bool': 'BOOL'
}

literals = ['+', '-', '*', '/', ';', ',']

tokens = list(reserved.values()) + [
    'ID',  # id
    'ORDERID',  # id
    'LPARAM',  # {
    'RPARAM',  # }
    'LBRACKET',  # <
    'RBRACKET',  # <
]
t_LPARAM = r'\{'
t_RPARAM = r'\}'
t_LBRACKET = r'\<'
t_RBRACKET = r'\>'
t_ignore = ' \t'


# 协议号
def t_ORDERID(t):
    r'[0-9]{1,3}'
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t


def t_comment(t):
    r'\#.*'
    pass


# 忽略错误
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# 记录行号
def t_newline(t):
    r'\n'
    t.lexer.lineno += len(t.value)
    pass


sometext = '''RiProto protoDemo <10,999> {
Int number;
bool isBool;
protoDeamo pd;
}'''
# 解析并读取
lexer = lex.lex()
lexer.input(sometext)
while 1:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
