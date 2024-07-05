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
    type = None
    name = ''
    is_array = False

    def __int__(self):
        self.type = None
        self.name = ''
        self.is_array = False

    def __str__(self):
        return f"[{self.type},{self.name},{self.is_array}]"

    def __repr__(self):
        return f"[{self.type},{self.name},{self.is_array}]"
