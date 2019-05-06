import ply.yacc as yacc
import LexKotoba
import globalScope
import sys

from dataStruct import Quad

tokens = LexKotoba.tokens

def p_start(p) :
	'''start : KOTOBA ID func_start ENDSTMT declare startaux BEGIN func_begin_main block END func_end
	| KOTOBA ID func_start ENDSTMT startaux BEGIN func_begin_main block END func_end'''

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
	'''assign : SET ID func_constantID EQUAL func_assign assignaux
	| SET ID OPENBRAC index CLOSEBRAC func_constantIDArray EQUAL func_assign assignaux'''

def p_assignaux(p) :
	'''assignaux : exp func_assign_value ENDSTMT
	| OPENCURL assiaux CLOSECURL ENDSTMT func_assign_array_end
	| callfunction func_assign_value'''

def p_assiaux(p) :
	'''assiaux : exp func_assign_array
	| exp func_assign_array COMA assiaux'''

def p_cte(p) :
	'''cte : ID func_constantID
	| ID OPENBRAC index CLOSEBRAC func_constantIDArray
	| BOOLCTE func_boolCte func_constant
	| NUMBERCTE func_numberCte func_constant
	| WORDCTE func_wordCte func_constant
	| SENTENCECTE func_sentenceCte func_constant'''

