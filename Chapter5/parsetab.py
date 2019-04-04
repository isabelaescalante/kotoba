
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND BEGIN BOOL BOOLCTE CLOSEBRAC CLOSECURL CLOSEPAREN COMA DEC DIV DO DOT ELSE END ENDSTMT EQUAL EXISTS FREQUENCY FUNC ID IF KOTOBA LENGTH MEAN MEDIAN MINUS MODE MULT NOT NUMBER NUMBERCTE OPENBRAC OPENCURL OPENPAREN OR PLUS READ RELOP REMOVE RETURN SEARCH SENTENCE SENTENCECTE TOKENIZE VOID WHILE WORD WORDCOUNT WORDCTE WRITEstart : KOTOBA ID func_start ENDSTMT declare startaux BEGIN func_begin_main block END\n\t| KOTOBA ID func_start ENDSTMT startaux BEGIN func_begin_main block ENDstartaux : function startaux\n\t| emptyblock : OPENCURL blockaux CLOSECURLblockaux : action blockaux\n\t| emptyaction : input\n\t| output\n\t| statementinput : READ OPENPAREN ID func_read CLOSEPAREN ENDSTMToutput : WRITE OPENPAREN outputaux CLOSEPAREN ENDSTMToutputaux : expression func_print\n\t| expression func_print COMA outputauxdeclare : DEC decauxdecaux : type ID func_declare_var declareaux\n\t| type ID OPENBRAC func_isSize cte CLOSEBRAC func_declare_array declareauxdeclareaux : ENDSTMT\n\t| COMA decauxassign : ID func_constantID EQUAL func_assign assignaux\n\t| ID func_constantID OPENBRAC func_isSize cte CLOSEBRAC EQUAL assignauxassignaux : exp func_assign_value ENDSTMT\n\t| OPENCURL assiaux CLOSECURL ENDSTMTassiaux : exp\n\t| exp COMA assiauxcte : ID func_constantID\n\t| BOOLCTE func_constant func_boolCte\n\t| NUMBERCTE func_constant func_numberCte\n\t| WORDCTE func_constant func_wordCte\n\t| SENTENCECTE func_constant func_sentenceCtetype : BOOL func_type\n\t| NUMBER func_type\n\t| WORD func_type\n\t| SENTENCE func_typestatement : assign\n\t| expression\n\t| condition\n\t| cycle\n\t| callfunctionexpression : logexpression\n\t| NOT func_logicOp_operation logexpression func_logicOPlogexpression : relopexpression \n\t| relopexpression AND func_logicOp_operation logexpression func_logicOP\n\t| relopexpression OR func_logicOp_operation logexpression func_logicOPrelopexpression : exp \n\t| exp func_relop RELOP func_relop_operation exp func_relopexp : term\n\t| term PLUS func_term_operation exp func_term\n\t| term MINUS func_term_operation exp func_termterm : factor\n\t| factor MULT func_factor_operation term func_factor\n\t| factor DIV func_factor_operation term func_factorfactor : OPENPAREN expression CLOSEPAREN\n\t| ctecondition : IF OPENPAREN expression CLOSEPAREN func_if block func_endIf \n\t|  IF OPENPAREN expression CLOSEPAREN func_if block ELSE func_else block func_endElsecycle : WHILE func_while OPENPAREN expression CLOSEPAREN func_whileExp block func_endWhile\n\t| DO func_do block WHILE OPENPAREN expression CLOSEPAREN func_endDoWhile ENDSTMTfunction : FUNC funcaux ID func_declare_function OPENPAREN parameter CLOSEPAREN OPENCURL declare blockaux returnaux ENDSTMT CLOSECURL\n\t| FUNC funcaux ID func_declare_function OPENPAREN parameter CLOSEPAREN OPENCURL blockaux returnaux ENDSTMT CLOSECURLfuncaux : type\n\t| VOIDparameter : type ID func_declare_var parameteraux\n\t| type ID OPENBRAC func_isSize cte CLOSEBRAC func_declare_array parameterauxparameteraux : COMA parameter\n\t| emptyreturnaux : RETURN ID\n\t| emptycallfunction : ID DOT special OPENPAREN spaux CLOSEPAREN ENDSTMT\n\t| ID OPENPAREN spaux CLOSEPAREN ENDSTMTspaux : cte\n\t| cte COMA spaux\n\t| emptyspecial : LENGTH  \n\t| FREQUENCY\n    | SEARCH\n    | EXISTS\n    | MEAN\n\t| MEDIAN\n\t| MODE\n\t| WORDCOUNT\n\t| TOKENIZE\n\t| REMOVEempty : func_start :func_isSize : func_declare_var : func_declare_array : func_declare_function : func_type : func_constant : func_constantID : func_boolCte : func_numberCte : func_wordCte : func_sentenceCte : func_begin_main : func_read : func_print : func_assign : func_assign_value : func_term_operation : func_term : func_factor_operation : func_factor : func_relop_operation : func_relop : func_logicOp_operation : func_logicOP : func_if : func_endIf : func_else : func_endElse : func_do : func_endDoWhile : func_while : func_whileExp : func_endWhile : func_clear : '
    
