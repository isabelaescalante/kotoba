import ply.yacc as yacc
import LexKotoba
import globalScope

tokens = LexKotoba.tokens

def p_start(p) :
	'''start : KOTOBA ID ENDSTMT declare startaux BEGIN block END
	| KOTOBA ID ENDSTMT startaux BEGIN block END'''
	print("aceptado")

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
	'''input : READ OPENPAREN ID CLOSEPAREN ENDSTMT'''

def p_output(p) :
	'''output : WRITE OPENPAREN outputaux CLOSEPAREN ENDSTMT'''

def p_outputaux(p) :
	'''outputaux : expression
	| expression COMA outputaux'''

def p_declare(p) :
	'''declare : DEC decaux'''

def p_decaux(p) :
	'''decaux : type ID declareaux
	| type ID OPENBRAC cte CLOSEBRAC  declareaux'''

def p_declareaux(p) :
	'''declareaux : ENDSTMT
	| COMA decaux'''

def p_assign(p) :
	'''assign : ID EQUAL assignaux
	| ID OPENBRAC cte CLOSEBRAC EQUAL assignaux'''

def p_assignaux(p) :
	'''assignaux : exp ENDSTMT
	| OPENCURL assiaux CLOSECURL ENDSTMT'''

def p_assiaux(p) :
	'''assiaux : exp
	| exp COMA assiaux'''

def p_cte(p) :
	'''cte : ID
	| BOOLCTE
	| NUMBERCTE
	| WORDCTE
	| SENTENCECTE'''

def p_type(p) :
	'''type : BOOL
	| NUMBER
	| WORD
	| SENTENCE'''

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
	'''function : FUNC funcaux ID OPENPAREN parameter CLOSEPAREN OPENCURL declare blockaux returnaux ENDSTMT CLOSECURL
	| FUNC funcaux ID OPENPAREN parameter CLOSEPAREN OPENCURL blockaux returnaux ENDSTMT CLOSECURL'''

def p_funcaux(p) :
	'''funcaux : type
	| VOID'''

def p_parameter(p) :
	'''parameter : type ID parameteraux
	| type ID OPENBRAC cte CLOSEBRAC parameteraux'''

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

yacc.yacc()

#Build the parser
data = '''kotoba program1;

declare number x, number arr[4.0], word w, bool b, sentence s;

function number myfunc(number y, number arr[5.0]){
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
