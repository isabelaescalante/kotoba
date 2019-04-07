from directory import Directory
from cube import Cube
from dataStruct import Stack
from dataStruct import Queue
from dataStruct import Quad

functionDirectory = Directory()
semanticCube = Cube()
functionName = ""
varName = ""
varType = ""
varSize = ""
quads = []
quadCount = 1
tempCount = 1
isVarFlag = True
pendingOperators = Stack()
pendingOperands = Stack()
pendingJumps = Stack()
operandTypes = Stack()
