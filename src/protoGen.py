from protoStruct import ProtoStruct

CLASS_NAME = r'${CLASS_NAME}'
FILED = r'${FILED}'
PROTO_LENGTH = r'${PROTO_LENGTH}'
JAVA_CLASS_TEMPLATE_FILE_PATH = '/home/cc/file/project/ply/src/JAVAClassTemplate.java'
JAVA_TYPE_BYTE_LENGTH_DIC = {
    'byte': 1,
    'short': 2,
    'int': 4,
    'long': 8,
    'float': 4,
    'double': 8,
    'boolean': 1,
    'char': 2,
}


def genFiled(ps):
    content = ''
    for filed in ps.fieldList:
        if filed is not None:
            content += "\tpublic " + filed.type + " " + filed.name + ';\n'
    return content


def genClassName(ps):
    return ps.name


def calProtoLen(ps):
    content = ''
    primitiveLen = 0
    for filed in ps.fieldList:
        if filed is not None:
            if JAVA_TYPE_BYTE_LENGTH_DIC[filed.type] is not None:
                primitiveLen += JAVA_TYPE_BYTE_LENGTH_DIC[filed.type]
            else:
                content += "sizeof("


def genProto(ps):
    # 打开文件
    file = open(JAVA_CLASS_TEMPLATE_FILE_PATH, "r")  # 使用 "r" 参数表示以只读方式打开文件
    # 读取文件内容
    content = file.read()
    # 关闭文件
    file.close()
    # 替换
    content = content.replace(CLASS_NAME, genClassName(ps))
    content = content.replace(FILED, genFiled(ps))
    content = content.replace(PROTO_LENGTH, calProtoLen(ps))
    # 打印文件内容
    print(content)
