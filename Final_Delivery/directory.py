# Functions Directory and Variable Table for Kotoba
# Stores all functions in a program
# Has one attributes:
#    1. Functions Table: Python Dictionary
from memory import Memory

class Directory:
    def __init__(self):
        self.functions = {}
        self.global_memory = Memory("Global", 1000, 1999) # 1000 slots
        self.local_memory = Memory("Local/Temporal", 2000, 3999) # 2000 slots
        self.constant_memory = Memory("Constant", 4000, 4999) # 1000 slots

    def addFunction(self, functionName, returnType, quadPosition):
        if functionName in self.functions:
            return False
        else:
            # Function data
            variables = {}
            parameters = []
            # Array to store function attributes
            data = [returnType, variables, parameters, quadPosition]
            # Add function to directory
            self.functions[functionName] = data

            return True

    def getFuncQuadPosition(self, functionName):
        if functionName in self.functions :
            return self.functions[functionName][3]
        else:
            return None

    def setFuncQuadPosition(self, functionName, position):
        if functionName in self.functions :
            self.functions[functionName][3] = position

    def addVariable(self, functionName, varName, varType, varSize):
        if varName in self.functions[functionName][1]:
            return False
        else:
            if functionName == "Main":
                varAddress = self.global_memory.get_nextAddress(varType)
                if varSize > 1:
                    for i in range(varSize-1):
                        self.global_memory.reserve_ListAddress(varType)

            else:
                varAddress = self.local_memory.get_nextAddress(varType)
                if varSize > 1:
                    for i in range(varSize-1):
                        self.local_memory.reserve_ListAddress(varType)

            varData = [varType, varSize, varAddress]
            # Add variable to function's variable dictionary, key: FunctionName, 1: position 1 of functions data, varName: key for variables dictionary
            self.functions[functionName][1][varName] = varData

            return True

    def addParameter(self, functionName, varType):
        self.functions[functionName][2].append(varType)            
        return True

    def varExists(self, functionName, varName):
        if varName in self.functions[functionName][1]:
            return True
        else:
            return False 

    def functionExists(self, functionName):
        if functionName in self.functions:
            return True
        else:
            return False 
    
    def functionType(self, functionName) :
        if self.functionExists(functionName) :
            return self.functions[functionName][0]
        else:
            return None    

    def getVarType(self, functionName, varName):
        return self.functions[functionName][1][varName][0]
    
    def getVarAddress(self, functionName, varName):
        return self.functions[functionName][1][varName][2]

    def getVarSize(self, functionName, varName):
        return self.functions[functionName][1][varName][1]
        
    def getVarValue(self, varAddress):
        if varAddress >= 1000 and varAddress < 2000:
            return self.global_memory.get_ValueForAddress(varAddress)
        elif varAddress >= 2000 and varAddress < 4000:
            return self.local_memory.get_ValueForAddress(varAddress)
        elif varAddress >= 4000 and varAddress < 5000:
            return self.constant_memory.get_ValueForAddress(varAddress)

    def setVarValue(self, varAddress, varValue):
        if varAddress >= 1000 and varAddress < 2000:
            return self.global_memory.set_AddressValue(varAddress, varValue)
        elif varAddress >= 2000 and varAddress < 4000:
            return self.local_memory.set_AddressValue(varAddress, varValue)

    def printDirectory(self):
        print("Function directory")
        for key in self.functions:
            print("FUNCTION: " + key)
            print("Return type: " + str(self.functions[key][0]))
            print("Quad position: " + str(self.functions[key][3]))
            for varKey in self.functions[key][1]:
                if(varKey) :
                    address = self.functions[key][1][varKey][2]
                    print("\tVARIABLE: " + varKey)
                    print("\tVar address: " + str(address))
                    print("\tVar type: " + str(self.functions[key][1][varKey][0]))
                    print("\tVar value: " + str(self.global_memory.get_ValueForAddress(address)))
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
