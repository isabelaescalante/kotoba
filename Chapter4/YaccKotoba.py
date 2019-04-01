import ply.yacc as yacc
import LexKotoba
import globalScope
import sys

from dataStruct import Quad

tokens = LexKotoba.tokens

def p_start(p) :
	'''start : KOTOBA ID func_start ENDSTMT declare startaux BEGIN func_begin_main block END
	| KOTOBA ID func_start ENDSTMT startaux BEGIN func_begin_main block END'''
	print("Compilation succeeded")
	# print(globalScope.functionDirectory.printDirectory())
	
	print("My quads are: ")
	for quad in globalScope.quads:
		quad.printQuad()

def p_startaux(p) :
	'''startaux : function startaux
	| empty'''

def p_block(p) :
	'''block : OPENCURL blockaux CLOSECURL'''

def p_blockaux(p) :
	'''blockaux : action blockaux
	| empty'''

def p_action(p) :
	'''action : input
	| output
	| statement'''

def p_input(p) :
	'''input : READ OPENPAREN ID func_read CLOSEPAREN ENDSTMT'''
	print("input " + str(globalScope.quadCount))

def p_output(p) :
	'''output : WRITE OPENPAREN outputaux CLOSEPAREN ENDSTMT'''

def p_outputaux(p) :
	'''outputaux : expression func_print
	| expression func_print COMA outputaux'''

def p_declare(p) :
	'''declare : DEC decaux'''

def p_decaux(p) :
	'''decaux : type ID func_declare_var declareaux
	| type ID OPENBRAC func_isSize cte CLOSEBRAC func_declare_array declareaux'''

def p_declareaux(p) :
	'''declareaux : ENDSTMT
	| COMA decaux'''

def p_assign(p) :
	'''assign : ID func_constantID EQUAL func_assign assignaux
	| ID func_constantID OPENBRAC func_isSize cte CLOSEBRAC EQUAL assignaux'''

def p_assignaux(p) :
	'''assignaux : exp func_assign_value ENDSTMT
	| OPENCURL assiaux CLOSECURL ENDSTMT'''

def p_assiaux(p) :
	'''assiaux : exp
	| exp COMA assiaux'''

def p_cte(p) :
	'''cte : ID func_constantID
	| BOOLCTE func_constant func_boolCte
	| NUMBERCTE func_constant func_numberCte
	| WORDCTE func_constant func_wordCte
	| SENTENCECTE func_constant func_sentenceCte''' 

def p_type(p) :
	'''type : BOOL func_type
	| NUMBER func_type
	| WORD func_type
	| SENTENCE func_type'''

def p_statement(p) :
	'''statement : assign
	| expression
	| condition
	| cycle
	| callfunction'''

def p_expression(p) :
	'''expression : logexpression
	| NOT func_logicOp_operation logexpression func_logicOP'''

def p_logexpression(p) :
	'''logexpression : relopexpression 
	| relopexpression AND func_logicOp_operation logexpression func_logicOP
	| relopexpression OR func_logicOp_operation logexpression func_logicOP'''

def p_relopexression(p) :
	'''relopexpression : exp 
	| exp func_relop RELOP func_relop_operation exp func_relop'''

def p_exp(p) :
	'''exp : term
	| term PLUS func_term_operation exp func_term
	| term MINUS func_term_operation exp func_term'''

def p_term(p) :
	'''term : factor
	| factor MULT func_factor_operation term func_factor
	| factor DIV func_factor_operation term func_factor'''

def p_factor(p) :
	'''factor : OPENPAREN expression CLOSEPAREN
	| cte'''

def p_condition(p) :
	'''condition : IF OPENPAREN expression CLOSEPAREN func_if block func_endIf 
	|  IF OPENPAREN expression CLOSEPAREN func_if block func_endIf ELSE func_else block func_endIf'''

def p_cycle(p) :
	'''cycle : WHILE OPENPAREN expression CLOSEPAREN block
	| DO block WHILE OPENPAREN expression CLOSEPAREN ENDSTMT'''

def p_function(p) :
	'''function : FUNC funcaux ID func_declare_function OPENPAREN parameter CLOSEPAREN OPENCURL declare blockaux returnaux ENDSTMT CLOSECURL func_clear
	| FUNC funcaux ID func_declare_function OPENPAREN parameter CLOSEPAREN OPENCURL blockaux returnaux ENDSTMT CLOSECURL func_clear'''

def p_funcaux(p) :
	'''funcaux : type
	| VOID'''

def p_parameter(p) :
	'''parameter : type ID func_declare_var parameteraux
	| type ID OPENBRAC func_isSize cte CLOSEBRAC func_declare_array parameteraux'''

