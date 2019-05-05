import sys
import globalScope
from dataStruct import Quad
from dataStruct import Stack

current_function_name = Stack()
pending_return_value = Stack()
return_ip = Stack()
param_count = 0

def execute_program():
    instruction_pointer = globalScope.instruction_pointer

    while True:
        current_quad = globalScope.quads[instruction_pointer]
        operator = current_quad.getOperator()

        if operator == "end":
            print("-----------------------------")
            globalScope.functionDirectory.global_memory.print_Memory()
            print("-----------------------------")
            globalScope.functionDirectory.local_memory.print_Memory()
            print("-----------------------------")
            globalScope.functionDirectory.constant_memory.print_Memory()
            print("-----------------------------")
            print("-----------------------------")
            print("-----------------------------")
            sys.exit("Execution Successful")
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
        elif operator == "operator_verify" or operator == "operator_address":
            instruction_pointer += 1
            #print("Verification operation completed")
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
    else : 
        value_to_assign = globalScope.functionDirectory.getVarValue(address_to_assign)

    if value_to_assign == None:
        sys.exit("No value to assign to")

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
        result_value = float(left_value) == float(right_value)
    elif operator == "operator_notequal":
        result_value = float(left_value) != float(right_value)
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

    print id_value

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

def param_operation(current_quad):
    global param_count
    param_address = current_quad.getLeftOperator()
    param_value = globalScope.functionDirectory.getVarValue(param_address)

    function_param_address = globalScope.functionDirectory.functions[current_function_name.top()][2][param_count][1]
    globalScope.functionDirectory.setVarValue(function_param_address, param_value)
    param_count += 1


def gosub_operation(current_quad, current_ip):
    global param_count
    return_ip.push(current_ip + 1)
    func_called = current_quad.getResult()
    param_count = 0

    print("fib quad " + str(globalScope.functionDirectory.getFuncQuadPosition(func_called) - 1))
    return globalScope.functionDirectory.getFuncQuadPosition(func_called) - 1

def return_operation(current_quad) :
    current_function_name.pop()

    return_value = globalScope.functionDirectory.getVarValue(current_quad.getResult())

    pending_return_value.push(return_value)
    new_ip = return_ip.pop()

    # globalScope.functionDirectory.local_memory.clear_Memory()

    return new_ip
