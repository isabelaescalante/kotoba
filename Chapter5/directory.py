# Functions Directory and Variable Table for Kotoba
# Stores all functions in a program
# Has one attributes:
#    1. Functions Table: Python Dictionary
from memory import Memory

class Directory:
    def __init__(self):
        self.functions = {}
        self.memory = Memory(1000,1999)

    def addFunction(self, functionName, returnType, quadPosition):
        if functionName in self.functions:
            return False
        else:
            # Function data
            variables = {}
            # Array to store function attributes
            data = [returnType, variables, quadPosition]
            # Add function to directory
            self.functions[functionName] = data

            return True

    def getFuncQuadPosition(self, functionName):
        if functionName in self.functions :
            return self.functions[functionName][2]
        else:
            return None

    def setFuncQuadPosition(self, functionName, position):
        if functionName in self.functions :
            self.functions[functionName][2] = position

    def addVariable(self, functionName, varName, varType, varSize):
        if varName in self.functions[functionName][1]:
            return False
        else:
            varAddress = self.memory.get_nextAddress(varType)
            self.memory.set_AddressValue(varAddress, "pending")
            varData = [varType, varSize, varAddress]
            # Add variable to function's variable dictionary, key: FunctionName, 1: position 1 of functions data, varName: key for variables dictionary
            self.functions[functionName][1][varName] = varData            
            return True


    def varExists(self, functionName, varName):
        if varName in self.functions[functionName][1]:
            return True
        else:
            return False 

    def getVarType(self, functionName, varName):
        if self.varExists(functionName, varName) :
            return self.functions[functionName][1][varName][0]
        else:
            return None
    
    def getVarAddress(self, functionName, varName):
        if self.varExists(functionName, varName) :
            return self.functions[functionName][1][varName][2]
        else:
            return None

    def printDirectory(self):
        print("Function directory")
        for key in self.functions:
            print("FUNCTION: " + key)
            print("Return type: " + str(self.functions[key][0]))
            print("Quad position: " + str(self.functions[key][2]))
            for varKey in self.functions[key][1]:
                if(varKey) :
                    address = self.functions[key][1][varKey][2]
                    print("\tVARIABLE: " + varKey)
                    print("\tVar address: " + str(address))
                    print("\tVar type: " + str(self.functions[key][1][varKey][0]))
                    print("\tVar value: ") + str(self.memory.get_ValueForAddress(address))
                    print("\tVar size: " + str(self.functions[key][1][varKey][1]))

# if __name__ == '__main__':
#     dir = Directory()

#     dir.addFunction("func1", "void", 123)
#     dir.addVariable("func1", "x", "number", 1, 100)
#     dir.addVariableData("func1", "x", [12, 10])
#     dir.addVariable("func1", "example", "word", 1, 101)
#     dir.addFunction("func2", "number", 124)
#     dir.addVariable("func2", "y", "number", 1, 102)

#     dir.printDirectory()
