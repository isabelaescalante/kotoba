import sys
import globalScope
from dataStruct import Quad
from dataStruct import Stack
from special import Word
from special import WordArray
from special import Sentence
from special import Numbers
from special import Array
from dataStruct import ActivationRecord
from memory import Memory


local_memory_handler = Stack()
current_function_name = Stack()
pending_return_value = Stack()
return_ip = Stack()
param_count = 0
printValues = []

def execute_program():
    instruction_pointer = globalScope.instruction_pointer
    
    while True:
        current_quad = globalScope.quads[instruction_pointer]
        operator = current_quad.getOperator()

        if operator == "end":
            print("")
            print("-----------------------------")
            print("-----------------------------")
            print("-----------------------------")
            print("-----------------------------")
            globalScope.functionDirectory.global_memory.print_Memory()
            print("-----------------------------")
            globalScope.functionDirectory.local_memory.print_Memory()
            print("-----------------------------")
            globalScope.functionDirectory.constant_memory.print_Memory()
            print("-----------------------------")
            print("Execution Successful")
            break
        elif operator == "operator_add":
            arithmetic_operation("operator_add", current_quad)
            instruction_pointer += 1
            #print("Add operation completed")
        elif operator == "operator_minus":
            arithmetic_operation("operator_minus", current_quad)
            instruction_pointer += 1
            #print("Subtraction operation completed")
        elif operator == "operator_mult":
            arithmetic_operation("operator_mult", current_quad)
            instruction_pointer += 1
            #print("Multiplication operation completed")
        elif operator == "operator_div":
            arithmetic_operation("operator_div", current_quad)
            instruction_pointer += 1
            #print("Division operation completed")
        elif operator == "operator_assign":
            assign_operation(current_quad)
            instruction_pointer += 1
            #print("Assign operation completed")
        elif operator == "operator_greater":
            bi_relational_operation(operator, current_quad)
            instruction_pointer += 1
            #print("Greater than operation completed")
        elif operator == "operator_less":
            bi_relational_operation(operator, current_quad)
            instruction_pointer += 1
            #print("Less than operation completed")
        elif operator == "operator_equal":
            bi_relational_operation(operator, current_quad)
            instruction_pointer += 1
            #print("Euqal to operation completed")
        elif operator == "operator_notequal":
            bi_relational_operation(operator, current_quad)
            instruction_pointer += 1
            #print("Not equal to operation completed")
        elif operator == "operator_not":
            not_operation(current_quad)
            instruction_pointer += 1
            #print("Not operation completed")
        elif operator == "operator_and":
            logical_operation(operator, current_quad)
            instruction_pointer += 1
            #print("And operation completed")
        elif operator == "operator_or":
            logical_operation(operator, current_quad)
            instruction_pointer += 1
            #print("Or operation completed")
        elif operator == "operator_print":
            print_operation(current_quad)
            instruction_pointer += 1
            #print("Print operation completed")
        elif operator == "operator_read":
            read_operation(current_quad)
            instruction_pointer += 1
            #print("Read operation completed")
        elif operator == "operator_goto":
            instruction_pointer = goto_operation(operator, current_quad)
            #print("Goto operation completed")
        elif operator == "operator_gotoF":
            new_ip = goto_operation(operator, current_quad)
            if new_ip == -1:
                instruction_pointer += 1
            else:
                instruction_pointer = new_ip
        elif operator == "operator_gotoT":
            new_ip = goto_operation(operator, current_quad)
            if new_ip == -1:
                instruction_pointer += 1
            else:
                instruction_pointer = new_ip
        elif operator == "operator_era":
            era_operation(current_quad)
            instruction_pointer += 1
            #print("Era operation completed")
        elif operator == "operator_param":
            param_operation(current_quad)
            instruction_pointer += 1
            #print("Param operation completed")
        elif operator == "operator_gosub":
            instruction_pointer = gosub_operation(current_quad, instruction_pointer)
            #print("Gosub operation completed")
        elif operator == "operator_return":
            instruction_pointer = return_operation(current_quad) 
            #print("Return operation completed")
        elif operator == "operator_verify" :
            verify_operation(current_quad, instruction_pointer)
            instruction_pointer += 1
            #print("Verification operation completed")
        elif operator == "operator_address" :
            address_operation(current_quad, instruction_pointer)
            instruction_pointer += 1
        elif operator == "operator_special":
            special_operation(current_quad)
            instruction_pointer += 1
        else:
            print("Did not find operator")


