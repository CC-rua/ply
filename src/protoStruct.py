class ProtoStruct:
    def __int__(self):
        self.name = ''
        self.mainOrder = 0
        self.subOrder = 0
        self.fieldList = []

    def __str__(self):
        return f"<{self.mainOrder},{self.subOrder}>:{self.fieldList}"

    def __repr__(self):
        return f"\n{self.name} <{self.mainOrder},{self.subOrder}>:{self.fieldList}"


class Field:
    def __int__(self):
        self.type = None
        self.name = ''

    def __str__(self):
        return f"[{self.type},{self.name}]"

    def __repr__(self):
        return f"[{self.type},{self.name}]"
