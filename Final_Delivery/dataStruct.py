# Data structures for Kotoba: Stack and Queue(using deque)
# March 15, 2019

from collections import deque
from memory import Memory

#Quadruple
class Quad:
    def __init__(self, op, leftOp, rightOp, res):
        self.operator = op
        self.leftOperator = leftOp
        self.rightOperator = rightOp
        self.result = res

    def getOperator(self):
        return self.operator

    def getLeftOperator(self):
        return self.leftOperator
    
    def getRightOperator(self):
        return self.rightOperator

    def getResult(self):
        return self.result

    def setResult(self, res):
        self.result = res

    def printQuad(self):
        print('{}, {}, {}, {}'.format(self.operator, self.leftOperator, self.rightOperator, self.result))

#Stack
class Stack:
    def __init__(self):
        self.items = []

    #Returns boolean specifying if stack is empty
    def isEmpty(self):
        return self.items == []

    #Removes all items of stack
    def empty(self):
        self.items[:] = []

    #Returns number of items in the stack
    def size(self):
        return len(self.items)

    #Adds item to the top of the stack
    def push(self, item):
        self.items.append(item)

    #Returns top item of the stack
    def top(self):
        return self.items[self.size()-1]

    #Returns and removes top item of the stack
    def pop(self):
        return self.items.pop()


#Queue
class Queue:
    def __init__(self):
        self.items = deque()

    #Returns boolean specifying if queue is empty
    def isEmpty(self):
        return self.items == []

    #Removes all items of stack
    def empty(self):
        self.items = []

    #Returns size of queue
    def size(self):
        return len(self.items)

    #Adds one element to queue
    def push(self, item):
        self.items.append(item)

    #Returns first item of the queue
    def first(self):
        return self.items[0]

    #Returns last item of the queue
    def last(self):
        return self.items[self.size()-1]

    #Returns and removes first element in the queue
    def pop(self):
        return self.items.popleft()

# Activation Record
class ActivationRecord:
    def __init__(self, func_memory):
        self.era_memory = func_memory #local memory for current function, type: Memory





# #TEST
# qu = Quad('operator_add',2,1,3)
# qu.printQuad()
# qu2 = Quad('operator_assign',2, "",'X')
# qu2.printQuad()
# qu3 = Quad('operator_read',"","",'Y')
# qu3.printQuad()

# s = Stack()
# s.push('cat')
# s.push('dog')
# print(s.size())
# print(s.isEmpty())
# print(s.top())
# print(s.pop())
# print(s.top())
# print(s.size())
# s.empty()
# print(s.size())

# print("--------------")

# q = Queue()
# q.push('apple')
# q.push('banana')
# print(q.size())
# print(q.isEmpty())
# print("First: " + q.first())
# print("Last: " + q.last())
# print(q.pop())
# print("First: " + q.first())
# print(q.size())
# q.empty()
# print(q.size())
