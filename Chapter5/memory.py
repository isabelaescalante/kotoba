# Memory strucutre for Kotoba

class Memory:
    def __init__(self):
        # Dictionaries [{number}, {word}, {sentence}, {bool}]
        # Key: address Value: var value
        self.variable_memory = [{}, {}, {}, {}]
        self.constant_memory = [{}, {}, {}, {}]
        # Counters for memory [number, word, sentence, bool]
        self.variable_counter = [0,0,0,0]
        self.constant_counter = [0,0,0,0]

    def get_VarAddress(self, varType):
        if varType is not None:
            if varType == "number":
                address = (100+self.variable_counter[0])
                self.variable_counter[0] += 1
                return address
            
            if varType == "word":
                address = (200+self.variable_counter[1])
                self.variable_counter[1] += 1
                return address

            if varType == "sentence":
                address = (300+self.variable_counter[2])
                self.variable_counter[2] += 1
                return address

            if varType == "bool":
                address = (400+self.variable_counter[3])
                self.variable_counter[3] += 1
                return address
            
            else:
                return -1

    def get_ConstantAddress(self, varType):
        if varType is not None:
            if varType == "number":
                address = (500+self.constant_counter[0])
                self.constant_counter[0] += 1
                return address
            
            if varType == "word":
                address = (600+self.constant_counter[1])
                self.constant_counter[1] += 1
                return address

            if varType == "sentence":
                address = (700+self.constant_counter[2])
                self.constant_counter[2] += 1
                return address

            if varType == "bool":
                address = (800+self.constant_counter[3])
                self.constant_counter[3] += 1
                return address
            
            else:
                return -1


    def set_VarValue(self, address, varValue):
        # Number
        if address > 99 and address < 200: 
            self.variable_memory[0][address] = varValue
        
        # Word
        if address > 199 and address < 300:
            self.variable_memory[1][address] = varValue

        # Sentence
        if address > 299 and address < 400:
            self.variable_memory[2][address] = varValue

        # Bool
        if address > 399 and address < 500:
            self.variable_memory[3][address] = varValue

    def set_ConstantValue(self, address, varValue):
        # Number Constant
        if address > 499 and address < 600: 
            self.constant_memory[0][address] = varValue
        
        # Word Constant
        if address > 599 and address < 700:
            self.constant_memory[1][address] = varValue

        # Sentence Constant
        if address > 699 and address < 800:
            self.constant_memory[2][address] = varValue

        # Bool Constant
        if address > 799 and address < 900:
            self.constant_memory[3][address] = varValue


    def get_ValueForAddress(self, address):
        # Variables
        if address > 99 and address < 200: 
            if (address - self.variable_counter[0]) < 100:
                return self.variable_memory[0][address]
            else:
                return None
        
        if address > 199 and address < 300:
            if (address - self.variable_counter[1]) < 200:
                return self.variable_memory[1][address]
            else:
                return None
        if address > 299 and address < 400:
            if (address - self.variable_counter[2]) < 300:
                return self.variable_memory[2][address]
            else:
                return None

        if address > 399 and address < 500:
            if (address - self.variable_counter[3]) < 400:
                return self.variable_memory[3][address]
            else:
                return None

        # Constants
        if address > 499 and address < 600: 
            if (address - self.constant_counter[0]) < 500:
                return self.constant_memory[0][address]
            else:
                return None
    
        if address > 599 and address < 700:
            if (address - self.constant_counter[1]) < 600:
                return self.constant_memory[1][address]
            else:
                return None

        if address > 699 and address < 800:
            if (address - self.constant_counter[2]) < 700:
                return self.constant_memory[2][address]
            else:
                return None

        if address > 799 and address < 900:
            if (address - self.constant_counter[3]) < 800:
                return self.constant_memory[3][address]
            else:
                return None
        
        else:
            return -1
    
    

    def print_Variables(self):
        print("Number Variables: ")
        for key, value in self.variable_memory[0].iteritems():
            print(key, value)
        
        print("Word Variables: ")
        for key, value in self.variable_memory[1].iteritems():
            print(key, value)

        print("Sentence Variables: ")
        for key, value in self.variable_memory[2].iteritems():
            print(key, value)

        print("Bool Variables: ")
        for key, value in self.variable_memory[3].iteritems():
            print(key, value)
    
    def print_Constants(self):
        print("Number Constants: ")
        for key, value in self.constant_memory[0].iteritems():
            print(key, value)
        
        print("Word Constants: ")
        for key, value in self.constant_memory[1].iteritems():
            print(key, value)

        print("Sentence Constants: ")
        for key, value in self.constant_memory[2].iteritems():
            print(key, value)

        print("Bool Constants: ")
        for key, value in self.constant_memory[3].iteritems():
            print(key, value)

# #TEST
# mem = Memory()

# #VARIABLES
# mem.set_VarValue(mem.get_VarAddress("number"), 2)
# mem.set_VarValue(mem.get_VarAddress("number"), 3)
# mem.set_VarValue(mem.get_VarAddress("word"), "hola")
# mem.set_VarValue(mem.get_VarAddress("word"), "hello")
# mem.set_VarValue(mem.get_VarAddress("sentence"), "Como estas")
# mem.set_VarValue(mem.get_VarAddress("bool"), True)
# #CONSTANTS
# mem.set_ConstantValue(mem.get_ConstantAddress("number"), 3)
# mem.set_ConstantValue(mem.get_ConstantAddress("word"), "HOLA")
# mem.set_ConstantValue(mem.get_ConstantAddress("sentence"), "COMO ESTAS")
# mem.set_ConstantValue(mem.get_ConstantAddress("bool"), False)

# mem.print_Variables()
# print("----------------------")
# mem.print_Constants()

# print(mem.get_ValueForAddress(100))
# print(mem.get_ValueForAddress(101))









