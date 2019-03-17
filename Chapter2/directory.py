# Functions Directory and Variable Table for Kotoba
# Stores all functions in a program
# Has two attributes: 
#    1. Key: String representing the Id of the program
#    2. Functions Table: Python Dictionary

class Directory():
    def __init__(self, id):
        self.id = id
        self.functions = {}
    
    def addFunction(self, functionName, returnType, memoryAddress):
        # Function data
        variables = {}

        # Array to store function attributes
        data = [returnType. variables, memoryAddress]

        # Add function to directory
        self.functions[functionName] = data

    def addVariable(self, functionName, varName, varType, varSize, varAddress):
        # Array to store variable attributes
        varData = [varType, varSize, varAddress]

        # Add variable to function's variable dictionary
        # key: FunctionName, 1: position 1 of functions data, varName: key for variables dictionary
        if varName in self.functions[functionName][1]:
            return False
        else:
            self.functions[functionName][1][varName] = varData
            return True


# class Variable:
#     def __init__(self, name, type, data):
#         self.name = name
#         self.type = type
#         self.data = data

# class Function:
#     def __init__(self, name, type, vars):
#         self.name = name
#         self.type = type
#         self.vars = vars

# class VariableTable(object):
#     def __init__(self, name, parent):
#         self.vars = {}
#         self.name = name
#         self.parent = parent

#     def add(self, var):
#         if self.vars.__contains__(var.name):
#             return False
#         else:
#             self.vars[var.name] = var
#             return True

#     def get(self, name):
#         if self.vars.__contains__(name):
#             return self.vars[name]
#         elif self.parent:
#             return self.parent.get(name)
#         else:
#             return None
        


