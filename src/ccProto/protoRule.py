# 描述proto
# RiProto protoDemo{
#     Int number;
# }
from src.ccProto import lex

reserved = {
    'RIPROTO': 'RiProto',
    'INT': 'Int'
}

literals = ['+', '-', '*', '/', ';']

tokens = list(reserved.values()) + [
    'ID',  # id
    'LPARAM',  # {
    'RPARAM',  # }
]
t_LPARAM = r'\{'
t_RPARAM = r'\}'
t_ignore = ' \t'


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'Id')
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
    return t


sometext = '''
RiProto protoDemo{
    Int number;#123
}
'''
# 解析并读取
lexer = lex.lex()
lexer.input(sometext)
while 1:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
