# Memory strucutre for Kotoba

class Memory:
    def __init__(self, name, initial_address, final_address):
        self.name = name
        self.number_memory = {} 
        self.word_memory = {}
        self.sentence_memory = {}
        self.bool_memory = {}

        # Address where memory starts and end, at least 400 slots (100 per data tyoe)
        self.initial_address = initial_address
        self.final_address = final_address

        # Number of slots per data type
        self.slots = (final_address - initial_address + 1)/4
        self.num_slot = initial_address
        self.word_slot = initial_address + self.slots
        self.sentence_slot = initial_address + (self.slots * 2)
        self.bool_slot = initial_address + (self.slots * 3)

        # Counters for memory [number, word, sentence, bool]
        self.variable_counter = [0,0,0,0]
        

    def get_nextAddress(self, varType):
        if varType is not None:
            if varType == "number":
                address = (self.num_slot + self.variable_counter[0])
                self.variable_counter[0] += 1
                self.set_AddressValue(address, -1) #initialize new address with -1
                return address
            
            if varType == "word":
                address = (self.word_slot + self.variable_counter[1])
                self.variable_counter[1] += 1
                self.set_AddressValue(address, -1) #initialize new address with -1
                return address

            if varType == "sentence":
                address = (self.sentence_slot + self.variable_counter[2])
                self.variable_counter[2] += 1
                self.set_AddressValue(address, -1) #initialize new address with -1
                return address

            if varType == "bool":
                address = (self.bool_slot + self.variable_counter[3])
                self.variable_counter[3] += 1
                self.set_AddressValue(address, -1) #initialize new address with -1
                return address
            
            else:
                return -1


    def set_AddressValue(self, address, varValue):
        # Number
        if address >= self.num_slot and address < self.word_slot: 
            self.number_memory[address] = varValue
        
        # Word
        if address >= self.word_slot and address < self.sentence_slot:
            self.word_memory[address] = varValue

        # Sentence
        if address >= self.sentence_slot and address < self.bool_slot:
            self.sentence_memory[address] = varValue

        # Bool
        if address >= self.bool_slot and address <= self.final_address:
            self.bool_memory[address] = varValue


    def get_ValueForAddress(self, address):
        if address >= self.initial_address and address < self.word_slot:
            if address in self.number_memory:
                return self.number_memory[address] 
        
        if address >= self.word_slot and address < self.sentence_slot:
            if address in self.word_memory:
                return self.word_memory[address] 

        if address >= self.sentence_slot and address < self.bool_slot:
            if address in self.sentence_memory:
                return self.sentence_memory[address] 

        if address >= self.bool_slot and address <= self.final_address:
           if address in self.bool_memory:
                return self.bool_memory[address] 

        return -1


    def get_AddressForConstant(self, cte):
        for address, value in self.number_memory.items():
            if value == cte:
                return address

        for address, value in self.word_memory.items():
            if value == cte:
                return address

        for address, value in self.sentence_memory.items():
            if value == cte:
                return address

        for address, value in self.bool_memory.items():
            if value == cte:
                return address

        return -1

    def clear_Memory(self):
        self.variable_counter[0] = 0
        self.variable_counter[1] = 0
        self.variable_counter[2] = 0
        self.variable_counter[3] = 0
        self.number_memory = {} 
        self.word_memory = {}
        self.sentence_memory = {}
        self.bool_memory = {}

    def print_Memory(self):
        print(self.name + " Memory")
        print("-----------------------------")
        print("Number: ")
        for key, value in self.number_memory.iteritems():
            print(key, value)
        
        print("Word: ")
        for key, value in self.word_memory.iteritems():
            print(key, value)

        print("Sentence: ")
        for key, value in self.sentence_memory.iteritems():
            print(key, value)

        print("Bool: ")
        for key, value in self.bool_memory.iteritems():
            print(key, value)
  

# #TEST
# mem = Memory("Global", 1000, 1999)

# #VARIABLES
# mem.set_AddressValue(mem.get_nextAddress("number"), 2)
# mem.set_AddressValue(mem.get_nextAddress("number"), 3)
# mem.set_AddressValue(mem.get_nextAddress("word"), "hola")
# mem.set_AddressValue(mem.get_nextAddress("word"), "hello")
# mem.set_AddressValue(mem.get_nextAddress("sentence"), "Como estas")
# mem.set_AddressValue(mem.get_nextAddress("bool"), True)

# mem.print_Memory()
# print("----------------------")

# # print(mem.get_ValueForAddress(1000))
# # print(mem.get_ValueForAddress(1001))

# #print(mem.get_AddressForConstant(10))







