import lex
import yacc

# 描述算术 x = 3 + 42 * (s - t)

# 所有 token
tokens = [
    'ID',  # x
    'EQUALS',  # =
    'NUMBER',  # 3
    'PLUS',  # +
    'MINUS',  # -
    'TIMES',  # *
    'DIVIDE',  # /
    'LPARAM',  # (
    'RPARAM',  # )
]

# Token 的规则描述 t_xxx 命名 字符串前加r防止转义
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_LPARAM = r'\('
t_RPARAM = r'\)'


# 这里，紧跟在 t_ 后面的单词，必须跟标记列表中的某个标记名称对应。如果需要执行动作的话，规则可以写成一个方法。
# 例如，下面的规则匹配数字字串，并且将匹配的字符串转化成 Python 的整型
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_COMMENT(t):
    r'\#.*'
    pass


# 记录行号
def t_newLine(t):
    r'\n'
    t.lexer.lineno += len(t.value)
    return t


# 忽略空格和制表
t_ignore = ' \t'


# 忽略错误
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# 测试字符串
sometext = '''x = 3 + 42 * (s - t) # 123'''

# 解析并读取
lexer = lex.lex()
lexer.input(sometext)
while 1:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