# Arithmetic Operations
def arithmetic_operation(operator, current_quad):
    left_op_address = current_quad.getLeftOperator()
    right_op_address = current_quad.getRightOperator()
    result_address = current_quad.getResult()

    left_value = globalScope.functionDirectory.getVarValue(left_op_address)
    right_value = globalScope.functionDirectory.getVarValue(right_op_address)

    # print("Left value: " + str(left_value) + " Right value: " + str(right_value))

    if left_value == None or right_value == None:
        sys.exit("Variable has no value to perform arithmetic operation")

    if operator == "operator_add":
        try:
            result_value = float(left_value) + float(right_value)
        except:
            result_value = left_value + right_value
            result_value = result_value.replace('""', ' ')

    elif operator == "operator_minus":
        result_value = float(left_value) - float(right_value)
    elif operator == "operator_mult":
        result_value = float(left_value) * float(right_value)
    elif operator == "operator_div":
        if right_value == 0:
            sys.exit("Unable to perform division by 0")
        else:
            result_value = float(left_value) / float(right_value)
    else:
        sys.exit("Error in arithmetic operation")

    globalScope.functionDirectory.setVarValue(result_address, result_value)


# Assign operation
def assign_operation(current_quad):
    address_to_assign = current_quad.getLeftOperator()
    id_address = current_quad.getResult()

    if '(' in str(address_to_assign) : 
        value_to_assign = pending_return_value.pop()

        if value_to_assign == None:
            sys.exit("No value to assign to")

        try: 
            len(value_to_assign) > 1
            for sublist in globalScope.arrayList:
                if(sublist[0] == id_address) :
                    var_size = sublist[1]
                    break
            if var_size < len(value_to_assign) :
                sys.exit("Variable size is smaller than result")
            else :
                for value in value_to_assign :
                    globalScope.functionDirectory.setVarValue(id_address, value)
                    id_address += 1
        except :
            globalScope.functionDirectory.setVarValue(id_address, value_to_assign)

    else : 
        value_to_assign = globalScope.functionDirectory.getVarValue(address_to_assign)
        if value_to_assign == None:
            sys.exit("No value to assign to")
        else :
            globalScope.functionDirectory.setVarValue(id_address, value_to_assign)

# Binary relational Operations
def bi_relational_operation(operator, current_quad):
    left_op_address = current_quad.getLeftOperator()
    right_op_address = current_quad.getRightOperator()
    result_address = current_quad.getResult()

    left_value = globalScope.functionDirectory.getVarValue(left_op_address)
    right_value = globalScope.functionDirectory.getVarValue(right_op_address)

    if left_value == None or right_value == None:
        sys.exit("Variable has no value to perform relational operation")

    if operator == "operator_greater":
        result_value = float(left_value) > float(right_value)
    elif operator == "operator_less":
        result_value = float(left_value) < float(right_value)
    elif operator == "operator_equal":
        try:
            result_value = float(left_value) == float(right_value)
        except:
            result_value = left_value == right_value
    elif operator == "operator_notequal":
        try:
            result_value = float(left_value) != float(right_value)
        except:
            result_value = left_value != right_value
    else:
        sys.exit("Error in relational operation")

    if result_value == True :
        result_value = "true"
    else :
        result_value = "false"

    globalScope.functionDirectory.setVarValue(result_address, result_value)

# Not relational operation
def not_operation(current_quad):
    left_op_address = current_quad.getLeftOperator()
    result_address = current_quad.getResult()

    left_value = globalScope.functionDirectory.getVarValue(left_op_address)

    if left_value == None:
        sys.exit("Variable has no value to perform not operation")

    if left_value == "true" :
        result_value = "false"
    else :
        result_value = "true"
    globalScope.functionDirectory.setVarValue(result_address, result_value)

# Logical Operations
def logical_operation(operator, current_quad):
    left_op_address = current_quad.getLeftOperator()
    right_op_address = current_quad.getRightOperator()
    result_address = current_quad.getResult()

    left_value = globalScope.functionDirectory.getVarValue(left_op_address)
    right_value = globalScope.functionDirectory.getVarValue(right_op_address)

    if left_value == None or right_value == None:
        sys.exit("Variable has no value to perform logical operation")

    if operator == "operator_and":
        result_value = left_value and right_value
    elif operator == "operator_or":
        result_value = left_value or right_value
    else:
        sys.exit("Error in logical operation")

    if result_value == True :
        result_value = "true"
    else :
        result_value = "false"

    globalScope.functionDirectory.setVarValue(result_address, result_value)

