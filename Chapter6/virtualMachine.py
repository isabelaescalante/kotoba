import sys
import globalScope
from dataStruct import Quad


def execute_program():
    instruction_pointer = globalScope.quadCount -1

    while True:
        if globalScope.quads[instruction_pointer].getOperator() == "end":
            return "Execution Successful"

        current_quad = globalScope.quads[instruction_pointer]
        operator = current_quad.getOperator()

        if operator == "operator_add":
            arithmetic_operation("operator_add", current_quad)
            print("Add operation completed")
        elif operator == "operator_minus":
            arithmetic_operation("operator_minus", current_quad)
            print("Subtraction operation completed")
        elif operator == "operator_mult":
            arithmetic_operation("operator_mult", current_quad)
            print("Multiplication operation completed")
        elif operator == "operator_div":
            arithmetic_operation("operator_div", current_quad)
            print("Division operation completed")


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

    
    