def p_parameteraux(p) :
	'''parameteraux : COMA parameter
	| empty'''

def p_returnaux(p) :
	'''returnaux : RETURN ID
	| empty'''

def p_callfunction(p) :
	'''callfunction : ID callaux OPENPAREN spaux CLOSEPAREN ENDSTMT'''

def p_callaux(p) :
	'''callaux : DOT special
	| empty'''

def p_spaux(p) :
	'''spaux : cte
	| cte COMA spaux
	| empty'''

def p_special(p) :
	'''special : LENGTH  
	| FREQUENCY
    | SEARCH
    | EXISTS
    | MEAN
	| MEDIAN
	| MODE
	| WORDCOUNT
	| TOKENIZE
	| REMOVE'''

def p_empty(p) :
	'''empty : '''

def p_error(p) :
    print("Error en %s" % p.value)

# Function to start program
def p_func_start(p) :
	'func_start :'
	if globalScope.functionDirectory.addFunction("Main", "void", globalScope.nextAddress) :
		globalScope.functionName = "Main"
		globalScope.nextAddress += 1
	else :
		sys.exit("Error: Function ID already exists")

# Function to toggle constant flag (size/constant)
def p_func_isSize(p) :
	'func_isSize : '
	globalScope.isVarFlag = False

# Functions to declare variables and arrays
def p_func_declare_var(p) :
	'func_declare_var : '
	if globalScope.functionDirectory.addVariable(globalScope.functionName, p[-1], globalScope.varType, 1, globalScope.nextAddress) :
		globalScope.nextAddress += 1
	else:
		sys.exit("Error: Variable ID already exists")

def p_func_declare_array(p) :
	'func_declare_array : '
	if globalScope.functionDirectory.addVariable(globalScope.functionName, p[-5], globalScope.varType, globalScope.varSize, globalScope.nextAddress) :
		globalScope.nextAddress += 1
		globalScope.isVarFlag = True
	else:
		sys.exit("Error: Variable ID already exists")

# Function to declare functions and its attributes
def p_func_declare_function(p) :
	'func_declare_function : '
	if globalScope.functionDirectory.addFunction(p[-1], globalScope.varType, globalScope.nextAddress) :
		globalScope.functionName = p[-1]
		globalScope.nextAddress += 1
	else :
		sys.exit("Error: Function ID already exists")

def p_func_type(p) :
	'func_type : '
	globalScope.varType = p[-1]

# Function for constants
def p_func_constant(p) :
	'func_constant : '
	if globalScope.isVarFlag:
		globalScope.pendingOperands.push(p[-1])
	else:
		globalScope.varSize = p[-1]

def p_func_constantID(p) :
	'func_constantID : '
	if globalScope.functionDirectory.varExists(globalScope.functionName, p[-1]) :
		globalScope.pendingOperands.push(p[-1])
		globalScope.operandTypes.push(globalScope.functionDirectory.getVarType(globalScope.functionName, p[-1]))
	elif globalScope.functionName != "Main" and globalScope.functionDirectory.varExists("Main", p[-1]) :
		globalScope.pendingOperands.push(p[-1])
		globalScope.operandTypes.push(globalScope.functionDirectory.getVarType("Main", p[-1]))
	else :
		sys.exit("ID " + p[-1] + " does not exist")

def p_func_boolCte(p) :
	'func_boolCte : '
	if globalScope.isVarFlag:
		globalScope.operandTypes.push("bool")

def p_func_numberCte(p) :
	'func_numberCte : '
	if globalScope.isVarFlag:
		globalScope.operandTypes.push("number")

def p_func_wordCte(p) :
	'func_wordCte : '
	if globalScope.isVarFlag:
		globalScope.operandTypes.push("word")

def p_func_sentenceCte(p) :
	'func_sentenceCte : '
	if globalScope.isVarFlag:
		globalScope.operandTypes.push("sentence")


# Function to begin with main program
def p_func_begin_main(p) :
	'func_begin_main : '
	globalScope.functionName = "Main"

# Function for kread
def p_func_read(p) :
	'func_read : '
	input_id = p[-1]

	if globalScope.functionDirectory.varExists(globalScope.functionName, input_id) or (globalScope.functionName != "Main" and globalScope.functionDirectory.varExists("Main", input_id)) :
		quadruple = Quad("operator_read", "-1", "-1", input_id)
		globalScope.quads.append(quadruple)
		globalScope.quadCount += 1
	else :
		sys.exit("Input ID does not exist")

# Function for kprint
def p_func_print(p) :
	'func_print : '
	output_exp = globalScope.pendingOperands.pop()
	globalScope.operandTypes.pop()
	quadruple = Quad("operator_print", output_exp, "-1", "-1")
	globalScope.quads.append(quadruple)
	globalScope.quadCount += 1

