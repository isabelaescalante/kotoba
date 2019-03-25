from directory import Directory
from cube import Cube
from dataStruct import Stack
from dataStruct import Queue
from dataStruct import Quad

functionDirectory = Directory()
semanticCube = Cube()
functionName = ""
varName = ""
varValue = []
varType = ""
varSize = ""
nextAddress = 100
quads = []
quadCount = 0
isVarFlag = True
pendingOperators = Stack()
pendingOperands = Stack()
operandTypes = Stack()