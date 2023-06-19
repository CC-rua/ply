import ply.lex as lex
import ply.yacc as yacc
import protoRule
from protoStruct import ProtoStruct
from protoStruct import Field
from protoRule import tokens

structNameSet = []
structList = []


def p_protoList(p):
    """
    protoList : proto
              | protoList proto
    """
    pass


def p_proto(p):
    """
    proto : struct LPARAM fieldList RPARAM
          | struct order LPARAM fieldList RPARAM
    """
    struct = ProtoStruct()
    struct.name = p[1]
    if len(p) == 5:
        struct.fieldList = p[3]
    if len(p) == 6:
        struct.mainOrder = p[2][0]
        struct.subOrder = p[2][1]
        struct.fieldList = p[4]
    structList.append(struct)


def p_struct(p):
    """
    struct : RIPROTO ID
    """
    structNameSet.append(p[2])
    p[0] = p[2]


def p_order(p):
    """
    order : LBRACKET ORDERID ',' ORDERID RBRACKET
    """
    p[0] = [p[2], p[4]]


def p_type(p):
    """
    type : INT
         | BOOL
    """
    p[0] = p[1]


def p_field(p):
    """
    field : type ID ';'
    """
    filed = Field()
    filed.type = p[1]
    filed.name = p[2]
    p[0] = filed


def p_innerStruct(p):
    """
    field : ID ID ';'
    """
    if not structNameSet.__contains__(p[1]):
        print("inner struct not found ", p[1])
        return
    filed = Field()
    filed.type = p[1]
    filed.name = p[2]
    p[0] = filed


def p_fieldList(p):
    """
    fieldList : field
              | fieldList field
    """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]


def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")


parser = yacc.yacc()
parser.parse(protoRule.sometext)

print(structNameSet)
print("structList:", structList)