# Functions for assign
def p_func_assign(p) :
	'func_assign : '
	globalScope.pendingOperators.push("operator_assign")

def p_func_assign_value(p) :
	'func_assign_value : '
	if not globalScope.pendingOperators.isEmpty() and globalScope.pendingOperators.top() == "operator_assign":
		# value
		rightOp = globalScope.pendingOperands.pop()
		rightType = globalScope.operandTypes.pop()
		# id with assigned value
		leftOp = globalScope.pendingOperands.pop()
		leftType = globalScope.operandTypes.pop()
	
		operator = globalScope.pendingOperators.pop()
		resultType = globalScope.semanticCube.verification(operator, leftType, rightType)

		if resultType != None:
			quadruple = Quad(operator, rightOp, "-1", leftOp)
			globalScope.quads.append(quadruple)
			globalScope.quadCount += 1
		else:
			sys.exit("Unable to assign value of type " + rightType + " to ID of type " + leftType)
			
# Functions for Arithmetic Expressions
def p_func_term_operation(p) :
	'func_term_operation : '
	if p[-1] == '+':
		globalScope.pendingOperators.push("operator_add")
	elif p[-1] == "-":
		globalScope.pendingOperators.push("operator_minus")

def p_func_term(p) :
	'func_term : '
	if not globalScope.pendingOperators.isEmpty() and (globalScope.pendingOperators.top() == "operator_add" or globalScope.pendingOperators.top() == "operator_minus"):
		rightOp = globalScope.pendingOperands.pop()
		rightType = globalScope.operandTypes.pop()
		leftOp = globalScope.pendingOperands.pop()
		leftType = globalScope.operandTypes.pop()
		operator = globalScope.pendingOperators.pop()

		resultType = globalScope.semanticCube.verification(operator, leftType, rightType)

		if resultType != None:
			result = "t" + str(globalScope.quadCount + 1)
			globalScope.pendingOperands.push(result)
			globalScope.operandTypes.push(resultType)
			quadruple = Quad(operator, leftOp, rightOp, result)
			globalScope.quads.append(quadruple)
			globalScope.quadCount += 1
		else:
			sys.exit("Unable to add/subtract term of type " + leftType + " with term of type " + rightType)

def p_func_factor_operation(p) :
	'func_factor_operation : '
	if p[-1] == '*':
		globalScope.pendingOperators.push("operator_mult")
	elif p[-1] == "/":
		globalScope.pendingOperators.push("operator_div")

def p_func_factor(p) :
	'func_factor : '
	if not globalScope.pendingOperators.isEmpty() and (globalScope.pendingOperators.top() == "operator_mult" or globalScope.pendingOperators.top() == "operator_div"):
		rightOp = globalScope.pendingOperands.pop()
		rightType = globalScope.operandTypes.pop()
		leftOp = globalScope.pendingOperands.pop()
		leftType = globalScope.operandTypes.pop()
		operator = globalScope.pendingOperators.pop()

		resultType = globalScope.semanticCube.verification(operator, leftType, rightType)

		if resultType != None:
			result = "t" + str(globalScope.quadCount + 1)
			globalScope.pendingOperands.push(result)
			globalScope.operandTypes.push(resultType)
			quadruple = Quad(operator, leftOp, rightOp, result)
			globalScope.quads.append(quadruple)
			globalScope.quadCount += 1
		else:
			sys.exit("Unable to multiply/divide factor of type " + leftType + " with factor of type " + rightType)

# Functions for Relational Expressions
def p_func_relop_operation(p) : 
	'func_relop_operation : '
	if p[-1] == ">":
		globalScope.pendingOperators.push("operator_greater")
	elif p[-1] == "<":
		globalScope.pendingOperators.push("operator_less")
	elif p[-1] == "==":
		globalScope.pendingOperators.push("operator_equal")
	elif p[-1] == "!=":
		globalScope.pendingOperators.push("operator_notequal")

def p_func_relop(p) :
	'func_relop : '
	if not globalScope.pendingOperators.isEmpty() and (globalScope.pendingOperators.top() == "operator_greater" or globalScope.pendingOperators.top() == "operator_less" or globalScope.pendingOperators.top() == "operator_equal" or globalScope.pendingOperators.top() == "operator_notequal") :
		rightOp = globalScope.pendingOperands.pop()
		rightType = globalScope.operandTypes.pop()
		leftOp = globalScope.pendingOperands.pop()
		leftType = globalScope.operandTypes.pop()
		operator = globalScope.pendingOperators.pop()

		resultType = globalScope.semanticCube.verification(operator, leftType, rightType)

		if resultType != None:
			result = "t" + str(globalScope.quadCount + 1)
			globalScope.pendingOperands.push(result)
			globalScope.operandTypes.push(resultType)
			quadruple = Quad(operator, leftOp, rightOp, result)
			globalScope.quads.append(quadruple)
			globalScope.quadCount += 1
			print("relop " + str(globalScope.quadCount))
		else:
			sys.exit("Unable to compare expression of type " + leftType + " with expression of type " + rightType)
	
