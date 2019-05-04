import sys
import globalScope
from dataStruct import Quad


def execute_program():
    instruction_pointer = globalScope.instruction_pointer

    while True:
        current_quad = globalScope.quads[instruction_pointer]
        operator = current_quad.getOperator()

        if operator == "end":
            return "Execution Successful"
        elif operator == "operator_add":
            arithmetic_operation("operator_add", current_quad)
            instruction_pointer += 1
            print("Add operation completed")
        elif operator == "operator_minus":
            arithmetic_operation("operator_minus", current_quad)
            instruction_pointer += 1
            print("Subtraction operation completed")
        elif operator == "operator_mult":
            arithmetic_operation("operator_mult", current_quad)
            instruction_pointer += 1
            print("Multiplication operation completed")
        elif operator == "operator_div":
            arithmetic_operation("operator_div", current_quad)
            instruction_pointer += 1
            print("Division operation completed")
        elif operator == "operator_assign":
            assign_operation(current_quad)
            instruction_pointer += 1
            print("Assign operation completed")
        elif operator == "operator_greater":
            bi_relational_operation(operator, current_quad)
            instruction_pointer += 1
            print("Greater than operation completed")
        elif operator == "operator_less":
            bi_relational_operation(operator, current_quad)
            instruction_pointer += 1
            print("Less than operation completed")
        elif operator == "operator_equal":
            bi_relational_operation(operator, current_quad)
            instruction_pointer += 1
            print("Euqal to operation completed")
        elif operator == "operator_notequal":
            bi_relational_operation(operator, current_quad)
            instruction_pointer += 1
            print("Not equal to operation completed")
        elif operator == "operator_not":
            not_operation(current_quad)
            instruction_pointer += 1
            print("Not operation completed")
        elif operator == "operator_and":
            logical_operation(operator, current_quad)
            instruction_pointer += 1
            print("And operation completed")
        elif operator == "operator_or":
            logical_operation(operator, current_quad)
            instruction_pointer += 1
            print("Or operation completed")
        elif operator == "operator_print":
            print_operation(current_quad)
            instruction_pointer += 1
            print("Print operation completed")
        elif operator == "operator_read":
            read_operation(current_quad)
            instruction_pointer += 1
            print("Read operation completed")
        elif operator == "operator_goto":
            instruction_pointer = goto_operation(operator, current_quad)
            print("Goto operation completed")
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
            new_ip = 
        else:
            print("Did not find operator")
            

# Arithmetic Operations
def arithmetic_operation(operator, current_quad):
    left_op_address = current_quad.getLeftOperator()
    right_op_address = current_quad.getRightOperator()
    result_address = current_quad.getResult()

    left_value = globalScope.functionDirectory.getVarValue(left_op_address)
    right_value = globalScope.functionDirectory.getVarValue(right_op_address)

    print("Left value: " + str(left_value) + " Right value: " + str(right_value))

    if left_value == None or right_value == None:
        sys.exit("Variable has no value to perform arithmetic operation")

    if operator == "operator_add":
        result_value = float(left_value) + float(right_value)
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
        sys.exit("Variable has no value to perform realtional operation")
    
    if operator == "operator_greater":
        result_value = left_value > right_value
    elif operator == "operator_less":
        result_value = left_value < right_value
    elif operator == "operator_equal":
        result_value = left_value == right_value
    elif operator == "operator_notequal":
        result_value = left_value != right_value
    else:
        sys.exit("Error in relational operation")

    globalScope.functionDirectory.setVarValue(result_address, result_value)

# Not relational operation
def not_operation(current_quad):
    left_op_address = current_quad.getLeftOperator()
    result_address = current_quad.getResult()

    left_value = globalScope.functionDirectory.getVarValue(left_op_address)

    if left_value == None:
        sys.exit("Variable has no value to perform not operation")

    result_value = not left_value
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

    input_value = input()

    if id_type == "number":
        try:
            input_value = float(input_value)
            globalScope.functionDirectory.setVarValue(id_address, input_value)
        except:
            sys.exit("Wrong input for number")
    if id_type == "bool":
        if input_value == "true" or input_value == "false":
            globalScope.functionDirectory.setVarValue(id_address, input_value)
        else:
            sys.exit("Wrong input for bool")
    if id_type == "word":
        if !(' ' in input_value) :
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
        
        if not exp_value:
            return goto_jump
        else:
            return -1
    elif operator == "operator_gotoT":
        exp_address = current_quad.getLeftOperand()
        exp_value = globalScope.functionDirectory.getVarValue(exp_address)

        if exp_value == None:
            sys.exit("Variable has no value to be evaluated with")
        
        if exp_value:
            return goto_jump
        else:
            return -1