# Print operation
def print_operation(current_quad):
    id_address = current_quad.getLeftOperator()
    id_value = globalScope.functionDirectory.getVarValue(id_address)

    if id_value == None:
        sys.exit("Variable has no value to print")

    printValues.append(id_value)
    print(id_value)

# Read operation
def read_operation(current_quad):
    id_address = current_quad.getResult()
    id_value = globalScope.functionDirectory.getVarValue(id_address)
    id_type = current_quad.getLeftOperator()

    input_value = raw_input("Enter input: ")


    if id_type == "number":
        try:
            input_value = float(input_value)
            globalScope.functionDirectory.setVarValue(id_address, input_value)
        except :
            sys.exit("Wrong input for number")
    if id_type == "bool":
        try:
            if input_value == "true" or input_value == "false" : 
                globalScope.functionDirectory.setVarValue(id_address, input_value)
        except:
            sys.exit("Wrong input for bool")
    if id_type == "word":
        if not ' ' in input_value :
            globalScope.functionDirectory.setVarValue(id_address, input_value)
        else:
            sys.exit("Wrong input for word")
    if id_type == "sentence":
        if ' ' in input_value :
            globalScope.functionDirectory.setVarValue(id_address, input_value)
        else:
            sys.exit("Wrong input for sentence")

# Goto operations
def goto_operation(operator, current_quad):
    goto_jump = current_quad.getResult() - 1

    if operator == "operator_goto":
        return goto_jump
    elif operator == "operator_gotoF":
        exp_address = current_quad.getLeftOperator()
        exp_value = globalScope.functionDirectory.getVarValue(exp_address)

        if exp_value == None:
            sys.exit("Variable has no value to be evaluated with")

        if exp_value == "false":
            return goto_jump
        else:
            return -1
    elif operator == "operator_gotoT":
        exp_address = current_quad.getLeftOperator()
        exp_value = globalScope.functionDirectory.getVarValue(exp_address)

        if exp_value == None:
            sys.exit("Variable has no value to be evaluated with")


        if exp_value == "true":
            return goto_jump
        else:
            return -1

def era_operation(current_quad):
    current_function_name.push(current_quad.getResult())
    current_era = ActivationRecord(globalScope.functionDirectory.local_memory)
    local_memory_handler.push(current_era)

    # globalScope.functionDirectory.local_memory.clear_Memory()

    new_memory = Memory("Local/Temporal", 2000, 3999)
    new_era = ActivationRecord(new_memory)
    local_memory_handler.push(new_era)
    
    # print("PREVIOUS ERA:")
    # current_era.era_memory.print_Memory()
    # print("-----------------------------")
    

def param_operation(current_quad):
    global param_count
    param_address = current_quad.getLeftOperator()
    param_value = globalScope.functionDirectory.getVarValue(param_address)

    function_param_address = globalScope.functionDirectory.functions[current_function_name.top()][2][param_count][1]
    
    func_era = local_memory_handler.top()
    func_era.era_memory.set_AddressValue(function_param_address, param_value)

    # globalScope.functionDirectory.setVarValue(function_param_address, param_value)
    param_count += 1

def gosub_operation(current_quad, current_ip):
    global param_count
    return_ip.push(current_ip + 1)
    func_called = current_quad.getResult()
    param_count = 0

    new_era = local_memory_handler.top()
    globalScope.functionDirectory.local_memory = new_era.era_memory
    
    # print("ERA GOSUB")
    # new_era.era_memory.print_Memory()
    # print("-----------------------------")
    
    return globalScope.functionDirectory.getFuncQuadPosition(func_called) - 1

def return_operation(current_quad) :
    current_function_name.pop()
    
    return_value = globalScope.functionDirectory.getVarValue(current_quad.getResult())
    pending_return_value.push(return_value)
   
    # print("Return Value: " + str(return_value))
   
    new_ip = return_ip.pop()
    
    finished_era = local_memory_handler.pop()
    
    # print("ERA DONE:")
    # finished_era.era_memory.print_Memory()
    # print("-----------------------------")
    
    next_era = local_memory_handler.pop()
    
    # print("NEXT ERA:")
    # next_era.era_memory.print_Memory()
    # print("-----------------------------")
    
    globalScope.functionDirectory.local_memory = next_era.era_memory
    # globalScope.functionDirectory.local_memory.clear_Memory()

    return new_ip

