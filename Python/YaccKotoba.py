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
	print(globalScope.functionDirectory.printDirectory())
	
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
	| ID func_constantID OPENBRAC func_isSize cte CLOSEBRAC EQUAL func_assign assignaux'''

def p_assignaux(p) :
	'''assignaux : exp ENDSTMT
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
	| specialfunction'''

def p_expression(p) :
	'''expression : relopexpression
	| relopexpression AND expression
	| relopexpression OR expression'''

def p_relopexression(p) :
	'''relopexpression : exp
	| exp RELOP exp
	| NOT exp'''

def p_exp(p) :
	'''exp : term
	| term PLUS exp
	| term MINUS exp'''

def p_term(p) :
	'''term : factor
	| factor MULT term
	| factor DIV term'''

def p_factor(p) :
	'''factor : OPENPAREN expression CLOSEPAREN
	| cte'''

def p_condition(p) :
	'''condition : IF OPENPAREN expression CLOSEPAREN block
	|  IF OPENPAREN expression CLOSEPAREN block ELSE block'''

def p_cycle(p) :
	'''cycle : WHILE OPENPAREN expression CLOSEPAREN block
	| DO block WHILE OPENPAREN expression CLOSEPAREN ENDSTMT'''

def p_function(p) :
	'''function : FUNC funcaux ID func_declare_function OPENPAREN parameter CLOSEPAREN OPENCURL declare blockaux returnaux ENDSTMT CLOSECURL
	| FUNC funcaux ID func_declare_function OPENPAREN parameter CLOSEPAREN OPENCURL blockaux returnaux ENDSTMT CLOSECURL'''

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

def p_specialfunction(p) :
	'''specialfunction : ID DOT special OPENPAREN spaux CLOSEPAREN ENDSTMT'''

def p_spaux(p) :
	'''spaux : cte
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

# Functions to declare variables and arrays
def p_func_declare_var(p) :
	'func_declare_var : '
	if globalScope.functionDirectory.addVariable(globalScope.functionName, p[-1], globalScope.varType, 1, globalScope.nextAddress) :
		globalScope.nextAddress += 1
	else:
		sys.exit("Error: Variable ID already exists")

def p_func_declare_array(p) :
	'func_declare_array : '
	if globalScope.functionDirectory.addVariable(globalScope.functionName, p[-4], globalScope.varType, globalScope.varSize, globalScope.nextAddress) :
		globalScope.nextAddress += 1
		globalScope.isVarFlag = True
	else:
		sys.exit("Error: Variable ID already exists")

# Function to toggle constant flag (size/constant)
def p_func_isSize(p) :
	'func_isSize : '
	globalScope.isVarFlag = False


# Function to declare functions and its attributes
def p_func_declare_function(p) :
	'func_declare_function : '
	if globalScope.functionDirectory.addFunction(p[-1], globalScope.varType, globalScope.nextAddress) :
		globalScope.functionName = p[-1]
		globalScope.nextAddress += 1
		globalScope.isVarFlag = True
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
	if globalScope.functionDirectory.varExists(globalScope.functionName, p[-1]) or (globalScope.functionName != "Main" and globalScope.functionDirectory.varExists("Main", p[-1])) :
		globalScope.pendingOperands.push(p[-1])
	else :
		sys.exit("ID does not exist")

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
		quadruple = Quad("operator_read", "", "", input_id)
		globalScope.quads.append(quadruple)
		globalScope.quadCount += 1
	else :
		sys.exit("Input ID does not exist")

# Function for kprint
def p_func_print(p) :
	'func_print : '
	output_exp = globalScope.pendingOperands.pop()
	quadruple = Quad("operator_print", output_exp, "", "")
	globalScope.quads.append(quadruple)
	globalScope.quadCount += 1

# Function for assign
def p_func_assign(p) :
	'func_assign : '
	globalScope.pendingOperators.push("operator_assign")

# Functions for Expressions

yacc.yacc()


# Build the parser
data = '''kotoba program1;

declare number x, number arr[4.0], word w, bool b, sentence s;

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
    kread(w);
    if(!(x < 1.0)){
        kprint(s,1.0);
    }
    if((x < 1.0) & (s == b)){
        s.wordCount();
    }

    while(x > 10.0){
        x = x - 1.0;
    }

    do{
        x = x / 2.0;
    }while(x > 20.0);
}
end'''

yacc.parse(data)