def p_index(p) :
	'''index : NUMBERCTE func_numberCte func_constant func_index
	| ID func_constantID func_index
 	'''
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
	|  IF OPENPAREN expression CLOSEPAREN func_if block ELSE func_else block func_endElse'''

def p_cycle(p) :
	'''cycle : WHILE func_while OPENPAREN expression CLOSEPAREN func_whileExp block func_endWhile
	| DO func_do block WHILE OPENPAREN expression CLOSEPAREN func_endDoWhile ENDSTMT'''

def p_function(p) :
	'''function : FUNC funcaux ID func_declare_function OPENPAREN parameter CLOSEPAREN OPENCURL declare blockaux returnaux ENDSTMT CLOSECURL
	| FUNC funcaux ID func_declare_function OPENPAREN parameter CLOSEPAREN OPENCURL blockaux returnaux ENDSTMT CLOSECURL'''

def p_funcaux(p) :
	'''funcaux : type
	| VOID func_type'''

def p_parameter(p) :
	'''parameter : type ID func_declare_par parameteraux
	| type ID OPENBRAC func_isSize cte CLOSEBRAC func_declare_array parameteraux
	| empty'''

def p_parameteraux(p) :
	'''parameteraux : COMA parameter
	| empty'''

def p_returnaux(p) :
	'''returnaux : RETURN ID func_return
	| RETURN func_return'''

def p_callfunction(p) :
	'''callfunction : CALL ID DOT special OPENPAREN spaux CLOSEPAREN func_callSpecial ENDSTMT
	| CALL ID func_callFunc OPENPAREN spaux CLOSEPAREN func_endCallFunction ENDSTMT'''

def p_spaux(p) :
	'''spaux : cte func_callFuncParameter
	| cte func_callFuncParameter COMA spaux
	| empty'''

def p_special(p) :
	'''special : LENGTH func_special
	| FREQUENCY func_special
    | SEARCH func_special
    | EXISTS func_special
    | MEAN func_special
	| MEDIAN func_special
	| MODE func_special
	| WORDCOUNT func_special
	| TOKENIZE func_special
	| REMOVE func_special
	| SORTWORDS func_special
	| SORTNUMBERS func_special
	| SIZE func_special'''

def p_empty(p) :
	'''empty : '''

def p_error(p) :
    print("Error en %s" % p.value)

# Function to start program
def p_func_start(p) :
	'func_start :'
	quadruple = Quad("operator_goto", -1, -1, "pending")
	globalScope.quads.append(quadruple)
	globalScope.quadCount += 1
	globalScope.pendingJumps.push(globalScope.quadCount - 1)
	if globalScope.functionDirectory.addFunction("Main", "void", -1) :
		globalScope.functionName = "Main"
	else :
		sys.exit("Error: Function ID already exists")

# Function to toggle constant flag (size/constant)
def p_func_isSize(p) :
	'func_isSize : '
	globalScope.isVarFlag = False

# Functions to declare variables and arrays
def p_func_declare_var(p) :
	'func_declare_var : '
	if not globalScope.functionDirectory.addVariable(globalScope.functionName, p[-1], globalScope.varType, 1) :
		sys.exit("Error: Variable ID " + p[-1] + " already exists")

def p_func_declare_array(p) :
	'func_declare_array : '
	if globalScope.functionDirectory.addVariable(globalScope.functionName, p[-5], globalScope.varType, globalScope.varSize) :
		globalScope.arrayList.append([globalScope.functionDirectory.getVarAddress(globalScope.functionName, p[-5]), globalScope.varSize, globalScope.functionName])
		globalScope.isVarFlag = True
	else:
		sys.exit("Error: Variable ID already exists")

def p_func_declare_par(p) :
	'func_declare_par : '
	if not globalScope.functionDirectory.addVariable(globalScope.functionName, p[-1], globalScope.varType, 1) :
		sys.exit("Error: Variable ID " + p[-1] + " already exists")

	address = globalScope.functionDirectory.getVarAddress(globalScope.functionName, p[-1])
	if not globalScope.functionDirectory.addParameter(globalScope.functionName, [globalScope.varType, address]) :
		sys.exit("Error: Parameter of type " + p[-1] + " cannot be added")

# Function to declare functions and its attributes
def p_func_declare_function(p) :
	'func_declare_function : '
	if globalScope.functionDirectory.addFunction(p[-1], globalScope.varType, globalScope.quadCount) :
		globalScope.functionName = p[-1]
	else :
		sys.exit("Error: Function ID " + p[-1] + " already exists")

def p_func_type(p) :
	'func_type : '
	globalScope.varType = p[-1]

def p_func_index(p) :
	'func_index : '
	try :
		float(p[-3])
		globalScope.index = p[-3]
	except : 
		globalScope.index = p[-2]


# Function for constants
def p_func_constant(p) :
	'func_constant : '
	if globalScope.isVarFlag :
		if globalScope.functionDirectory.constant_memory.get_AddressForConstant(p[-2]) == -1:
			type = globalScope.operandTypes.top()
			address = globalScope.functionDirectory.constant_memory.get_nextAddress(type)
			globalScope.functionDirectory.constant_memory.set_AddressValue(address, p[-2])
			globalScope.pendingOperands.push(address)
		else:
			address = globalScope.functionDirectory.constant_memory.get_AddressForConstant(p[-2])
			globalScope.functionDirectory.constant_memory.set_AddressValue(address, p[-2])
			globalScope.pendingOperands.push(address)
	else:
		globalScope.varSize = int(float(p[-2]))

def p_func_constantID(p) :
	'func_constantID : '
	functionName = globalScope.functionName
	if globalScope.functionDirectory.varExists(functionName, p[-1]):
		address = globalScope.functionDirectory.getVarAddress(functionName, p[-1])
		globalScope.pendingOperands.push(address)
		globalScope.operandTypes.push(globalScope.functionDirectory.getVarType(functionName, p[-1]))
		globalScope.varName = p[-1]
	elif globalScope.functionDirectory.functionExists(p[-1]) :
		globalScope.pendingOperands.push(p[-1])
		globalScope.operandTypes.push(globalScope.functionDirectory.functionType(p[-1]))
	elif globalScope.functionName != "Main" and globalScope.functionDirectory.varExists("Main", p[-1]) :
		address = globalScope.functionDirectory.getVarAddress("Main", p[-1])
		globalScope.pendingOperands.push(address)
		globalScope.operandTypes.push(globalScope.functionDirectory.getVarType("Main", p[-1]))
	else :
		sys.exit("ID " + p[-1] + " does not exist")

def p_func_constantIDArray(p) :
	'func_constantIDArray : '
	functionName = globalScope.functionName
	globalScope.varName = p[-4]

	if globalScope.functionDirectory.varExists(functionName, p[-4]):
		index_val = globalScope.pendingOperands.pop()
		index_type = globalScope.operandTypes.pop()

		if index_type == "number" :
			if globalScope.functionDirectory.varExists(functionName, globalScope.index) :
				address = "(" + str(globalScope.functionDirectory.getVarAddress(functionName, p[-4])) + ")"
				globalScope.pendingOperands.push(address)
				globalScope.operandTypes.push(globalScope.functionDirectory.getVarType(functionName, p[-4]))
			
				quadruple = Quad("operator_verify", "0", globalScope.functionDirectory.functions[functionName][1][p[-4]][1], index_val)
				globalScope.quads.append(quadruple)

				quadruple = Quad("operator_address", index_val, globalScope.functionDirectory.getVarAddress(functionName, p[-4]), "-1")
				globalScope.quads.append(quadruple)

				globalScope.quadCount += 2


			elif int(float(globalScope.index)) < globalScope.functionDirectory.functions[functionName][1][p[-4]][1] and int(float(globalScope.index)) > -1:
				address = globalScope.functionDirectory.getVarAddress(functionName, p[-4]) + int(float(globalScope.index))
				globalScope.pendingOperands.push(address)
				globalScope.operandTypes.push(globalScope.functionDirectory.getVarType(functionName, p[-4]))

				quadruple = Quad("operator_verify", "0", globalScope.functionDirectory.functions[functionName][1][p[-4]][1], globalScope.index)
				globalScope.quads.append(quadruple)

				quadruple = Quad("operator_address", globalScope.index, globalScope.functionDirectory.getVarAddress(functionName, p[-4]), address)
				globalScope.quads.append(quadruple)

				globalScope.quadCount += 2

			else :
				sys.exit("Out of range for size of variable " + p[-4])
		else :
			sys.exit("Wrong type of variable for index.")
	else :
		sys.exit("ID " + p[-4] + " does not exist")

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
	mainGoto = globalScope.pendingJumps.pop()
	globalScope.quads[mainGoto-1].setResult(globalScope.quadCount)
	globalScope.functionDirectory.setFuncQuadPosition("Main", globalScope.quadCount)

# Function for kread
def p_func_read(p) :
	'func_read : '
	input_id = p[-1]
	functionName = globalScope.functionName

	if globalScope.functionDirectory.varExists(functionName, input_id):
		address = globalScope.functionDirectory.getVarAddress(functionName, input_id)
		quadruple = Quad("operator_read", globalScope.functionDirectory.getVarType(functionName, p[-1]), "-1", address)
		globalScope.quads.append(quadruple)
		globalScope.quadCount += 1
	elif functionName != "Main" and globalScope.functionDirectory.varExists("Main", input_id):
		address = globalScope.functionDirectory.getVarAddress("Main", input_id)
		quadruple = Quad("operator_read", globalScope.functionDirectory.getVarType(functionName, p[-1]), "-1", address)
		globalScope.quads.append(quadruple)
		globalScope.quadCount += 1
	else :
		sys.exit("Input ID " + input_id + " does not exist")

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

def p_func_assign_array(p) :
	'func_assign_array : '
	if not globalScope.pendingOperators.isEmpty() and globalScope.pendingOperators.top() == "operator_assign":
		if globalScope.arrayIndexCounter < globalScope.functionDirectory.getVarSize(globalScope.functionName, globalScope.varName):
			# value
			rightOp = globalScope.pendingOperands.pop()
			rightType = globalScope.operandTypes.pop()
			# id with assigned value
			leftOp = globalScope.pendingOperands.top() + globalScope.arrayIndexCounter
			leftType = globalScope.operandTypes.top()

			operator = globalScope.pendingOperators.top()
			resultType = globalScope.semanticCube.verification(operator, leftType, rightType)
			globalScope.arrayIndexCounter += 1

			if resultType != None:
				quadruple = Quad(operator, rightOp, "-1", leftOp)
				globalScope.quads.append(quadruple)
				globalScope.quadCount += 1
			else:
				sys.exit("Unable to assign value of type " + rightType + " to ID of type " + leftType)

def p_func_assign_array_end(p) :
	'func_assign_array_end : '
	if globalScope.arrayIndexCounter < globalScope.functionDirectory.getVarSize(globalScope.functionName, globalScope.varName):
		sys.exit("Incorrect amount of values for array")
	else :
		globalScope.pendingOperands.pop()
		globalScope.operandTypes.pop()
		globalScope.pendingOperators.top()
		globalScope.arrayIndexCounter = 0

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
			result = globalScope.functionDirectory.local_memory.get_nextAddress(resultType)
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
			result = globalScope.functionDirectory.local_memory.get_nextAddress(resultType)
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
			result = globalScope.functionDirectory.local_memory.get_nextAddress(resultType)
			globalScope.pendingOperands.push(result)
			globalScope.operandTypes.push(resultType)
			quadruple = Quad(operator, leftOp, rightOp, result)
			globalScope.quads.append(quadruple)
			globalScope.quadCount += 1
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
			result = globalScope.functionDirectory.local_memory.get_nextAddress(resultType)
			globalScope.pendingOperands.push(result)
			globalScope.operandTypes.push(resultType)
			quadruple = Quad(operator, leftOp, rightOp, result)
			globalScope.quads.append(quadruple)
			globalScope.quadCount += 1
		else:
			sys.exit("Type " + leftType + " and type " + rightType + " can't be combined with a logical operator")

	elif not globalScope.pendingOperators.isEmpty() and globalScope.pendingOperators.top() == "operator_not":
		leftOp = globalScope.pendingOperands.pop()
		leftType = globalScope.operandTypes.pop()
		operator = globalScope.pendingOperators.pop()

		if leftType == "bool":
			result = globalScope.functionDirectory.local_memory.get_nextAddress("bool")
			globalScope.pendingOperands.push(result)
			globalScope.operandTypes.push("bool")
			quadruple = Quad(operator, leftOp, "-1", result)
			globalScope.quads.append(quadruple)
			globalScope.quadCount += 1
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
		globalScope.pendingJumps.push(globalScope.quadCount - 1)
	else:
		sys.exit("Cannot evaluate if condition with expression of type " + expressionType)

def p_func_endIf(p) :
	'func_endIf : '
	endIf = globalScope.pendingJumps.pop()
	globalScope.quads[endIf-1].setResult(globalScope.quadCount)

def p_func_else(p) :
	'func_else : '
	quadruple = Quad("operator_goto", "-1", "-1", "pending")
	globalScope.quads.append(quadruple)
	globalScope.quadCount += 1
	# Adds quad after else goto to if gotoF
	endIf = globalScope.pendingJumps.pop()
	globalScope.quads[endIf-1].setResult(globalScope.quadCount)
	# Adds else goto pending jump
	globalScope.pendingJumps.push(globalScope.quadCount - 1)

def p_func_endElse(p) :
	'func_endElse : '
	elseFalse = globalScope.pendingJumps.pop()
	globalScope.quads[elseFalse-1].setResult(globalScope.quadCount)

# Functions for cycles
def p_func_do(p) :
	'func_do : '
	globalScope.pendingJumps.push(globalScope.quadCount)

def p_func_endDoWhile(p) :
	'func_endDoWhile : '
	whileType = globalScope.operandTypes.pop()

	if whileType == "bool":
		result = globalScope.pendingOperands.pop()
		returnLoop = globalScope.pendingJumps.pop()

		quadruple = Quad("operator_gotoT", result, "-1", returnLoop)
		globalScope.quads.append(quadruple)
		globalScope.quadCount += 1
	else:
		sys.exit("Do while expression can't be evaluated with value of type " + whileType)

def p_func_while(p) :
	'func_while : '
	globalScope.pendingJumps.push(globalScope.quadCount)

def p_func_whileExp(p) :
	'func_whileExp : '
	whileType = globalScope.operandTypes.pop()

	if whileType == "bool":
		result = globalScope.pendingOperands.pop()
		quadruple = Quad("operator_gotoF", result, "-1", "pending")
		globalScope.quads.append(quadruple)
		globalScope.quadCount += 1
		globalScope.pendingJumps.push(globalScope.quadCount - 1)
	else:
		sys.exit("While expression can't be evaluated with value of type " + whileType)


def	p_func_endWhile(p) :
	'func_endWhile : '
	endWhile = globalScope.pendingJumps.pop()
	returnWhile = globalScope.pendingJumps.pop()

	quadruple = Quad("operator_goto", "-1", "-1", returnWhile)
	globalScope.quads.append(quadruple)
	globalScope.quadCount += 1

	globalScope.quads[endWhile-1].setResult(globalScope.quadCount)

def p_func_callFunc(p) :
	'func_callFunc : '
	if globalScope.functionDirectory.functionExists(p[-1]) :
		globalScope.functionCalled = p[-1]

		globalScope.pendingOperands.push(p[-1])
		quadruple = Quad("operator_era", "-1", "-1", p[-1])
		globalScope.quads.append(quadruple)
		globalScope.quadCount += 1
	else :
		sys.exit("Function ID doesn't exist in directory")

def p_func_callFuncParameter(p) :
	'func_callFuncParameter : '
	parameterVar = globalScope.pendingOperands.pop()
	parameterType = globalScope.operandTypes.pop()

	if globalScope.isSpecial :
		globalScope.varName = parameterVar
	elif parameterType == globalScope.functionDirectory.functions[globalScope.functionCalled][2][globalScope.parameterCount - 1][0] :
		quadruple = Quad("operator_param", parameterVar, "-1", "param" + str(globalScope.parameterCount))
		globalScope.quads.append(quadruple)
		globalScope.quadCount += 1
		globalScope.parameterCount += 1
	else :
		sys.exit("Parameter incorrect for function " + globalScope.pendingOperands.top())

def p_func_endCallFunction(p) :
	'func_endCallFunction : '
	if globalScope.functionCalled == globalScope.pendingOperands.pop() and globalScope.parameterCount - 1 == len(globalScope.functionDirectory.functions[globalScope.functionCalled][2]):
		quadruple = Quad("operator_gosub", "-1", "-1",globalScope.functionCalled)
		globalScope.quads.append(quadruple)
		globalScope.quadCount += 1

		if globalScope.functionDirectory.functions[globalScope.functionCalled][0] != "void" :
			globalScope.pendingOperands.push("(" + globalScope.functionCalled + ")")
			globalScope.operandTypes.push(globalScope.functionDirectory.functions[globalScope.functionCalled][0])

		print("Local Memory for: " + globalScope.functionCalled)
		globalScope.functionDirectory.local_memory.print_Memory()
		print("-----------------------------")
		globalScope.functionCalled = ""
		globalScope.parameterCount = 1

		# CLEAR LOCAL MEMORY
		globalScope.functionDirectory.local_memory.clear_Memory()

def p_func_special(p) :
	'func_special : '
	globalScope.funcSpecial = p[-1]
	globalScope.isSpecial = True

def p_func_callSpecial(p) :
	'func_callSpecial : '
	if globalScope.functionDirectory.varExists(globalScope.functionName, p[-6]) :
		address = globalScope.functionDirectory.getVarAddress(globalScope.functionName, p[-6])

		if p[-2] == "":
			quadruple = Quad("operator_special", address, "-1", globalScope.funcSpecial)
			globalScope.quads.append(quadruple)
		else :
			quadruple = Quad("operator_special", address, globalScope.varName, globalScope.funcSpecial)
			globalScope.quads.append(quadruple)
			globalScope.quadCount += 1

		if globalScope.funcSpecial != "sortNumbers" or globalScope.funcSpecial != "sortWords" or globalScope.funcSpecial != "remove":
			globalScope.pendingOperands.push("(" + globalScope.funcSpecial + ")")
			if globalScope.funcSpecial == "exists" :
				globalScope.operandTypes.push("bool")
			elif globalScope.funcSpecial == "tokenize" :
				globalScope.operandTypes.push("word")
			else :
				globalScope.operandTypes.push("number")

		

	globalScope.isSpecial = False

def p_func_return(p) :
	'func_return : '
	if globalScope.functionDirectory.functionType(globalScope.functionName) != "void":
		address = globalScope.functionDirectory.getVarAddress(globalScope.functionName, p[-1])
		quadruple = Quad("operator_return", "-1", "-1", address)
		globalScope.quads.append(quadruple)
		globalScope.quadCount += 1
	else :
		quadruple = Quad("operator_return", "-1", "-1", "void")
		globalScope.quads.append(quadruple)
		globalScope.quadCount += 1


# # Function to clear global scope variables after program ending
# def p_func_clear(p) :
# 	'func_clear : '
# 	quadruple = Quad("operator_endfunc", "-1", "-1", "-1")
# 	globalScope.quads.append(quadruple)
# 	globalScope.quadCount += 1

# 	globalScope.pendingOperators.empty()
# 	globalScope.pendingOperands.empty()
# 	globalScope.operandTypes.empty()
# 	globalScope.isVarFlag = True
# 	globalScope.functionName = ""
# 	globalScope.varName = ""
# 	globalScope.varType = ""
# 	globalScope.varSize = ""


# Function to add end program
def p_func_end(p) :
	'func_end : '
	quadruple = Quad("end", "-1", "-1", "-1")
	globalScope.quads.append(quadruple)
	globalScope.quadCount += 1

	print("Compilation succeeded")
	globalScope.functionDirectory.printDirectory()
	print("-----------------------------")

	print("My quads are: ")
	i = 1
	for quad in globalScope.quads:
		print(str(i) + "   " + str(quad.getOperator()) + "\t" + str(quad.getLeftOperator()) + "\t" + str(quad.getRightOperator()) + "\t" + str(quad.getResult()))
		#quad.printQuad()
		i += 1

	# print("-----------------------------")
	# globalScope.functionDirectory.global_memory.print_Memory()
	# print("-----------------------------")
	# globalScope.functionDirectory.local_memory.print_Memory()
	# print("-----------------------------")
	# globalScope.functionDirectory.constant_memory.print_Memory()
	print("-----------------------------")
	print("-----------------------------")
	print("-----------------------------")
	print("")


# Build the parser
def parse(data) :
	yacc.yacc()

	yacc.parse(data)