def verify_operation(current_quad, instruction_pointer) :
    left_op_address = float(current_quad.getLeftOperator())
    right_op_address = float(current_quad.getRightOperator())
    result_address = current_quad.getResult()


    if float(result_address) > 999 :
        index_value = float(globalScope.functionDirectory.getVarValue(result_address))
        if index_value < left_op_address or index_value > right_op_address - 1 :
            sys.exit("Index value incorrect for variable of size " + str(right_op_address))
        else :
            globalScope.functionDirectory.setVarValue(globalScope.quads[instruction_pointer].result, index_value)


def address_operation(current_quad, instruction_pointer) :
    left_op_address = current_quad.getLeftOperator()
    right_op_address = current_quad.getRightOperator()
    result_address = current_quad.getResult() 
    
    if float(left_op_address) > 999 :
        left_value = float(globalScope.functionDirectory.getVarValue(left_op_address))
        result_val = left_value + float(right_op_address)
        result_pointer = globalScope.functionDirectory.getVarValue(result_val)
        globalScope.functionDirectory.constant_memory.set_AddressValue(result_address, result_pointer)
            

def special_operation(current_quad) :
    special_function = current_quad.getResult()
    var_used = current_quad.getLeftOperator()
    var_value = globalScope.functionDirectory.getVarValue(var_used)
    var_size = 0
    list_values = []
    if current_quad.getRightOperator() != "-1" :
        par_used = current_quad.getRightOperator()
        par_value = globalScope.functionDirectory.getVarValue(par_used)


    if special_function == "length" :
        if not ' ' in var_value and not float(var_value):
            word = Word()
            word.createWord(var_value)
            result = word.length()
            pending_return_value.push(result)
        else :
            sys.exit("Incorrect type of variable for function")
        
    elif special_function == "frequency" :
        if not ' ' in var_value :
            del list_values[:]
            for sublist in globalScope.arrayList:
                if(sublist[0] == var_used) :
                    var_size = sublist[1]
                    break
            current_address = var_used
            while current_address < var_size + var_used :
                var_value = globalScope.functionDirectory.getVarValue(current_address)
                list_values.append(var_value)
                current_address += 1
            
            wordArray = WordArray()
            wordArray.createArray(list_values)
            result = wordArray.frequency(par_value)
            pending_return_value.push(result) 
        else :
            sys.exit("Incorrect type of variable for function")      

    elif special_function == "search" :
        if not ' ' in var_value :
            del list_values[:]
            for sublist in globalScope.arrayList:
                if(sublist[0] == var_used) :
                    var_size = sublist[1]
                    break
            current_address = var_used
            while current_address < var_size + var_used :
                var_value = globalScope.functionDirectory.getVarValue(current_address)
                list_values.append(var_value)
                current_address += 1
            
            wordArray = WordArray()
            wordArray.createArray(list_values)
            result = wordArray.search(par_value) 
            pending_return_value.push(result)  
        else :
            sys.exit("Incorrect type of variable for function")

    elif special_function == "exists" :
        if not ' ' in var_value :
            del list_values[:]
            for sublist in globalScope.arrayList:
                if(sublist[0] == var_used) :
                    var_size = sublist[1]
                    break
            current_address = var_used
            while current_address < var_size + var_used :
                var_value = globalScope.functionDirectory.getVarValue(current_address)
                list_values.append(var_value)
                current_address += 1
            
            wordArray = WordArray()
            wordArray.createArray(list_values)
            result = wordArray.exists(par_value)  

            if result == True :
                result = "true"
            else :
                result = "false"

            pending_return_value.push(result)
        else :
            sys.exit("Incorrect type of variable for function")

    elif special_function == "sortWords" :
        if not ' ' in var_value :
            del list_values[:]
            for sublist in globalScope.arrayList:
                if(sublist[0] == var_used) :
                    var_size = sublist[1]
                    break
            current_address = var_used
            while current_address < var_size + var_used :
                var_value = globalScope.functionDirectory.getVarValue(current_address)
                list_values.append(var_value)
                current_address += 1
            
            wordArray = WordArray()
            wordArray.createArray(list_values)
            wordArray.sortWords()
            result = wordArray.wordArr

            current_address = var_used
            while current_address < var_size + var_used :
                for index in result :
                    globalScope.functionDirectory.setVarValue(current_address, index)
                    current_address += 1
        else :
            sys.exit("Incorrect type of variable for function")

    elif special_function == "wordCount" :
        if ' ' in var_value: 
            sentence = Sentence()
            sentence.createSentence(var_value)
            result = sentence.wordCount()

            pending_return_value.push(result)  
        else :
            sys.exit("Incorrect type of variable for function")          

    elif special_function == "tokenize" :
        if ' ' in var_value: 
            sentence = Sentence()
            sentence.createSentence(var_value)
            result = sentence.tokenize()

            pending_return_value.push(result)
        else :
            sys.exit("Incorrect type of variable for function")

    elif special_function == "remove" :
        if ' ' in var_value: 
            sentence = Sentence()
            sentence.createSentence(var_value)
            sentence.remove(par_value)
            result = sentence.sentence

            globalScope.functionDirectory.setVarValue(var_used, result)
        else :
            sys.exit("Incorrect type of variable for function")
    
    elif special_function == "mean" :
        if float(var_value) :
            del list_values[:]
            for sublist in globalScope.arrayList:
                if(sublist[0] == var_used) :
                    var_size = sublist[1]
                    break
            current_address = var_used
            while current_address < var_size + var_used :
                var_value = globalScope.functionDirectory.getVarValue(current_address)
                list_values.append(float(var_value))
                current_address += 1
                
            numArray = Numbers()
            numArray.createArray(list_values)
            result = numArray.mean()
            pending_return_value.push(result)
        else :
            sys.exit("Incorrect type of variable for function")
            
    elif special_function == "median" :
        if float(var_value) :
            del list_values[:]
            for sublist in globalScope.arrayList:
                if(sublist[0] == var_used) :
                    var_size = sublist[1]
                    break
            current_address = var_used
            while current_address < var_size + var_used :
                var_value = globalScope.functionDirectory.getVarValue(current_address)
                list_values.append(float(var_value))
                current_address += 1
               
            numArray = Numbers()
            numArray.createArray(list_values)
            result = numArray.median()
            pending_return_value.push(result)
        else :
            sys.exit("Incorrect type of variable for function")

    elif special_function == "mode" :
        if float(var_value) :
            del list_values[:]
            for sublist in globalScope.arrayList:
                if(sublist[0] == var_used) :
                    var_size = sublist[1]
                    break
            current_address = var_used
            while current_address < var_size + var_used :
                var_value = globalScope.functionDirectory.getVarValue(current_address)
                list_values.append(float(var_value))
                current_address += 1
                
            numArray = Numbers()
            numArray.createArray(list_values)
            result = numArray.mode()
            pending_return_value.push(result)
        else :
            sys.exit("Incorrect type of variable for function")

    elif special_function == "sortNumbers" :
        if float(var_value) :
            del list_values[:]
            for sublist in globalScope.arrayList:
                if(sublist[0] == var_used) :
                    var_size = sublist[1]
                    break
            current_address = var_used
            while current_address < var_size + var_used :
                var_value = globalScope.functionDirectory.getVarValue(current_address)
                list_values.append(float(var_value))
                current_address += 1
               
            numArray = Numbers()
            numArray.createArray(list_values)
            numArray.sortNumbers()
            result = numArray.numbers

            current_address = var_used
            while current_address < var_size + var_used :
                for index in result :
                    globalScope.functionDirectory.setVarValue(current_address, index)
                    current_address += 1
        else :
            sys.exit("Incorrect type of variable for function")

    elif special_function == "size" :
        del list_values[:]
        for sublist in globalScope.arrayList:
            if(sublist[0] == var_used) :
                var_size = sublist[1]
                break
        if var_size < 2 :
            sys.exit("Incorrect type of variable for function")

        current_address = var_used
        while current_address < var_size + var_used :
            var_value = globalScope.functionDirectory.getVarValue(current_address)
            list_values.append(var_value)
            current_address += 1

        array = Array()
        array.createArray(list_values)
        result = array.size()

        pending_return_value.push(result)
       

    else :
        sys.exit("Function " + special_function + " does not exist in language")

def finalVariables() :
    variables = []

    for varName in globalScope.functionDirectory.functions["Main"][1] :
        size = globalScope.functionDirectory.functions["Main"][1][varName][1]
        if size == 1 :
            data = globalScope.functionDirectory.functions["Main"][1][varName]
            value = globalScope.functionDirectory.getVarValue(data[2])
        else :
            i = 0
            values = []
            while i < size :
                data = globalScope.functionDirectory.functions["Main"][1][varName]
                values.append(globalScope.functionDirectory.getVarValue(data[2] + i))
                i += 1
            value = values
        if not value is None:
            variables.append([varName, value])

    return variables

