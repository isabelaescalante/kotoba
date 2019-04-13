import sys
import globalScope
from dataStruct import Quad


def execute_program():
    instruction_pointer = globalScope.quadCount -1

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


# Arithmetic Operations
def arithmetic_operation(operator, current_quad):
    left_op_address = current_quad.getLeftOperator()
    right_op_address = current_quad.getRightOperator()
    result_address = current_quad.getResult()

    left_value = globalScope.functionDirectory.getVarValue(left_op_address)
    right_value = globalScope.functionDirectory.getVarValue(right_op_address)

    if left_value == None or right_value == None:
        sys.exit("Variable has no value")

    if operator == "operator_add":
        result_value = left_value + right_value
    elif operator == "operator_minus":
        result_value = left_value + right_value
    elif operator == "operator_mult":
        result_value = left_value * right_value
    elif operator == "operator_div":
        if right_value == 0:
            sys.exit("Unable to perform division by 0")
        else:
            result_value = left_value / right_value
    else:
        sys.exit("Error in arithmetic operation")

    globalScope.functionDirectory.setVarValue(result_address, result_value)


# Assign operation
def assign_operation(current_quad):
    address_to_assign = current_quad.getLeftOperator()
    id_address = current_quad.getResult()

    if value_to_assign == None:
        sys.exit("No value to assign to")

    value_to_assign = globalScope.functionDirectory.getVarValue(address_to_assign)
    globalScope.functionDirectory.setVarValue(id_address, value_to_assign)
    
# Binary relational Operations
def bi_relational_operation(operator, current_quad):
    left_op_address = current_quad.getLeftOperator()
    right_op_address = current_quad.getRightOperator()
    result_address = current_quad.getResult()

    left_value = globalScope.functionDirectory.getVarValue(left_op_address)
    right_value = globalScope.functionDirectory.getVarValue(right_op_address)

    if left_value == None or right_value == None:
        sys.exit("Variable has no value")
    
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
        sys.exit("Variable has no value")

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
        sys.exit("Variable has no value")
    
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

    # PENDING ACTIONS

# Read operation
def read_operation(current_quad):
    id_address = current_quad.getResult()
    id_value = globalScope.functionDirectory.getVarValue(id_address)

    # PENDING ACTIONS