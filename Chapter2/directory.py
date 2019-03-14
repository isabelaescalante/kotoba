class Variable:
    def __init__(self, name, type, data):
        self.name = name
        self.type = type
        self.data = data

class Function:
    def __init__(self, name, type, vars):
        self.name = name
        self.type = type
        self.vars = vars

class VariableTable(object):
    def __init__(self, name, parent):
        self.vars = {}
        self.name = name
        self.parent = parent

    def add(self, var):
        if self.vars.__contains__(var.name):
            return False
        else:
            self.vars[var.name] = var
            return True

    def get(self, name):
        if self.vars.__contains__(name):
            return self.vars[name]
        elif self.parent:
            return self.parent.get(name)
        else:
            return None
        