# Functions for Logic Expressions
def p_func_logicOp_operation(p) :
	'func_logicOp_operation : '
	if p[-1] == "&":
		globalScope.pendingOperators.push("operator_and")
	elif p[-1] == "|":
		globalScope.pendingOperators.push("operator_or")
	elif p[-1] == "!":
		globalScope.pendingOperators.push("operator_not")

def p_func_logicOP(p) :
	'func_logicOP : '
	if not globalScope.pendingOperators.isEmpty() and (globalScope.pendingOperators.top() == "operator_and" or globalScope.pendingOperators.top() == "operator_or"):
		rightOp = globalScope.pendingOperands.pop()
		rightType = globalScope.operandTypes.pop()
		leftOp = globalScope.pendingOperands.pop()
		leftType = globalScope.operandTypes.pop()
		operator = globalScope.pendingOperators.pop()

		resultType = globalScope.semanticCube.verification(operator, leftType, rightType)

		if resultType != None:
			result = "t" + str(globalScope.quadCount + 1)
			globalScope.pendingOperands.push(result)
			globalScope.operandTypes.push(resultType)
			quadruple = Quad(operator, leftOp, rightOp, result)
			globalScope.quads.append(quadruple)
			globalScope.quadCount += 1
		else:
			sys.exit("Type " + leftType + " and type " + rightType + " can't be combined with a logical operator")
	
	elif not globalScope.pendingOperators.isEmpty() and globalScope.pendingOperators.top() == "operator_not":
		rightOp = globalScope.pendingOperands.pop()
		rightType = globalScope.operandTypes.pop()
		operator = globalScope.pendingOperators.pop()

		if rightType == "bool":
			result = "t" + str(globalScope.quadCount + 1)
			globalScope.pendingOperands.push(result)
			globalScope.operandTypes.push("bool")
			quadruple = Quad(operator, "-1", rightOp, result)
			globalScope.quads.append(quadruple)
			globalScope.quadCount += 1
			print("not " + str(globalScope.quadCount))
		else:
			sys.exit("Operator not can only be applied to operands of type bool")

# Functions for decisions
def p_func_if(p) :
	'func_if : '
	expressionType = globalScope.operandTypes.pop()

	if expressionType == "bool":
		result = globalScope.pendingOperands.pop()
		quadruple = Quad("operator_gotoF", result, "-1", "pending")
		globalScope.quads.append(quadruple)
		globalScope.quadCount += 1
		print("if " + str(globalScope.quadCount))
		globalScope.pendingJumps.push(globalScope.quadCount - 1)
	else:
		sys.exit("Cannot evaluate if condition with expression of type " + expressionType)

def p_func_endIf(p) :
	'func_endIf : '
	endIf = globalScope.pendingJumps.top()
	print(endIf)
	globalScope.quads[endIf-1].setResult(globalScope.quadCount)

def p_func_else(p) :
	'func_else : '
	quadruple = Quad("operator_goto", "-1", "-1", "pending")
	globalScope.quads.append(quadruple)
	globalScope.quadCount += 1

	elseFalse = globalScope.pendingJumps.pop()
	globalScope.pendingJumps.push(globalScope.quadCount - 1)
	globalScope.quads[elseFalse].setResult(globalScope.quadCount)

# Function to clear global scope variables after function ending
def p_func_clear(p) :
	'func_clear : '
	globalScope.pendingOperators.empty()
	globalScope.pendingOperands.empty()
	globalScope.operandTypes.empty()
	globalScope.quadCount = 1
	globalScope.isVarFlag = True
	globalScope.functionName = ""
	globalScope.varName = ""
	globalScope.varValue = []
	globalScope.varType = ""
	globalScope.varSize = ""
	globalScope.quads = []

yacc.yacc()


# Build the parser
data = '''kotoba program1;

declare number x, number arr[4.0], word w, bool b, sentence s, sentence ss;

function number myfunc(number y){
    declare number x;
    if(y > 2.0){
        y = y + 1.0;
    }else{
        y = y * 2.0;
    }
    return y;
}

begin
{
    if(!((x < 1.0) & (s == ss))) {
        kprint(s);
    }

	x = 1.0 + 4.0 * (5.0 / 5.0);

}
end
'''

yacc.parse(data)
