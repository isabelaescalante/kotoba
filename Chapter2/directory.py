# Functions Directory and Variable Table for Kotoba
# Stores all functions in a program
# Has one attributes:
#    1. Functions Table: Python Dictionary

class Directory():
    def __init__(self):
        self.functions = {}

    def addFunction(self, functionName, returnType, memoryAddress):
        if functionName in self.functions:
            return False
        else:
            # Function data
            variables = {}

            # Array to store function attributes
            data = [returnType, variables, memoryAddress]

            # Add function to directory
            self.functions[functionName] = data

            return True


    def addVariable(self, functionName, varName, varType, varSize, varAddress):
        if varName in self.functions[functionName][1]:
            return False
        else:
            # Array to store variable attributes
            varData = [varType, varSize, varAddress]

            # Add variable to function's variable dictionary, key: FunctionName, 1: position 1 of functions data, varName: key for variables dictionary
            self.functions[functionName][1][varName] = varData
            return True

    def printDirectory(self):
        print("Function directory")
        for key in self.functions:
            print("Function name: " + key)
            print("Return type: " + self.functions[key][0])
            print("Memory address: " + self.functions[key][2])
            print("Variables: ")
            for varKey in self.functions[key][1]:
                print("Var name: " + varKey)
                print("Var type: " + self.functions[key][1][varKey][0])
                print("Var size: " + self.functions[key][1][varKey][1])
                print("Var address: " + self.functions[key][1][varKey][2])

if __name__ == '__main__':
    dir = Directory()

    dir.addFunction("func1", "void", "123")
    dir.addVariable("func1", "x", "number", "1", "001")
    dir.addVariable("func1", "example", "word", "1", "002")
    dir.addFunction("func2", "number", "124")
    dir.addVariable("func2", "y", "number", "1", "003")
    dir.addFunction("func1", "number", "125")

    dir.printDirectory()