_lr_action_items = {'DO':([15,34,39,41,42,44,45,47,49,50,51,55,56,59,60,61,62,63,65,66,67,68,69,70,75,76,77,79,80,82,85,92,104,105,107,108,110,111,117,146,147,150,151,152,158,159,164,165,169,170,171,173,174,177,179,182,183,185,191,193,194,202,210,215,216,217,224,225,227,231,232,235,],[-15,43,-18,-16,-91,-91,-91,-91,-39,-10,-8,-50,-40,-42,-92,-37,-38,-47,-54,-45,43,-9,-36,-35,-92,-19,-94,-95,-93,-96,-5,-26,-26,-28,-29,-27,-30,-53,-109,-105,-105,-41,-109,-109,-103,-103,43,-17,-52,-51,-12,-43,-44,-20,-70,-48,-49,-107,43,-11,-111,-46,-55,-22,-69,-118,-21,-23,-57,-58,-113,-56,]),'RETURN':([15,39,41,42,44,45,47,49,50,51,53,55,56,59,60,61,62,63,65,66,67,68,69,70,75,76,77,79,80,82,85,92,99,104,105,107,108,110,111,117,146,147,150,151,152,158,159,164,165,169,170,171,173,174,177,179,182,183,185,190,191,193,194,202,208,210,215,216,217,224,225,227,231,232,235,],[-15,-18,-16,-91,-91,-91,-91,-39,-10,-8,-7,-50,-40,-42,-92,-37,-38,-47,-54,-45,-84,-9,-36,-35,-92,-19,-94,-95,-93,-96,-5,-26,-6,-26,-28,-29,-27,-30,-53,-109,-105,-105,-41,-109,-109,-103,-103,-84,-17,-52,-51,-12,-43,-44,-20,-70,-48,-49,-107,205,-84,-11,-111,-46,205,-55,-22,-69,-118,-21,-23,-57,-58,-113,-56,]),'BOOLCTE':([15,32,34,38,39,41,42,44,45,47,48,49,50,51,55,56,58,59,60,61,62,63,65,66,67,68,69,70,75,76,77,79,80,82,84,85,86,87,88,89,90,91,92,93,95,96,104,105,107,108,110,111,113,114,117,118,119,120,121,136,137,138,139,146,147,150,151,152,153,154,156,157,158,159,161,162,164,165,166,169,170,171,172,173,174,176,177,179,182,183,185,186,191,193,194,202,210,212,214,215,216,217,224,225,227,231,232,235,],[-15,-86,45,45,-18,-16,-91,-91,-91,-91,45,-39,-10,-8,-50,-40,-108,-42,-92,-37,-38,-47,-54,-45,45,-9,-36,-35,-92,-19,-94,-95,-93,-96,45,-5,-104,-104,45,45,-108,-108,-26,45,-102,-102,-26,-28,-29,-27,-30,-53,45,45,-109,45,45,-86,-100,45,45,45,-106,-105,-105,-41,-109,-109,45,45,45,45,-103,-103,45,-86,45,-17,45,-52,-51,-12,45,-43,-44,45,-20,-70,-48,-49,-107,45,45,-11,-111,-46,-55,45,45,-22,-69,-118,-21,-23,-57,-58,-113,-56,]),'READ':([15,34,39,41,42,44,45,47,49,50,51,55,56,59,60,61,62,63,65,66,67,68,69,70,75,76,77,79,80,82,85,92,104,105,107,108,110,111,117,146,147,150,151,152,158,159,164,165,169,170,171,173,174,177,179,182,183,185,191,193,194,202,210,215,216,217,224,225,227,231,232,235,],[-15,46,-18,-16,-91,-91,-91,-91,-39,-10,-8,-50,-40,-42,-92,-37,-38,-47,-54,-45,46,-9,-36,-35,-92,-19,-94,-95,-93,-96,-5,-26,-26,-28,-29,-27,-30,-53,-109,-105,-105,-41,-109,-109,-103,-103,46,-17,-52,-51,-12,-43,-44,-20,-70,-48,-49,-107,46,-11,-111,-46,-55,-22,-69,-118,-21,-23,-57,-58,-113,-56,]),'MEDIAN':([94,],[129,]),'VOID':([10,],[21,]),'NUMBER':([6,10,40,72,187,],[13,13,13,13,13,]),'ENDSTMT':([3,4,15,28,33,39,41,42,44,45,47,49,50,51,53,55,56,59,60,61,62,63,65,66,67,68,69,70,75,76,77,79,80,82,85,92,99,103,104,105,107,108,110,111,117,142,146,147,148,150,151,152,155,158,159,164,165,167,169,170,171,173,174,177,178,179,182,183,185,190,191,193,194,199,200,202,206,207,208,209,210,213,215,216,217,219,221,222,224,225,227,231,232,235,],[-85,5,-15,-87,39,-18,-16,-91,-91,-91,-91,-39,-10,-8,-7,-50,-40,-42,-92,-37,-38,-47,-54,-45,-84,-9,-36,-35,-92,-19,-94,-95,-93,-96,-5,-26,-6,-88,-26,-28,-29,-27,-30,-53,-109,39,-105,-105,171,-41,-109,-109,179,-103,-103,-84,-17,193,-52,-51,-12,-43,-44,-20,-101,-70,-48,-49,-107,-84,-84,-11,-111,215,216,-46,220,-68,-84,-115,-55,225,-22,-69,-118,-67,230,231,-21,-23,-57,-58,-113,-56,]),'WHILE':([15,34,39,41,42,44,45,47,49,50,51,55,56,59,60,61,62,63,65,66,67,68,69,70,75,76,77,79,80,82,85,92,104,105,106,107,108,110,111,117,146,147,150,151,152,158,159,164,165,169,170,171,173,174,177,179,182,183,185,191,193,194,202,210,215,216,217,224,225,227,231,232,235,],[-15,64,-18,-16,-91,-91,-91,-91,-39,-10,-8,-50,-40,-42,-92,-37,-38,-47,-54,-45,64,-9,-36,-35,-92,-19,-94,-95,-93,-96,-5,-26,-26,-28,143,-29,-27,-30,-53,-109,-105,-105,-41,-109,-109,-103,-103,64,-17,-52,-51,-12,-43,-44,-20,-70,-48,-49,-107,64,-11,-111,-46,-55,-22,-69,-118,-21,-23,-57,-58,-113,-56,]),'SENTENCECTE':([15,32,34,38,39,41,42,44,45,47,48,49,50,51,55,56,58,59,60,61,62,63,65,66,67,68,69,70,75,76,77,79,80,82,84,85,86,87,88,89,90,91,92,93,95,96,104,105,107,108,110,111,113,114,117,118,119,120,121,136,137,138,139,146,147,150,151,152,153,154,156,157,158,159,161,162,164,165,166,169,170,171,172,173,174,176,177,179,182,183,185,186,191,193,194,202,210,212,214,215,216,217,224,225,227,231,232,235,],[-15,-86,47,47,-18,-16,-91,-91,-91,-91,47,-39,-10,-8,-50,-40,-108,-42,-92,-37,-38,-47,-54,-45,47,-9,-36,-35,-92,-19,-94,-95,-93,-96,47,-5,-104,-104,47,47,-108,-108,-26,47,-102,-102,-26,-28,-29,-27,-30,-53,47,47,-109,47,47,-86,-100,47,47,47,-106,-105,-105,-41,-109,-109,47,47,47,47,-103,-103,47,-86,47,-17,47,-52,-51,-12,47,-43,-44,47,-20,-70,-48,-49,-107,47,47,-11,-111,-46,-55,47,47,-22,-69,-118,-21,-23,-57,-58,-113,-56,]),'DIV':([42,44,45,47,55,60,65,75,77,79,80,82,92,104,105,107,108,110,111,],[-91,-91,-91,-91,86,-92,-54,-92,-94,-95,-93,-96,-26,-26,-28,-29,-27,-30,-53,]),'DEC':([5,164,],[6,6,]),'OPENPAREN':([15,30,34,36,39,41,42,44,45,46,47,48,49,50,51,52,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,75,76,77,79,80,82,84,85,86,87,88,89,90,91,92,95,96,97,104,105,107,108,110,111,113,114,117,118,119,121,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,143,146,147,150,151,152,154,158,159,161,164,165,166,169,170,171,172,173,174,176,177,179,182,183,185,191,193,194,202,210,212,214,215,216,217,224,225,227,231,232,235,],[-15,-89,48,72,-18,-16,-91,-91,-91,81,-91,48,-39,-10,-8,84,-50,-40,88,-108,-42,93,-37,-38,-47,-116,-54,-45,48,-9,-36,-35,-92,-19,-94,-95,-93,-96,48,-5,-104,-104,48,48,-108,-108,-26,-102,-102,138,-26,-28,-29,-27,-30,-53,48,48,-109,48,48,-100,-83,-76,-77,-81,-79,-82,-74,-75,-80,157,-78,48,48,48,-106,166,-105,-105,-41,-109,-109,48,-103,-103,48,48,-17,48,-52,-51,-12,48,-43,-44,48,-20,-70,-48,-49,-107,48,-11,-111,-46,-55,48,48,-22,-69,-118,-21,-23,-57,-58,-113,-56,]),'MULT':([42,44,45,47,55,60,65,75,77,79,80,82,92,104,105,107,108,110,111,],[-91,-91,-91,-91,87,-92,-54,-92,-94,-95,-93,-96,-26,-26,-28,-29,-27,-30,-53,]),'BEGIN':([5,7,8,9,11,15,19,23,39,41,76,165,229,234,],[-84,18,-4,-84,-84,-15,-3,31,-18,-16,-19,-17,-60,-59,]),'WORD':([6,10,40,72,187,],[16,16,16,16,16,]),'CLOSEPAREN':([42,44,45,47,55,56,59,63,65,66,75,77,79,80,82,83,93,101,104,105,107,108,109,110,111,112,115,116,117,122,123,124,140,144,146,147,149,150,151,152,156,157,158,159,160,163,169,170,173,174,180,181,182,183,185,188,189,192,195,202,204,218,228,233,],[-91,-91,-91,-91,-50,-40,-42,-47,-54,-45,-92,-94,-95,-93,-96,111,-84,141,-26,-28,-29,-27,-98,-30,-53,145,148,-99,-109,155,-71,-73,-87,167,-105,-105,-13,-41,-109,-109,-84,-84,-103,-103,184,-84,-52,-51,-43,-44,-72,200,-48,-49,-107,-63,-66,209,-14,-46,-65,-88,-84,-64,]),'WORDCOUNT':([94,],[128,]),'OPENCURL':([18,29,31,37,43,78,121,141,145,154,168,184,201,211,212,223,],[-97,34,-97,34,-114,34,-100,164,-110,176,34,-117,34,-112,176,34,]),'MINUS':([42,44,45,47,55,60,63,65,75,77,79,80,82,92,104,105,107,108,110,111,146,147,169,170,],[-91,-91,-91,-91,-50,-92,96,-54,-92,-94,-95,-93,-96,-26,-26,-28,-29,-27,-30,-53,-105,-105,-52,-51,]),'KOTOBA':([0,],[1,]),'PLUS':([42,44,45,47,55,60,63,65,75,77,79,80,82,92,104,105,107,108,110,111,146,147,169,170,],[-91,-91,-91,-91,-50,-92,95,-54,-92,-94,-95,-93,-96,-26,-26,-28,-29,-27,-30,-53,-105,-105,-52,-51,]),'DOT':([60,],[94,]),'TOKENIZE':([94,],[130,]),'$end':([2,71,102,],[0,-2,-1,]),'CLOSECURL':([34,42,44,45,47,49,50,51,53,54,55,56,59,60,61,62,63,65,66,67,68,69,70,75,77,79,80,82,85,92,99,104,105,107,108,110,111,117,146,147,150,151,152,158,159,169,170,171,173,174,177,179,182,183,185,193,194,197,198,202,210,215,216,217,220,224,225,226,227,230,231,232,235,],[-84,-91,-91,-91,-91,-39,-10,-8,-7,85,-50,-40,-42,-92,-37,-38,-47,-54,-45,-84,-9,-36,-35,-92,-94,-95,-93,-96,-5,-26,-6,-26,-28,-29,-27,-30,-53,-109,-105,-105,-41,-109,-109,-103,-103,-52,-51,-12,-43,-44,-20,-70,-48,-49,-107,-11,-111,213,-24,-46,-55,-22,-69,-118,229,-21,-23,-25,-57,234,-58,-113,-56,]),'END':([35,73,85,],[71,102,-5,]),'RELOP':([42,44,45,47,55,60,63,65,66,75,77,79,80,82,92,98,104,105,107,108,110,111,146,147,158,159,169,170,182,183,],[-91,-91,-91,-91,-50,-92,-47,-54,-107,-92,-94,-95,-93,-96,-26,139,-26,-28,-29,-27,-30,-53,-105,-105,-103,-103,-52,-51,-48,-49,]),'EXISTS':([94,],[127,]),'SENTENCE':([6,10,40,72,187,],[12,12,12,12,12,]),'SEARCH':([94,],[126,]),'EQUAL':([60,92,196,],[-92,121,212,]),'WRITE':([15,34,39,41,42,44,45,47,49,50,51,55,56,59,60,61,62,63,65,66,67,68,69,70,75,76,77,79,80,82,85,92,104,105,107,108,110,111,117,146,147,150,151,152,158,159,164,165,169,170,171,173,174,177,179,182,183,185,191,193,194,202,210,215,216,217,224,225,227,231,232,235,],[-15,57,-18,-16,-91,-91,-91,-91,-39,-10,-8,-50,-40,-42,-92,-37,-38,-47,-54,-45,57,-9,-36,-35,-92,-19,-94,-95,-93,-96,-5,-26,-26,-28,-29,-27,-30,-53,-109,-105,-105,-41,-109,-109,-103,-103,57,-17,-52,-51,-12,-43,-44,-20,-70,-48,-49,-107,57,-11,-111,-46,-55,-22,-69,-118,-21,-23,-57,-58,-113,-56,]),'FUNC':([5,9,11,15,39,41,76,165,229,234,],[10,10,10,-15,-18,-16,-19,-17,-60,-59,]),'COMA':([28,33,42,44,45,47,55,56,59,63,65,66,75,77,79,80,82,103,104,105,107,108,110,111,116,117,123,140,142,146,147,149,150,151,152,158,159,163,169,170,173,174,182,183,185,198,202,218,228,],[-87,40,-91,-91,-91,-91,-50,-40,-42,-47,-54,-45,-92,-94,-95,-93,-96,-88,-26,-28,-29,-27,-30,-53,-99,-109,156,-87,40,-105,-105,172,-41,-109,-109,-103,-103,187,-52,-51,-43,-44,-48,-49,-107,214,-46,-88,187,]),'NUMBERCTE':([15,32,34,38,39,41,42,44,45,47,48,49,50,51,55,56,58,59,60,61,62,63,65,66,67,68,69,70,75,76,77,79,80,82,84,85,86,87,88,89,90,91,92,93,95,96,104,105,107,108,110,111,113,114,117,118,119,120,121,136,137,138,139,146,147,150,151,152,153,154,156,157,158,159,161,162,164,165,166,169,170,171,172,173,174,176,177,179,182,183,185,186,191,193,194,202,210,212,214,215,216,217,224,225,227,231,232,235,],[-15,-86,42,42,-18,-16,-91,-91,-91,-91,42,-39,-10,-8,-50,-40,-108,-42,-92,-37,-38,-47,-54,-45,42,-9,-36,-35,-92,-19,-94,-95,-93,-96,42,-5,-104,-104,42,42,-108,-108,-26,42,-102,-102,-26,-28,-29,-27,-30,-53,42,42,-109,42,42,-86,-100,42,42,42,-106,-105,-105,-41,-109,-109,42,42,42,42,-103,-103,42,-86,42,-17,42,-52,-51,-12,42,-43,-44,42,-20,-70,-48,-49,-107,42,42,-11,-111,-46,-55,42,42,-22,-69,-118,-21,-23,-57,-58,-113,-56,]),'ELSE':([85,194,],[-5,211,]),'ID':([1,12,13,14,15,16,17,20,21,22,24,25,26,27,32,34,38,39,41,42,44,45,47,48,49,50,51,55,56,58,59,60,61,62,63,65,66,67,68,69,70,75,76,77,79,80,81,82,84,85,86,87,88,89,90,91,92,93,95,96,100,104,105,107,108,110,111,113,114,117,118,119,120,121,136,137,138,139,146,147,150,151,152,153,154,156,157,158,159,161,162,164,165,166,169,170,171,172,173,174,176,177,179,182,183,185,186,191,193,194,202,205,210,212,214,215,216,217,224,225,227,231,232,235,],[3,-90,-90,-90,-15,-90,28,-61,-62,30,-34,-32,-31,-33,-86,60,75,-18,-16,-91,-91,-91,-91,75,-39,-10,-8,-50,-40,-108,-42,-92,-37,-38,-47,-54,-45,60,-9,-36,-35,-92,-19,-94,-95,-93,109,-96,75,-5,-104,-104,75,75,-108,-108,-26,75,-102,-102,140,-26,-28,-29,-27,-30,-53,75,75,-109,75,75,-86,-100,75,75,75,-106,-105,-105,-41,-109,-109,75,75,75,75,-103,-103,75,-86,60,-17,75,-52,-51,-12,75,-43,-44,75,-20,-70,-48,-49,-107,75,60,-11,-111,-46,219,-55,75,75,-22,-69,-118,-21,-23,-57,-58,-113,-56,]),'IF':([15,34,39,41,42,44,45,47,49,50,51,55,56,59,60,61,62,63,65,66,67,68,69,70,75,76,77,79,80,82,85,92,104,105,107,108,110,111,117,146,147,150,151,152,158,159,164,165,169,170,171,173,174,177,179,182,183,185,191,193,194,202,210,215,216,217,224,225,227,231,232,235,],[-15,52,-18,-16,-91,-91,-91,-91,-39,-10,-8,-50,-40,-42,-92,-37,-38,-47,-54,-45,52,-9,-36,-35,-92,-19,-94,-95,-93,-96,-5,-26,-26,-28,-29,-27,-30,-53,-109,-105,-105,-41,-109,-109,-103,-103,52,-17,-52,-51,-12,-43,-44,-20,-70,-48,-49,-107,52,-11,-111,-46,-55,-22,-69,-118,-21,-23,-57,-58,-113,-56,]),'AND':([42,44,45,47,55,59,60,63,65,66,75,77,79,80,82,92,104,105,107,108,110,111,146,147,158,159,169,170,182,183,185,202,],[-91,-91,-91,-91,-50,90,-92,-47,-54,-45,-92,-94,-95,-93,-96,-26,-26,-28,-29,-27,-30,-53,-105,-105,-103,-103,-52,-51,-48,-49,-107,-46,]),'OPENBRAC':([28,60,92,140,],[32,-92,120,162,]),'MODE':([94,],[133,]),'REMOVE':([94,],[125,]),'LENGTH':([94,],[131,]),'FREQUENCY':([94,],[132,]),'BOOL':([6,10,40,72,187,],[14,14,14,14,14,]),'WORDCTE':([15,32,34,38,39,41,42,44,45,47,48,49,50,51,55,56,58,59,60,61,62,63,65,66,67,68,69,70,75,76,77,79,80,82,84,85,86,87,88,89,90,91,92,93,95,96,104,105,107,108,110,111,113,114,117,118,119,120,121,136,137,138,139,146,147,150,151,152,153,154,156,157,158,159,161,162,164,165,166,169,170,171,172,173,174,176,177,179,182,183,185,186,191,193,194,202,210,212,214,215,216,217,224,225,227,231,232,235,],[-15,-86,44,44,-18,-16,-91,-91,-91,-91,44,-39,-10,-8,-50,-40,-108,-42,-92,-37,-38,-47,-54,-45,44,-9,-36,-35,-92,-19,-94,-95,-93,-96,44,-5,-104,-104,44,44,-108,-108,-26,44,-102,-102,-26,-28,-29,-27,-30,-53,44,44,-109,44,44,-86,-100,44,44,44,-106,-105,-105,-41,-109,-109,44,44,44,44,-103,-103,44,-86,44,-17,44,-52,-51,-12,44,-43,-44,44,-20,-70,-48,-49,-107,44,44,-11,-111,-46,-55,44,44,-22,-69,-118,-21,-23,-57,-58,-113,-56,]),'NOT':([15,34,39,41,42,44,45,47,48,49,50,51,55,56,59,60,61,62,63,65,66,67,68,69,70,75,76,77,79,80,82,84,85,88,92,104,105,107,108,110,111,117,138,146,147,150,151,152,158,159,164,165,166,169,170,171,172,173,174,177,179,182,183,185,191,193,194,202,210,215,216,217,224,225,227,231,232,235,],[-15,58,-18,-16,-91,-91,-91,-91,58,-39,-10,-8,-50,-40,-42,-92,-37,-38,-47,-54,-45,58,-9,-36,-35,-92,-19,-94,-95,-93,-96,58,-5,58,-26,-26,-28,-29,-27,-30,-53,-109,58,-105,-105,-41,-109,-109,-103,-103,58,-17,58,-52,-51,-12,58,-43,-44,-20,-70,-48,-49,-107,58,-11,-111,-46,-55,-22,-69,-118,-21,-23,-57,-58,-113,-56,]),'CLOSEBRAC':([42,44,45,47,74,75,77,79,80,82,104,105,107,108,110,175,203,],[-91,-91,-91,-91,103,-92,-94,-95,-93,-96,-26,-28,-29,-27,-30,196,218,]),'MEAN':([94,],[135,]),'OR':([42,44,45,47,55,59,60,63,65,66,75,77,79,80,82,92,104,105,107,108,110,111,146,147,158,159,169,170,182,183,185,202,],[-91,-91,-91,-91,-50,91,-92,-47,-54,-45,-92,-94,-95,-93,-96,-26,-26,-28,-29,-27,-30,-53,-105,-105,-103,-103,-52,-51,-48,-49,-107,-46,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'func_read':([109,],[144,]),'func_isSize':([32,120,162,],[38,153,186,]),'spaux':([93,156,157,],[122,180,181,]),'func_declare_function':([30,],[36,]),'func_endIf':([194,],[210,]),'func_endDoWhile':([209,],[222,]),'outputaux':([88,172,],[115,195,]),'func_endElse':([232,],[235,]),'func_if':([145,],[168,]),'func_term':([158,159,],[182,183,]),'func_logicOP':([117,151,152,],[150,173,174,]),'assiaux':([176,214,],[197,226,]),'special':([94,],[134,]),'func_else':([211,],[223,]),'returnaux':([190,208,],[206,221,]),'func_endWhile':([217,],[227,]),'func_factor_operation':([86,87,],[113,114,]),'func_print':([116,],[149,]),'func_wordCte':([79,],[107,]),'funcaux':([10,],[22,]),'start':([0,],[2,]),'callfunction':([34,67,164,191,],[49,49,49,49,]),'func_do':([43,],[78,]),'startaux':([5,9,11,],[7,19,23,]),'factor':([34,48,67,84,88,89,113,114,118,119,136,137,138,154,161,164,166,172,176,191,212,214,],[55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,]),'input':([34,67,164,191,],[51,51,51,51,]),'declareaux':([33,142,],[41,165,]),'func_declare_var':([28,140,],[33,163,]),'type':([6,10,40,72,187,],[17,20,17,100,100,]),'func_relop':([66,185,],[98,202,]),'empty':([5,9,11,34,67,93,156,157,163,164,190,191,208,228,],[8,8,8,53,53,124,124,124,189,53,207,53,207,189,]),'blockaux':([34,67,164,191,],[54,99,190,208,]),'function':([5,9,11,],[9,9,9,]),'statement':([34,67,164,191,],[50,50,50,50,]),'func_numberCte':([77,],[105,]),'func_type':([12,13,14,16,],[24,25,26,27,]),'func_constantID':([60,75,],[92,104,]),'parameteraux':([163,228,],[188,233,]),'func_logicOp_operation':([58,90,91,],[89,118,119,]),'logexpression':([34,48,67,84,88,89,118,119,138,164,166,172,191,],[56,56,56,56,56,117,151,152,56,56,56,56,56,]),'func_while':([64,],[97,]),'func_sentenceCte':([82,],[110,]),'func_constant':([42,44,45,47,],[77,79,80,82,]),'func_whileExp':([184,],[201,]),'func_term_operation':([95,96,],[136,137,]),'func_assign_value':([178,],[199,]),'func_boolCte':([80,],[108,]),'relopexpression':([34,48,67,84,88,89,118,119,138,164,166,172,191,],[59,59,59,59,59,59,59,59,59,59,59,59,59,]),'parameter':([72,187,],[101,204,]),'condition':([34,67,164,191,],[61,61,61,61,]),'cycle':([34,67,164,191,],[62,62,62,62,]),'term':([34,48,67,84,88,89,113,114,118,119,136,137,138,154,161,164,166,172,176,191,212,214,],[63,63,63,63,63,63,146,147,63,63,63,63,63,63,63,63,63,63,63,63,63,63,]),'func_assign':([121,],[154,]),'func_start':([3,],[4,]),'func_factor':([146,147,],[169,170,]),'func_declare_array':([103,218,],[142,228,]),'assign':([34,67,164,191,],[70,70,70,70,]),'cte':([34,38,48,67,84,88,89,93,113,114,118,119,136,137,138,153,154,156,157,161,164,166,172,176,186,191,212,214,],[65,74,65,65,65,65,65,123,65,65,65,65,65,65,65,175,65,123,123,65,65,65,65,65,203,65,65,65,]),'decaux':([6,40,],[15,76,]),'assignaux':([154,212,],[177,224,]),'exp':([34,48,67,84,88,89,118,119,136,137,138,154,161,164,166,172,176,191,212,214,],[66,66,66,66,66,66,66,66,158,159,66,178,185,66,66,66,198,66,178,198,]),'action':([34,67,164,191,],[67,67,67,67,]),'output':([34,67,164,191,],[68,68,68,68,]),'func_begin_main':([18,31,],[29,37,]),'expression':([34,48,67,84,88,138,164,166,172,191,],[69,83,69,112,116,160,69,192,116,69,]),'declare':([5,164,],[11,191,]),'block':([29,37,78,168,201,223,],[35,73,106,194,217,232,]),'func_relop_operation':([139,],[161,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> KOTOBA ID func_start ENDSTMT declare startaux BEGIN func_begin_main block END','start',10,'p_start','YaccKotoba.py',11),
  ('start -> KOTOBA ID func_start ENDSTMT startaux BEGIN func_begin_main block END','start',9,'p_start','YaccKotoba.py',12),
  ('startaux -> function startaux','startaux',2,'p_startaux','YaccKotoba.py',24),
  ('startaux -> empty','startaux',1,'p_startaux','YaccKotoba.py',25),
  ('block -> OPENCURL blockaux CLOSECURL','block',3,'p_block','YaccKotoba.py',28),
  ('blockaux -> action blockaux','blockaux',2,'p_blockaux','YaccKotoba.py',31),
  ('blockaux -> empty','blockaux',1,'p_blockaux','YaccKotoba.py',32),
  ('action -> input','action',1,'p_action','YaccKotoba.py',35),
  ('action -> output','action',1,'p_action','YaccKotoba.py',36),
  ('action -> statement','action',1,'p_action','YaccKotoba.py',37),
  ('input -> READ OPENPAREN ID func_read CLOSEPAREN ENDSTMT','input',6,'p_input','YaccKotoba.py',40),
  ('output -> WRITE OPENPAREN outputaux CLOSEPAREN ENDSTMT','output',5,'p_output','YaccKotoba.py',43),
  ('outputaux -> expression func_print','outputaux',2,'p_outputaux','YaccKotoba.py',46),
  ('outputaux -> expression func_print COMA outputaux','outputaux',4,'p_outputaux','YaccKotoba.py',47),
  ('declare -> DEC decaux','declare',2,'p_declare','YaccKotoba.py',50),
  ('decaux -> type ID func_declare_var declareaux','decaux',4,'p_decaux','YaccKotoba.py',53),
  ('decaux -> type ID OPENBRAC func_isSize cte CLOSEBRAC func_declare_array declareaux','decaux',8,'p_decaux','YaccKotoba.py',54),
  ('declareaux -> ENDSTMT','declareaux',1,'p_declareaux','YaccKotoba.py',57),
  ('declareaux -> COMA decaux','declareaux',2,'p_declareaux','YaccKotoba.py',58),
  ('assign -> ID func_constantID EQUAL func_assign assignaux','assign',5,'p_assign','YaccKotoba.py',61),
  ('assign -> ID func_constantID OPENBRAC func_isSize cte CLOSEBRAC EQUAL assignaux','assign',8,'p_assign','YaccKotoba.py',62),
  ('assignaux -> exp func_assign_value ENDSTMT','assignaux',3,'p_assignaux','YaccKotoba.py',65),
  ('assignaux -> OPENCURL assiaux CLOSECURL ENDSTMT','assignaux',4,'p_assignaux','YaccKotoba.py',66),
  ('assiaux -> exp','assiaux',1,'p_assiaux','YaccKotoba.py',69),
  ('assiaux -> exp COMA assiaux','assiaux',3,'p_assiaux','YaccKotoba.py',70),
  ('cte -> ID func_constantID','cte',2,'p_cte','YaccKotoba.py',73),
  ('cte -> BOOLCTE func_constant func_boolCte','cte',3,'p_cte','YaccKotoba.py',74),
  ('cte -> NUMBERCTE func_constant func_numberCte','cte',3,'p_cte','YaccKotoba.py',75),
  ('cte -> WORDCTE func_constant func_wordCte','cte',3,'p_cte','YaccKotoba.py',76),
  ('cte -> SENTENCECTE func_constant func_sentenceCte','cte',3,'p_cte','YaccKotoba.py',77),
  ('type -> BOOL func_type','type',2,'p_type','YaccKotoba.py',80),
  ('type -> NUMBER func_type','type',2,'p_type','YaccKotoba.py',81),
  ('type -> WORD func_type','type',2,'p_type','YaccKotoba.py',82),
  ('type -> SENTENCE func_type','type',2,'p_type','YaccKotoba.py',83),
  ('statement -> assign','statement',1,'p_statement','YaccKotoba.py',86),
  ('statement -> expression','statement',1,'p_statement','YaccKotoba.py',87),
  ('statement -> condition','statement',1,'p_statement','YaccKotoba.py',88),
  ('statement -> cycle','statement',1,'p_statement','YaccKotoba.py',89),
  ('statement -> callfunction','statement',1,'p_statement','YaccKotoba.py',90),
  ('expression -> logexpression','expression',1,'p_expression','YaccKotoba.py',93),
  ('expression -> NOT func_logicOp_operation logexpression func_logicOP','expression',4,'p_expression','YaccKotoba.py',94),
  ('logexpression -> relopexpression','logexpression',1,'p_logexpression','YaccKotoba.py',97),
  ('logexpression -> relopexpression AND func_logicOp_operation logexpression func_logicOP','logexpression',5,'p_logexpression','YaccKotoba.py',98),
  ('logexpression -> relopexpression OR func_logicOp_operation logexpression func_logicOP','logexpression',5,'p_logexpression','YaccKotoba.py',99),
  ('relopexpression -> exp','relopexpression',1,'p_relopexression','YaccKotoba.py',102),
  ('relopexpression -> exp func_relop RELOP func_relop_operation exp func_relop','relopexpression',6,'p_relopexression','YaccKotoba.py',103),
  ('exp -> term','exp',1,'p_exp','YaccKotoba.py',106),
  ('exp -> term PLUS func_term_operation exp func_term','exp',5,'p_exp','YaccKotoba.py',107),
  ('exp -> term MINUS func_term_operation exp func_term','exp',5,'p_exp','YaccKotoba.py',108),
  ('term -> factor','term',1,'p_term','YaccKotoba.py',111),
  ('term -> factor MULT func_factor_operation term func_factor','term',5,'p_term','YaccKotoba.py',112),
  ('term -> factor DIV func_factor_operation term func_factor','term',5,'p_term','YaccKotoba.py',113),
  ('factor -> OPENPAREN expression CLOSEPAREN','factor',3,'p_factor','YaccKotoba.py',116),
  ('factor -> cte','factor',1,'p_factor','YaccKotoba.py',117),
  ('condition -> IF OPENPAREN expression CLOSEPAREN func_if block func_endIf','condition',7,'p_condition','YaccKotoba.py',120),
  ('condition -> IF OPENPAREN expression CLOSEPAREN func_if block ELSE func_else block func_endElse','condition',10,'p_condition','YaccKotoba.py',121),
  ('cycle -> WHILE func_while OPENPAREN expression CLOSEPAREN func_whileExp block func_endWhile','cycle',8,'p_cycle','YaccKotoba.py',124),
  ('cycle -> DO func_do block WHILE OPENPAREN expression CLOSEPAREN func_endDoWhile ENDSTMT','cycle',9,'p_cycle','YaccKotoba.py',125),
  ('function -> FUNC funcaux ID func_declare_function OPENPAREN parameter CLOSEPAREN OPENCURL declare blockaux returnaux ENDSTMT CLOSECURL','function',13,'p_function','YaccKotoba.py',128),
  ('function -> FUNC funcaux ID func_declare_function OPENPAREN parameter CLOSEPAREN OPENCURL blockaux returnaux ENDSTMT CLOSECURL','function',12,'p_function','YaccKotoba.py',129),
  ('funcaux -> type','funcaux',1,'p_funcaux','YaccKotoba.py',132),
  ('funcaux -> VOID','funcaux',1,'p_funcaux','YaccKotoba.py',133),
  ('parameter -> type ID func_declare_var parameteraux','parameter',4,'p_parameter','YaccKotoba.py',136),
  ('parameter -> type ID OPENBRAC func_isSize cte CLOSEBRAC func_declare_array parameteraux','parameter',8,'p_parameter','YaccKotoba.py',137),
  ('parameteraux -> COMA parameter','parameteraux',2,'p_parameteraux','YaccKotoba.py',140),
  ('parameteraux -> empty','parameteraux',1,'p_parameteraux','YaccKotoba.py',141),
  ('returnaux -> RETURN ID','returnaux',2,'p_returnaux','YaccKotoba.py',144),
  ('returnaux -> empty','returnaux',1,'p_returnaux','YaccKotoba.py',145),
  ('callfunction -> ID DOT special OPENPAREN spaux CLOSEPAREN ENDSTMT','callfunction',7,'p_callfunction','YaccKotoba.py',148),
  ('callfunction -> ID OPENPAREN spaux CLOSEPAREN ENDSTMT','callfunction',5,'p_callfunction','YaccKotoba.py',149),
  ('spaux -> cte','spaux',1,'p_spaux','YaccKotoba.py',152),
  ('spaux -> cte COMA spaux','spaux',3,'p_spaux','YaccKotoba.py',153),
  ('spaux -> empty','spaux',1,'p_spaux','YaccKotoba.py',154),
  ('special -> LENGTH','special',1,'p_special','YaccKotoba.py',157),
  ('special -> FREQUENCY','special',1,'p_special','YaccKotoba.py',158),
  ('special -> SEARCH','special',1,'p_special','YaccKotoba.py',159),
  ('special -> EXISTS','special',1,'p_special','YaccKotoba.py',160),
  ('special -> MEAN','special',1,'p_special','YaccKotoba.py',161),
  ('special -> MEDIAN','special',1,'p_special','YaccKotoba.py',162),
  ('special -> MODE','special',1,'p_special','YaccKotoba.py',163),
  ('special -> WORDCOUNT','special',1,'p_special','YaccKotoba.py',164),
  ('special -> TOKENIZE','special',1,'p_special','YaccKotoba.py',165),
  ('special -> REMOVE','special',1,'p_special','YaccKotoba.py',166),
  ('empty -> <empty>','empty',0,'p_empty','YaccKotoba.py',169),
  ('func_start -> <empty>','func_start',0,'p_func_start','YaccKotoba.py',176),
  ('func_isSize -> <empty>','func_isSize',0,'p_func_isSize','YaccKotoba.py',189),
  ('func_declare_var -> <empty>','func_declare_var',0,'p_func_declare_var','YaccKotoba.py',194),
  ('func_declare_array -> <empty>','func_declare_array',0,'p_func_declare_array','YaccKotoba.py',201),
  ('func_declare_function -> <empty>','func_declare_function',0,'p_func_declare_function','YaccKotoba.py',210),
  ('func_type -> <empty>','func_type',0,'p_func_type','YaccKotoba.py',218),
  ('func_constant -> <empty>','func_constant',0,'p_func_constant','YaccKotoba.py',223),
  ('func_constantID -> <empty>','func_constantID',0,'p_func_constantID','YaccKotoba.py',230),
  ('func_boolCte -> <empty>','func_boolCte',0,'p_func_boolCte','YaccKotoba.py',241),
  ('func_numberCte -> <empty>','func_numberCte',0,'p_func_numberCte','YaccKotoba.py',246),
  ('func_wordCte -> <empty>','func_wordCte',0,'p_func_wordCte','YaccKotoba.py',251),
  ('func_sentenceCte -> <empty>','func_sentenceCte',0,'p_func_sentenceCte','YaccKotoba.py',256),
  ('func_begin_main -> <empty>','func_begin_main',0,'p_func_begin_main','YaccKotoba.py',263),
  ('func_read -> <empty>','func_read',0,'p_func_read','YaccKotoba.py',270),
  ('func_print -> <empty>','func_print',0,'p_func_print','YaccKotoba.py',282),
  ('func_assign -> <empty>','func_assign',0,'p_func_assign','YaccKotoba.py',291),
  ('func_assign_value -> <empty>','func_assign_value',0,'p_func_assign_value','YaccKotoba.py',295),
  ('func_term_operation -> <empty>','func_term_operation',0,'p_func_term_operation','YaccKotoba.py',316),
  ('func_term -> <empty>','func_term',0,'p_func_term','YaccKotoba.py',323),
  ('func_factor_operation -> <empty>','func_factor_operation',0,'p_func_factor_operation','YaccKotoba.py',345),
  ('func_factor -> <empty>','func_factor',0,'p_func_factor','YaccKotoba.py',352),
  ('func_relop_operation -> <empty>','func_relop_operation',0,'p_func_relop_operation','YaccKotoba.py',375),
  ('func_relop -> <empty>','func_relop',0,'p_func_relop','YaccKotoba.py',386),
  ('func_logicOp_operation -> <empty>','func_logicOp_operation',0,'p_func_logicOp_operation','YaccKotoba.py',409),
  ('func_logicOP -> <empty>','func_logicOP',0,'p_func_logicOP','YaccKotoba.py',418),
  ('func_if -> <empty>','func_if',0,'p_func_if','YaccKotoba.py',457),
  ('func_endIf -> <empty>','func_endIf',0,'p_func_endIf','YaccKotoba.py',470),
  ('func_else -> <empty>','func_else',0,'p_func_else','YaccKotoba.py',475),
  ('func_endElse -> <empty>','func_endElse',0,'p_func_endElse','YaccKotoba.py',486),
  ('func_do -> <empty>','func_do',0,'p_func_do','YaccKotoba.py',492),
  ('func_endDoWhile -> <empty>','func_endDoWhile',0,'p_func_endDoWhile','YaccKotoba.py',496),
  ('func_while -> <empty>','func_while',0,'p_func_while','YaccKotoba.py',510),
  ('func_whileExp -> <empty>','func_whileExp',0,'p_func_whileExp','YaccKotoba.py',514),
  ('func_endWhile -> <empty>','func_endWhile',0,'p_func_endWhile','YaccKotoba.py',528),
  ('func_clear -> <empty>','func_clear',0,'p_func_clear','YaccKotoba.py',541),
]