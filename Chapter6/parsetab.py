
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND BEGIN BOOL BOOLCTE CALL CLOSEBRAC CLOSECURL CLOSEPAREN COMA DEC DIV DO DOT ELSE END ENDSTMT EQUAL EXISTS FREQUENCY FUNC ID IF KOTOBA LENGTH MEAN MEDIAN MINUS MODE MULT NOT NUMBER NUMBERCTE OPENBRAC OPENCURL OPENPAREN OR PLUS READ RELOP REMOVE RETURN SEARCH SENTENCE SENTENCECTE TOKENIZE VOID WHILE WORD WORDCOUNT WORDCTE WRITEstart : KOTOBA ID func_start ENDSTMT declare startaux BEGIN func_begin_main block END\n\t| KOTOBA ID func_start ENDSTMT startaux BEGIN func_begin_main block ENDstartaux : function startaux\n\t| emptyblock : OPENCURL blockaux CLOSECURLblockaux : action blockaux\n\t| emptyaction : input\n\t| output\n\t| statementinput : READ OPENPAREN ID func_read CLOSEPAREN ENDSTMToutput : WRITE OPENPAREN outputaux CLOSEPAREN ENDSTMToutputaux : expression func_print\n\t| expression func_print COMA outputauxdeclare : DEC decauxdecaux : type ID func_declare_var declareaux\n\t| type ID OPENBRAC func_isSize cte CLOSEBRAC func_declare_array declareauxdeclareaux : ENDSTMT\n\t| COMA decauxassign : ID func_constantID EQUAL func_assign assignaux\n\t| ID func_constantID OPENBRAC func_isSize cte CLOSEBRAC EQUAL assignauxassignaux : exp func_assign_value ENDSTMT\n\t| OPENCURL assiaux CLOSECURL ENDSTMTassiaux : exp\n\t| exp COMA assiauxcte : ID func_constantID\n\t| BOOLCTE func_boolCte func_constant \n\t| NUMBERCTE func_numberCte func_constant \n\t| WORDCTE func_wordCte func_constant \n\t| SENTENCECTE func_sentenceCte func_constanttype : BOOL func_type\n\t| NUMBER func_type\n\t| WORD func_type\n\t| SENTENCE func_typestatement : assign\n\t| expression\n\t| condition\n\t| cycle\n\t| callfunctionexpression : logexpression\n\t| NOT func_logicOp_operation logexpression func_logicOPlogexpression : relopexpression \n\t| relopexpression AND func_logicOp_operation logexpression func_logicOP\n\t| relopexpression OR func_logicOp_operation logexpression func_logicOPrelopexpression : exp \n\t| exp func_relop RELOP func_relop_operation exp func_relopexp : term\n\t| term PLUS func_term_operation exp func_term\n\t| term MINUS func_term_operation exp func_termterm : factor\n\t| factor MULT func_factor_operation term func_factor\n\t| factor DIV func_factor_operation term func_factorfactor : OPENPAREN expression CLOSEPAREN\n\t| ctecondition : IF OPENPAREN expression CLOSEPAREN func_if block func_endIf \n\t|  IF OPENPAREN expression CLOSEPAREN func_if block ELSE func_else block func_endElsecycle : WHILE func_while OPENPAREN expression CLOSEPAREN func_whileExp block func_endWhile\n\t| DO func_do block WHILE OPENPAREN expression CLOSEPAREN func_endDoWhile ENDSTMTfunction : FUNC funcaux ID func_declare_function OPENPAREN parameter CLOSEPAREN OPENCURL declare blockaux returnaux ENDSTMT CLOSECURL func_clear\n\t| FUNC funcaux ID func_declare_function OPENPAREN parameter CLOSEPAREN OPENCURL blockaux returnaux ENDSTMT CLOSECURL func_clearfuncaux : type\n\t| VOIDparameter : type ID func_declare_par parameteraux\n\t| type ID OPENBRAC func_isSize cte CLOSEBRAC func_declare_array parameterauxparameteraux : COMA parameter\n\t| emptyreturnaux : RETURN ID\n\t| emptycallfunction : CALL ID DOT special OPENPAREN spaux CLOSEPAREN ENDSTMT\n\t| CALL ID func_callFunc OPENPAREN spaux CLOSEPAREN func_endCallFunction ENDSTMTspaux : cte func_callFuncParameter  \n\t| cte func_callFuncParameter COMA spaux\n\t| emptyspecial : LENGTH  \n\t| FREQUENCY\n    | SEARCH\n    | EXISTS\n    | MEAN\n\t| MEDIAN\n\t| MODE\n\t| WORDCOUNT\n\t| TOKENIZE\n\t| REMOVEempty : func_start :func_isSize : func_declare_var : func_declare_array : func_declare_par : func_declare_function : func_type : func_constant : func_constantID : func_boolCte : func_numberCte : func_wordCte : func_sentenceCte : func_begin_main : func_read : func_print : func_assign : func_assign_value : func_term_operation : func_term : func_factor_operation : func_factor : func_relop_operation : func_relop : func_logicOp_operation : func_logicOP : func_if : func_endIf : func_else : func_endElse : func_do : func_endDoWhile : func_while : func_whileExp : func_endWhile : func_callFunc : func_callFuncParameter : func_endCallFunction : func_clear : '
    
_lr_action_items = {'DO':([15,34,39,41,42,44,45,47,49,50,51,55,56,59,60,61,62,63,65,67,68,69,70,71,76,77,78,80,81,83,86,93,104,105,107,108,110,111,117,134,135,138,139,140,143,144,161,162,166,167,168,170,171,174,176,177,183,189,191,192,202,210,215,216,226,227,229,230,231,236,237,241,],[-15,43,-18,-16,-95,-96,-94,-97,-39,-10,-8,-50,-40,-42,-93,-37,-38,-47,-54,-45,43,-9,-36,-35,-93,-19,-92,-92,-92,-92,-5,-26,-26,-28,-29,-27,-30,-53,-110,-106,-106,-41,-110,-110,-104,-104,43,-17,-52,-51,-12,-43,-44,-20,-48,-49,-108,43,-11,-112,-46,-55,-22,-119,-21,-23,-57,-69,-70,-58,-114,-56,]),'RETURN':([15,39,41,42,44,45,47,49,50,51,53,55,56,59,60,61,62,63,65,67,68,69,70,71,76,77,78,80,81,83,86,93,99,104,105,107,108,110,111,117,134,135,138,139,140,143,144,161,162,166,167,168,170,171,174,176,177,183,188,189,191,192,202,208,210,215,216,226,227,229,230,231,236,237,241,],[-15,-18,-16,-95,-96,-94,-97,-39,-10,-8,-7,-50,-40,-42,-93,-37,-38,-47,-54,-45,-84,-9,-36,-35,-93,-19,-92,-92,-92,-92,-5,-26,-6,-26,-28,-29,-27,-30,-53,-110,-106,-106,-41,-110,-110,-104,-104,-84,-17,-52,-51,-12,-43,-44,-20,-48,-49,-108,205,-84,-11,-112,-46,205,-55,-22,-119,-21,-23,-57,-69,-70,-58,-114,-56,]),'BOOLCTE':([15,32,34,38,39,41,42,44,45,47,48,49,50,51,55,56,58,59,60,61,62,63,65,67,68,69,70,71,76,77,78,80,81,83,85,86,87,88,89,90,91,92,93,94,95,104,105,107,108,110,111,113,114,117,118,119,120,121,122,123,124,127,134,135,138,139,140,141,142,143,144,157,158,160,161,162,163,166,167,168,169,170,171,173,174,176,177,179,183,187,189,191,192,202,210,212,214,215,216,219,226,227,229,230,231,236,237,241,],[-15,-86,45,45,-18,-16,-95,-96,-94,-97,45,-39,-10,-8,-50,-40,-109,-42,-93,-37,-38,-47,-54,-45,45,-9,-36,-35,-93,-19,-92,-92,-92,-92,45,-5,-105,-105,45,45,-109,-109,-26,-103,-103,-26,-28,-29,-27,-30,-53,45,45,-110,45,45,-86,-101,45,45,45,-107,-106,-106,-41,-110,-110,45,45,-104,-104,45,45,-86,45,-17,45,-52,-51,-12,45,-43,-44,45,-20,-48,-49,45,-108,45,45,-11,-112,-46,-55,45,45,-22,-119,45,-21,-23,-57,-69,-70,-58,-114,-56,]),'READ':([15,34,39,41,42,44,45,47,49,50,51,55,56,59,60,61,62,63,65,67,68,69,70,71,76,77,78,80,81,83,86,93,104,105,107,108,110,111,117,134,135,138,139,140,143,144,161,162,166,167,168,170,171,174,176,177,183,189,191,192,202,210,215,216,226,227,229,230,231,236,237,241,],[-15,46,-18,-16,-95,-96,-94,-97,-39,-10,-8,-50,-40,-42,-93,-37,-38,-47,-54,-45,46,-9,-36,-35,-93,-19,-92,-92,-92,-92,-5,-26,-26,-28,-29,-27,-30,-53,-110,-106,-106,-41,-110,-110,-104,-104,46,-17,-52,-51,-12,-43,-44,-20,-48,-49,-108,46,-11,-112,-46,-55,-22,-119,-21,-23,-57,-69,-70,-58,-114,-56,]),'MEDIAN':([125,],[150,]),'VOID':([10,],[21,]),'NUMBER':([6,10,40,73,184,],[13,13,13,13,13,]),'ENDSTMT':([3,4,15,28,33,39,41,42,44,45,47,49,50,51,53,55,56,59,60,61,62,63,65,67,68,69,70,71,76,77,78,80,81,83,86,93,99,103,104,105,107,108,110,111,117,130,134,135,136,138,139,140,143,144,161,162,164,166,167,168,170,171,174,175,176,177,183,188,189,191,192,197,200,202,206,207,208,209,210,213,215,216,217,218,221,223,224,226,227,229,230,231,236,237,241,],[-85,5,-15,-87,39,-18,-16,-95,-96,-94,-97,-39,-10,-8,-7,-50,-40,-42,-93,-37,-38,-47,-54,-45,-84,-9,-36,-35,-93,-19,-92,-92,-92,-92,-5,-26,-6,-88,-26,-28,-29,-27,-30,-53,-110,39,-106,-106,168,-41,-110,-110,-104,-104,-84,-17,191,-52,-51,-12,-43,-44,-20,-102,-48,-49,-108,-84,-84,-11,-112,215,-122,-46,222,-68,-84,-116,-55,227,-22,-119,230,231,-67,235,236,-21,-23,-57,-69,-70,-58,-114,-56,]),'WHILE':([15,34,39,41,42,44,45,47,49,50,51,55,56,59,60,61,62,63,65,67,68,69,70,71,76,77,78,80,81,83,86,93,104,105,106,107,108,110,111,117,134,135,138,139,140,143,144,161,162,166,167,168,170,171,174,176,177,183,189,191,192,202,210,215,216,226,227,229,230,231,236,237,241,],[-15,64,-18,-16,-95,-96,-94,-97,-39,-10,-8,-50,-40,-42,-93,-37,-38,-47,-54,-45,64,-9,-36,-35,-93,-19,-92,-92,-92,-92,-5,-26,-26,-28,131,-29,-27,-30,-53,-110,-106,-106,-41,-110,-110,-104,-104,64,-17,-52,-51,-12,-43,-44,-20,-48,-49,-108,64,-11,-112,-46,-55,-22,-119,-21,-23,-57,-69,-70,-58,-114,-56,]),'SENTENCECTE':([15,32,34,38,39,41,42,44,45,47,48,49,50,51,55,56,58,59,60,61,62,63,65,67,68,69,70,71,76,77,78,80,81,83,85,86,87,88,89,90,91,92,93,94,95,104,105,107,108,110,111,113,114,117,118,119,120,121,122,123,124,127,134,135,138,139,140,141,142,143,144,157,158,160,161,162,163,166,167,168,169,170,171,173,174,176,177,179,183,187,189,191,192,202,210,212,214,215,216,219,226,227,229,230,231,236,237,241,],[-15,-86,47,47,-18,-16,-95,-96,-94,-97,47,-39,-10,-8,-50,-40,-109,-42,-93,-37,-38,-47,-54,-45,47,-9,-36,-35,-93,-19,-92,-92,-92,-92,47,-5,-105,-105,47,47,-109,-109,-26,-103,-103,-26,-28,-29,-27,-30,-53,47,47,-110,47,47,-86,-101,47,47,47,-107,-106,-106,-41,-110,-110,47,47,-104,-104,47,47,-86,47,-17,47,-52,-51,-12,47,-43,-44,47,-20,-48,-49,47,-108,47,47,-11,-112,-46,-55,47,47,-22,-119,47,-21,-23,-57,-69,-70,-58,-114,-56,]),'DIV':([42,44,45,47,55,60,65,76,78,80,81,83,93,104,105,107,108,110,111,],[-95,-96,-94,-97,87,-93,-54,-93,-92,-92,-92,-92,-26,-26,-28,-29,-27,-30,-53,]),'DEC':([5,161,],[6,6,]),'OPENPAREN':([15,30,34,36,39,41,42,44,45,46,47,48,49,50,51,52,55,56,57,58,59,60,61,62,63,64,65,67,68,69,70,71,76,77,78,80,81,83,85,86,87,88,89,90,91,92,93,94,95,96,97,104,105,107,108,110,111,113,114,117,118,119,121,122,123,124,126,127,131,134,135,138,139,140,142,143,144,146,147,148,149,150,151,152,153,154,155,156,158,161,162,163,166,167,168,169,170,171,173,174,176,177,183,189,191,192,202,210,212,214,215,216,226,227,229,230,231,236,237,241,],[-15,-90,48,73,-18,-16,-95,-96,-94,82,-97,48,-39,-10,-8,85,-50,-40,89,-109,-42,-93,-37,-38,-47,-117,-54,-45,48,-9,-36,-35,-93,-19,-92,-92,-92,-92,48,-5,-105,-105,48,48,-109,-109,-26,-103,-103,124,-120,-26,-28,-29,-27,-30,-53,48,48,-110,48,48,-101,48,48,48,157,-107,163,-106,-106,-41,-110,-110,48,-104,-104,-83,-76,-77,-81,-79,-82,-74,-75,-80,179,-78,48,48,-17,48,-52,-51,-12,48,-43,-44,48,-20,-48,-49,-108,48,-11,-112,-46,-55,48,48,-22,-119,-21,-23,-57,-69,-70,-58,-114,-56,]),'MULT':([42,44,45,47,55,60,65,76,78,80,81,83,93,104,105,107,108,110,111,],[-95,-96,-94,-97,88,-93,-54,-93,-92,-92,-92,-92,-26,-26,-28,-29,-27,-30,-53,]),'BEGIN':([5,7,8,9,11,15,19,23,39,41,77,162,234,239,240,242,],[-84,18,-4,-84,-84,-15,-3,31,-18,-16,-19,-17,-123,-60,-123,-59,]),'WORD':([6,10,40,73,184,],[16,16,16,16,16,]),'CLOSEPAREN':([42,44,45,47,55,56,59,63,65,67,76,78,80,81,83,84,101,104,105,107,108,109,110,111,112,115,116,117,128,132,134,135,137,138,139,140,143,144,145,157,159,166,167,170,171,176,177,179,180,181,182,183,185,186,190,193,199,201,202,203,219,220,232,233,238,],[-95,-96,-94,-97,-50,-40,-42,-47,-54,-45,-93,-92,-92,-92,-92,111,129,-26,-28,-29,-27,-99,-30,-53,133,136,-100,-110,-89,164,-106,-106,-13,-41,-110,-110,-104,-104,178,-84,-84,-52,-51,-43,-44,-48,-49,-84,200,-121,-73,-108,-63,-66,209,-14,217,-71,-46,-65,-84,-88,-72,-84,-64,]),'WORDCOUNT':([125,],[149,]),'OPENCURL':([18,29,31,37,43,79,121,129,133,142,165,178,198,211,212,225,],[-98,34,-98,34,-115,34,-101,161,-111,173,34,-118,34,-113,173,34,]),'MINUS':([42,44,45,47,55,60,63,65,76,78,80,81,83,93,104,105,107,108,110,111,134,135,166,167,],[-95,-96,-94,-97,-50,-93,95,-54,-93,-92,-92,-92,-92,-26,-26,-28,-29,-27,-30,-53,-106,-106,-52,-51,]),'KOTOBA':([0,],[1,]),'PLUS':([42,44,45,47,55,60,63,65,76,78,80,81,83,93,104,105,107,108,110,111,134,135,166,167,],[-95,-96,-94,-97,-50,-93,94,-54,-93,-92,-92,-92,-92,-26,-26,-28,-29,-27,-30,-53,-106,-106,-52,-51,]),'DOT':([97,],[125,]),'TOKENIZE':([125,],[151,]),'BOOL':([6,10,40,73,184,],[14,14,14,14,14,]),'$end':([2,72,102,],[0,-2,-1,]),'CLOSECURL':([34,42,44,45,47,49,50,51,53,54,55,56,59,60,61,62,63,65,67,68,69,70,71,76,78,80,81,83,86,93,99,104,105,107,108,110,111,117,134,135,138,139,140,143,144,166,167,168,170,171,174,176,177,183,191,192,195,196,202,210,215,216,222,226,227,228,229,230,231,235,236,237,241,],[-84,-95,-96,-94,-97,-39,-10,-8,-7,86,-50,-40,-42,-93,-37,-38,-47,-54,-45,-84,-9,-36,-35,-93,-92,-92,-92,-92,-5,-26,-6,-26,-28,-29,-27,-30,-53,-110,-106,-106,-41,-110,-110,-104,-104,-52,-51,-12,-43,-44,-20,-48,-49,-108,-11,-112,213,-24,-46,-55,-22,-119,234,-21,-23,-25,-57,-69,-70,240,-58,-114,-56,]),'END':([35,74,86,],[72,102,-5,]),'RELOP':([42,44,45,47,55,60,63,65,67,76,78,80,81,83,93,98,104,105,107,108,110,111,134,135,143,144,166,167,176,177,],[-95,-96,-94,-97,-50,-93,-47,-54,-108,-93,-92,-92,-92,-92,-26,127,-26,-28,-29,-27,-30,-53,-106,-106,-104,-104,-52,-51,-48,-49,]),'EXISTS':([125,],[148,]),'SENTENCE':([6,10,40,73,184,],[12,12,12,12,12,]),'SEARCH':([125,],[147,]),'EQUAL':([60,93,194,],[-93,121,212,]),'WRITE':([15,34,39,41,42,44,45,47,49,50,51,55,56,59,60,61,62,63,65,67,68,69,70,71,76,77,78,80,81,83,86,93,104,105,107,108,110,111,117,134,135,138,139,140,143,144,161,162,166,167,168,170,171,174,176,177,183,189,191,192,202,210,215,216,226,227,229,230,231,236,237,241,],[-15,57,-18,-16,-95,-96,-94,-97,-39,-10,-8,-50,-40,-42,-93,-37,-38,-47,-54,-45,57,-9,-36,-35,-93,-19,-92,-92,-92,-92,-5,-26,-26,-28,-29,-27,-30,-53,-110,-106,-106,-41,-110,-110,-104,-104,57,-17,-52,-51,-12,-43,-44,-20,-48,-49,-108,57,-11,-112,-46,-55,-22,-119,-21,-23,-57,-69,-70,-58,-114,-56,]),'FUNC':([5,9,11,15,39,41,77,162,234,239,240,242,],[10,10,10,-15,-18,-16,-19,-17,-123,-60,-123,-59,]),'COMA':([28,33,42,44,45,47,55,56,59,63,65,67,76,78,80,81,83,103,104,105,107,108,110,111,116,117,128,130,134,135,137,138,139,140,143,144,159,166,167,170,171,176,177,181,183,196,201,202,220,233,],[-87,40,-95,-96,-94,-97,-50,-40,-42,-47,-54,-45,-93,-92,-92,-92,-92,-88,-26,-28,-29,-27,-30,-53,-100,-110,-89,40,-106,-106,169,-41,-110,-110,-104,-104,184,-52,-51,-43,-44,-48,-49,-121,-108,214,219,-46,-88,184,]),'NUMBERCTE':([15,32,34,38,39,41,42,44,45,47,48,49,50,51,55,56,58,59,60,61,62,63,65,67,68,69,70,71,76,77,78,80,81,83,85,86,87,88,89,90,91,92,93,94,95,104,105,107,108,110,111,113,114,117,118,119,120,121,122,123,124,127,134,135,138,139,140,141,142,143,144,157,158,160,161,162,163,166,167,168,169,170,171,173,174,176,177,179,183,187,189,191,192,202,210,212,214,215,216,219,226,227,229,230,231,236,237,241,],[-15,-86,42,42,-18,-16,-95,-96,-94,-97,42,-39,-10,-8,-50,-40,-109,-42,-93,-37,-38,-47,-54,-45,42,-9,-36,-35,-93,-19,-92,-92,-92,-92,42,-5,-105,-105,42,42,-109,-109,-26,-103,-103,-26,-28,-29,-27,-30,-53,42,42,-110,42,42,-86,-101,42,42,42,-107,-106,-106,-41,-110,-110,42,42,-104,-104,42,42,-86,42,-17,42,-52,-51,-12,42,-43,-44,42,-20,-48,-49,42,-108,42,42,-11,-112,-46,-55,42,42,-22,-119,42,-21,-23,-57,-69,-70,-58,-114,-56,]),'ELSE':([86,192,],[-5,211,]),'ID':([1,12,13,14,15,16,17,20,21,22,24,25,26,27,32,34,38,39,41,42,44,45,47,48,49,50,51,55,56,58,59,60,61,62,63,65,66,67,68,69,70,71,76,77,78,80,81,82,83,85,86,87,88,89,90,91,92,93,94,95,100,104,105,107,108,110,111,113,114,117,118,119,120,121,122,123,124,127,134,135,138,139,140,141,142,143,144,157,158,160,161,162,163,166,167,168,169,170,171,173,174,176,177,179,183,187,189,191,192,202,205,210,212,214,215,216,219,226,227,229,230,231,236,237,241,],[3,-91,-91,-91,-15,-91,28,-61,-62,30,-34,-32,-31,-33,-86,60,76,-18,-16,-95,-96,-94,-97,76,-39,-10,-8,-50,-40,-109,-42,-93,-37,-38,-47,-54,97,-45,60,-9,-36,-35,-93,-19,-92,-92,-92,109,-92,76,-5,-105,-105,76,76,-109,-109,-26,-103,-103,128,-26,-28,-29,-27,-30,-53,76,76,-110,76,76,-86,-101,76,76,76,-107,-106,-106,-41,-110,-110,76,76,-104,-104,76,76,-86,60,-17,76,-52,-51,-12,76,-43,-44,76,-20,-48,-49,76,-108,76,60,-11,-112,-46,221,-55,76,76,-22,-119,76,-21,-23,-57,-69,-70,-58,-114,-56,]),'IF':([15,34,39,41,42,44,45,47,49,50,51,55,56,59,60,61,62,63,65,67,68,69,70,71,76,77,78,80,81,83,86,93,104,105,107,108,110,111,117,134,135,138,139,140,143,144,161,162,166,167,168,170,171,174,176,177,183,189,191,192,202,210,215,216,226,227,229,230,231,236,237,241,],[-15,52,-18,-16,-95,-96,-94,-97,-39,-10,-8,-50,-40,-42,-93,-37,-38,-47,-54,-45,52,-9,-36,-35,-93,-19,-92,-92,-92,-92,-5,-26,-26,-28,-29,-27,-30,-53,-110,-106,-106,-41,-110,-110,-104,-104,52,-17,-52,-51,-12,-43,-44,-20,-48,-49,-108,52,-11,-112,-46,-55,-22,-119,-21,-23,-57,-69,-70,-58,-114,-56,]),'AND':([42,44,45,47,55,59,60,63,65,67,76,78,80,81,83,93,104,105,107,108,110,111,134,135,143,144,166,167,176,177,183,202,],[-95,-96,-94,-97,-50,91,-93,-47,-54,-45,-93,-92,-92,-92,-92,-26,-26,-28,-29,-27,-30,-53,-106,-106,-104,-104,-52,-51,-48,-49,-108,-46,]),'OPENBRAC':([28,60,93,128,],[32,-93,120,160,]),'MODE':([125,],[154,]),'REMOVE':([125,],[146,]),'LENGTH':([125,],[152,]),'FREQUENCY':([125,],[153,]),'CALL':([15,34,39,41,42,44,45,47,49,50,51,55,56,59,60,61,62,63,65,67,68,69,70,71,76,77,78,80,81,83,86,93,104,105,107,108,110,111,117,134,135,138,139,140,143,144,161,162,166,167,168,170,171,174,176,177,183,189,191,192,202,210,215,216,226,227,229,230,231,236,237,241,],[-15,66,-18,-16,-95,-96,-94,-97,-39,-10,-8,-50,-40,-42,-93,-37,-38,-47,-54,-45,66,-9,-36,-35,-93,-19,-92,-92,-92,-92,-5,-26,-26,-28,-29,-27,-30,-53,-110,-106,-106,-41,-110,-110,-104,-104,66,-17,-52,-51,-12,-43,-44,-20,-48,-49,-108,66,-11,-112,-46,-55,-22,-119,-21,-23,-57,-69,-70,-58,-114,-56,]),'WORDCTE':([15,32,34,38,39,41,42,44,45,47,48,49,50,51,55,56,58,59,60,61,62,63,65,67,68,69,70,71,76,77,78,80,81,83,85,86,87,88,89,90,91,92,93,94,95,104,105,107,108,110,111,113,114,117,118,119,120,121,122,123,124,127,134,135,138,139,140,141,142,143,144,157,158,160,161,162,163,166,167,168,169,170,171,173,174,176,177,179,183,187,189,191,192,202,210,212,214,215,216,219,226,227,229,230,231,236,237,241,],[-15,-86,44,44,-18,-16,-95,-96,-94,-97,44,-39,-10,-8,-50,-40,-109,-42,-93,-37,-38,-47,-54,-45,44,-9,-36,-35,-93,-19,-92,-92,-92,-92,44,-5,-105,-105,44,44,-109,-109,-26,-103,-103,-26,-28,-29,-27,-30,-53,44,44,-110,44,44,-86,-101,44,44,44,-107,-106,-106,-41,-110,-110,44,44,-104,-104,44,44,-86,44,-17,44,-52,-51,-12,44,-43,-44,44,-20,-48,-49,44,-108,44,44,-11,-112,-46,-55,44,44,-22,-119,44,-21,-23,-57,-69,-70,-58,-114,-56,]),'NOT':([15,34,39,41,42,44,45,47,48,49,50,51,55,56,59,60,61,62,63,65,67,68,69,70,71,76,77,78,80,81,83,85,86,89,93,104,105,107,108,110,111,117,124,134,135,138,139,140,143,144,161,162,163,166,167,168,169,170,171,174,176,177,183,189,191,192,202,210,215,216,226,227,229,230,231,236,237,241,],[-15,58,-18,-16,-95,-96,-94,-97,58,-39,-10,-8,-50,-40,-42,-93,-37,-38,-47,-54,-45,58,-9,-36,-35,-93,-19,-92,-92,-92,-92,58,-5,58,-26,-26,-28,-29,-27,-30,-53,-110,58,-106,-106,-41,-110,-110,-104,-104,58,-17,58,-52,-51,-12,58,-43,-44,-20,-48,-49,-108,58,-11,-112,-46,-55,-22,-119,-21,-23,-57,-69,-70,-58,-114,-56,]),'CLOSEBRAC':([42,44,45,47,75,76,78,80,81,83,104,105,107,108,110,172,204,],[-95,-96,-94,-97,103,-93,-92,-92,-92,-92,-26,-28,-29,-27,-30,194,220,]),'MEAN':([125,],[156,]),'OR':([42,44,45,47,55,59,60,63,65,67,76,78,80,81,83,93,104,105,107,108,110,111,134,135,143,144,166,167,176,177,183,202,],[-95,-96,-94,-97,-50,92,-93,-47,-54,-45,-93,-92,-92,-92,-92,-26,-26,-28,-29,-27,-30,-53,-106,-106,-104,-104,-52,-51,-48,-49,-108,-46,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'func_read':([109,],[132,]),'func_isSize':([32,120,160,],[38,141,187,]),'spaux':([157,179,219,],[180,199,232,]),'func_declare_function':([30,],[36,]),'func_endIf':([192,],[210,]),'func_endDoWhile':([209,],[224,]),'outputaux':([89,169,],[115,193,]),'func_endElse':([237,],[241,]),'func_clear':([234,240,],[239,242,]),'func_if':([133,],[165,]),'func_endCallFunction':([200,],[218,]),'func_term':([143,144,],[176,177,]),'func_logicOP':([117,139,140,],[138,170,171,]),'assiaux':([173,214,],[195,228,]),'special':([125,],[155,]),'func_else':([211,],[225,]),'returnaux':([188,208,],[206,223,]),'func_endWhile':([216,],[229,]),'func_factor_operation':([87,88,],[113,114,]),'func_print':([116,],[137,]),'func_wordCte':([44,],[80,]),'funcaux':([10,],[22,]),'start':([0,],[2,]),'callfunction':([34,68,161,189,],[49,49,49,49,]),'func_do':([43,],[79,]),'startaux':([5,9,11,],[7,19,23,]),'factor':([34,48,68,85,89,90,113,114,118,119,122,123,124,142,158,161,163,169,173,189,212,214,],[55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,]),'input':([34,68,161,189,],[51,51,51,51,]),'declareaux':([33,130,],[41,162,]),'func_declare_var':([28,],[33,]),'type':([6,10,40,73,184,],[17,20,17,100,100,]),'func_relop':([67,183,],[98,202,]),'empty':([5,9,11,34,68,157,159,161,179,188,189,208,219,233,],[8,8,8,53,53,182,186,53,182,207,53,207,182,186,]),'blockaux':([34,68,161,189,],[54,99,188,208,]),'function':([5,9,11,],[9,9,9,]),'func_declare_par':([128,],[159,]),'statement':([34,68,161,189,],[50,50,50,50,]),'func_numberCte':([42,],[78,]),'func_type':([12,13,14,16,],[24,25,26,27,]),'func_constantID':([60,76,],[93,104,]),'parameteraux':([159,233,],[185,238,]),'func_logicOp_operation':([58,91,92,],[90,118,119,]),'logexpression':([34,48,68,85,89,90,118,119,124,161,163,169,189,],[56,56,56,56,56,117,139,140,56,56,56,56,56,]),'func_while':([64,],[96,]),'func_sentenceCte':([47,],[83,]),'func_constant':([78,80,81,83,],[105,107,108,110,]),'func_whileExp':([178,],[198,]),'func_term_operation':([94,95,],[122,123,]),'func_callFunc':([97,],[126,]),'func_boolCte':([45,],[81,]),'relopexpression':([34,48,68,85,89,90,118,119,124,161,163,169,189,],[59,59,59,59,59,59,59,59,59,59,59,59,59,]),'parameter':([73,184,],[101,203,]),'func_assign_value':([175,],[197,]),'condition':([34,68,161,189,],[61,61,61,61,]),'cycle':([34,68,161,189,],[62,62,62,62,]),'term':([34,48,68,85,89,90,113,114,118,119,122,123,124,142,158,161,163,169,173,189,212,214,],[63,63,63,63,63,63,134,135,63,63,63,63,63,63,63,63,63,63,63,63,63,63,]),'func_assign':([121,],[142,]),'func_start':([3,],[4,]),'func_callFuncParameter':([181,],[201,]),'func_factor':([134,135,],[166,167,]),'func_declare_array':([103,220,],[130,233,]),'assign':([34,68,161,189,],[71,71,71,71,]),'cte':([34,38,48,68,85,89,90,113,114,118,119,122,123,124,141,142,157,158,161,163,169,173,179,187,189,212,214,219,],[65,75,65,65,65,65,65,65,65,65,65,65,65,65,172,65,181,65,65,65,65,65,181,204,65,65,65,181,]),'decaux':([6,40,],[15,77,]),'assignaux':([142,212,],[174,226,]),'exp':([34,48,68,85,89,90,118,119,122,123,124,142,158,161,163,169,173,189,212,214,],[67,67,67,67,67,67,67,67,143,144,67,175,183,67,67,67,196,67,175,196,]),'action':([34,68,161,189,],[68,68,68,68,]),'output':([34,68,161,189,],[69,69,69,69,]),'func_begin_main':([18,31,],[29,37,]),'expression':([34,48,68,85,89,124,161,163,169,189,],[70,84,70,112,116,145,70,190,116,70,]),'declare':([5,161,],[11,189,]),'block':([29,37,79,165,198,225,],[35,74,106,192,216,237,]),'func_relop_operation':([127,],[158,]),}

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
  ('startaux -> function startaux','startaux',2,'p_startaux','YaccKotoba.py',30),
  ('startaux -> empty','startaux',1,'p_startaux','YaccKotoba.py',31),
  ('block -> OPENCURL blockaux CLOSECURL','block',3,'p_block','YaccKotoba.py',34),
  ('blockaux -> action blockaux','blockaux',2,'p_blockaux','YaccKotoba.py',37),
  ('blockaux -> empty','blockaux',1,'p_blockaux','YaccKotoba.py',38),
  ('action -> input','action',1,'p_action','YaccKotoba.py',41),
  ('action -> output','action',1,'p_action','YaccKotoba.py',42),
  ('action -> statement','action',1,'p_action','YaccKotoba.py',43),
  ('input -> READ OPENPAREN ID func_read CLOSEPAREN ENDSTMT','input',6,'p_input','YaccKotoba.py',46),
  ('output -> WRITE OPENPAREN outputaux CLOSEPAREN ENDSTMT','output',5,'p_output','YaccKotoba.py',49),
  ('outputaux -> expression func_print','outputaux',2,'p_outputaux','YaccKotoba.py',52),
  ('outputaux -> expression func_print COMA outputaux','outputaux',4,'p_outputaux','YaccKotoba.py',53),
  ('declare -> DEC decaux','declare',2,'p_declare','YaccKotoba.py',56),
  ('decaux -> type ID func_declare_var declareaux','decaux',4,'p_decaux','YaccKotoba.py',59),
  ('decaux -> type ID OPENBRAC func_isSize cte CLOSEBRAC func_declare_array declareaux','decaux',8,'p_decaux','YaccKotoba.py',60),
  ('declareaux -> ENDSTMT','declareaux',1,'p_declareaux','YaccKotoba.py',63),
  ('declareaux -> COMA decaux','declareaux',2,'p_declareaux','YaccKotoba.py',64),
  ('assign -> ID func_constantID EQUAL func_assign assignaux','assign',5,'p_assign','YaccKotoba.py',67),
  ('assign -> ID func_constantID OPENBRAC func_isSize cte CLOSEBRAC EQUAL assignaux','assign',8,'p_assign','YaccKotoba.py',68),
  ('assignaux -> exp func_assign_value ENDSTMT','assignaux',3,'p_assignaux','YaccKotoba.py',71),
  ('assignaux -> OPENCURL assiaux CLOSECURL ENDSTMT','assignaux',4,'p_assignaux','YaccKotoba.py',72),
  ('assiaux -> exp','assiaux',1,'p_assiaux','YaccKotoba.py',75),
  ('assiaux -> exp COMA assiaux','assiaux',3,'p_assiaux','YaccKotoba.py',76),
  ('cte -> ID func_constantID','cte',2,'p_cte','YaccKotoba.py',79),
  ('cte -> BOOLCTE func_boolCte func_constant','cte',3,'p_cte','YaccKotoba.py',80),
  ('cte -> NUMBERCTE func_numberCte func_constant','cte',3,'p_cte','YaccKotoba.py',81),
  ('cte -> WORDCTE func_wordCte func_constant','cte',3,'p_cte','YaccKotoba.py',82),
  ('cte -> SENTENCECTE func_sentenceCte func_constant','cte',3,'p_cte','YaccKotoba.py',83),
  ('type -> BOOL func_type','type',2,'p_type','YaccKotoba.py',86),
  ('type -> NUMBER func_type','type',2,'p_type','YaccKotoba.py',87),
  ('type -> WORD func_type','type',2,'p_type','YaccKotoba.py',88),
  ('type -> SENTENCE func_type','type',2,'p_type','YaccKotoba.py',89),
  ('statement -> assign','statement',1,'p_statement','YaccKotoba.py',92),
  ('statement -> expression','statement',1,'p_statement','YaccKotoba.py',93),
  ('statement -> condition','statement',1,'p_statement','YaccKotoba.py',94),
  ('statement -> cycle','statement',1,'p_statement','YaccKotoba.py',95),
  ('statement -> callfunction','statement',1,'p_statement','YaccKotoba.py',96),
  ('expression -> logexpression','expression',1,'p_expression','YaccKotoba.py',99),
  ('expression -> NOT func_logicOp_operation logexpression func_logicOP','expression',4,'p_expression','YaccKotoba.py',100),
  ('logexpression -> relopexpression','logexpression',1,'p_logexpression','YaccKotoba.py',103),
  ('logexpression -> relopexpression AND func_logicOp_operation logexpression func_logicOP','logexpression',5,'p_logexpression','YaccKotoba.py',104),
  ('logexpression -> relopexpression OR func_logicOp_operation logexpression func_logicOP','logexpression',5,'p_logexpression','YaccKotoba.py',105),
  ('relopexpression -> exp','relopexpression',1,'p_relopexression','YaccKotoba.py',108),
  ('relopexpression -> exp func_relop RELOP func_relop_operation exp func_relop','relopexpression',6,'p_relopexression','YaccKotoba.py',109),
  ('exp -> term','exp',1,'p_exp','YaccKotoba.py',112),
  ('exp -> term PLUS func_term_operation exp func_term','exp',5,'p_exp','YaccKotoba.py',113),
  ('exp -> term MINUS func_term_operation exp func_term','exp',5,'p_exp','YaccKotoba.py',114),
  ('term -> factor','term',1,'p_term','YaccKotoba.py',117),
  ('term -> factor MULT func_factor_operation term func_factor','term',5,'p_term','YaccKotoba.py',118),
  ('term -> factor DIV func_factor_operation term func_factor','term',5,'p_term','YaccKotoba.py',119),
  ('factor -> OPENPAREN expression CLOSEPAREN','factor',3,'p_factor','YaccKotoba.py',122),
  ('factor -> cte','factor',1,'p_factor','YaccKotoba.py',123),
  ('condition -> IF OPENPAREN expression CLOSEPAREN func_if block func_endIf','condition',7,'p_condition','YaccKotoba.py',126),
  ('condition -> IF OPENPAREN expression CLOSEPAREN func_if block ELSE func_else block func_endElse','condition',10,'p_condition','YaccKotoba.py',127),
  ('cycle -> WHILE func_while OPENPAREN expression CLOSEPAREN func_whileExp block func_endWhile','cycle',8,'p_cycle','YaccKotoba.py',130),
  ('cycle -> DO func_do block WHILE OPENPAREN expression CLOSEPAREN func_endDoWhile ENDSTMT','cycle',9,'p_cycle','YaccKotoba.py',131),
  ('function -> FUNC funcaux ID func_declare_function OPENPAREN parameter CLOSEPAREN OPENCURL declare blockaux returnaux ENDSTMT CLOSECURL func_clear','function',14,'p_function','YaccKotoba.py',134),
  ('function -> FUNC funcaux ID func_declare_function OPENPAREN parameter CLOSEPAREN OPENCURL blockaux returnaux ENDSTMT CLOSECURL func_clear','function',13,'p_function','YaccKotoba.py',135),
  ('funcaux -> type','funcaux',1,'p_funcaux','YaccKotoba.py',138),
  ('funcaux -> VOID','funcaux',1,'p_funcaux','YaccKotoba.py',139),
  ('parameter -> type ID func_declare_par parameteraux','parameter',4,'p_parameter','YaccKotoba.py',142),
  ('parameter -> type ID OPENBRAC func_isSize cte CLOSEBRAC func_declare_array parameteraux','parameter',8,'p_parameter','YaccKotoba.py',143),
  ('parameteraux -> COMA parameter','parameteraux',2,'p_parameteraux','YaccKotoba.py',146),
  ('parameteraux -> empty','parameteraux',1,'p_parameteraux','YaccKotoba.py',147),
  ('returnaux -> RETURN ID','returnaux',2,'p_returnaux','YaccKotoba.py',150),
  ('returnaux -> empty','returnaux',1,'p_returnaux','YaccKotoba.py',151),
  ('callfunction -> CALL ID DOT special OPENPAREN spaux CLOSEPAREN ENDSTMT','callfunction',8,'p_callfunction','YaccKotoba.py',154),
  ('callfunction -> CALL ID func_callFunc OPENPAREN spaux CLOSEPAREN func_endCallFunction ENDSTMT','callfunction',8,'p_callfunction','YaccKotoba.py',155),
  ('spaux -> cte func_callFuncParameter','spaux',2,'p_spaux','YaccKotoba.py',158),
  ('spaux -> cte func_callFuncParameter COMA spaux','spaux',4,'p_spaux','YaccKotoba.py',159),
  ('spaux -> empty','spaux',1,'p_spaux','YaccKotoba.py',160),
  ('special -> LENGTH','special',1,'p_special','YaccKotoba.py',163),
  ('special -> FREQUENCY','special',1,'p_special','YaccKotoba.py',164),
  ('special -> SEARCH','special',1,'p_special','YaccKotoba.py',165),
  ('special -> EXISTS','special',1,'p_special','YaccKotoba.py',166),
  ('special -> MEAN','special',1,'p_special','YaccKotoba.py',167),
  ('special -> MEDIAN','special',1,'p_special','YaccKotoba.py',168),
  ('special -> MODE','special',1,'p_special','YaccKotoba.py',169),
  ('special -> WORDCOUNT','special',1,'p_special','YaccKotoba.py',170),
  ('special -> TOKENIZE','special',1,'p_special','YaccKotoba.py',171),
  ('special -> REMOVE','special',1,'p_special','YaccKotoba.py',172),
  ('empty -> <empty>','empty',0,'p_empty','YaccKotoba.py',175),
  ('func_start -> <empty>','func_start',0,'p_func_start','YaccKotoba.py',182),
  ('func_isSize -> <empty>','func_isSize',0,'p_func_isSize','YaccKotoba.py',194),
  ('func_declare_var -> <empty>','func_declare_var',0,'p_func_declare_var','YaccKotoba.py',199),
  ('func_declare_array -> <empty>','func_declare_array',0,'p_func_declare_array','YaccKotoba.py',204),
  ('func_declare_par -> <empty>','func_declare_par',0,'p_func_declare_par','YaccKotoba.py',211),
  ('func_declare_function -> <empty>','func_declare_function',0,'p_func_declare_function','YaccKotoba.py',219),
  ('func_type -> <empty>','func_type',0,'p_func_type','YaccKotoba.py',226),
  ('func_constant -> <empty>','func_constant',0,'p_func_constant','YaccKotoba.py',231),
  ('func_constantID -> <empty>','func_constantID',0,'p_func_constantID','YaccKotoba.py',246),
  ('func_boolCte -> <empty>','func_boolCte',0,'p_func_boolCte','YaccKotoba.py',263),
  ('func_numberCte -> <empty>','func_numberCte',0,'p_func_numberCte','YaccKotoba.py',268),
  ('func_wordCte -> <empty>','func_wordCte',0,'p_func_wordCte','YaccKotoba.py',273),
  ('func_sentenceCte -> <empty>','func_sentenceCte',0,'p_func_sentenceCte','YaccKotoba.py',278),
  ('func_begin_main -> <empty>','func_begin_main',0,'p_func_begin_main','YaccKotoba.py',285),
  ('func_read -> <empty>','func_read',0,'p_func_read','YaccKotoba.py',293),
  ('func_print -> <empty>','func_print',0,'p_func_print','YaccKotoba.py',312),
  ('func_assign -> <empty>','func_assign',0,'p_func_assign','YaccKotoba.py',321),
  ('func_assign_value -> <empty>','func_assign_value',0,'p_func_assign_value','YaccKotoba.py',325),
  ('func_term_operation -> <empty>','func_term_operation',0,'p_func_term_operation','YaccKotoba.py',346),
  ('func_term -> <empty>','func_term',0,'p_func_term','YaccKotoba.py',353),
  ('func_factor_operation -> <empty>','func_factor_operation',0,'p_func_factor_operation','YaccKotoba.py',374),
  ('func_factor -> <empty>','func_factor',0,'p_func_factor','YaccKotoba.py',381),
  ('func_relop_operation -> <empty>','func_relop_operation',0,'p_func_relop_operation','YaccKotoba.py',403),
  ('func_relop -> <empty>','func_relop',0,'p_func_relop','YaccKotoba.py',414),
  ('func_logicOp_operation -> <empty>','func_logicOp_operation',0,'p_func_logicOp_operation','YaccKotoba.py',436),
  ('func_logicOP -> <empty>','func_logicOP',0,'p_func_logicOP','YaccKotoba.py',445),
  ('func_if -> <empty>','func_if',0,'p_func_if','YaccKotoba.py',482),
  ('func_endIf -> <empty>','func_endIf',0,'p_func_endIf','YaccKotoba.py',495),
  ('func_else -> <empty>','func_else',0,'p_func_else','YaccKotoba.py',500),
  ('func_endElse -> <empty>','func_endElse',0,'p_func_endElse','YaccKotoba.py',511),
  ('func_do -> <empty>','func_do',0,'p_func_do','YaccKotoba.py',517),
  ('func_endDoWhile -> <empty>','func_endDoWhile',0,'p_func_endDoWhile','YaccKotoba.py',521),
  ('func_while -> <empty>','func_while',0,'p_func_while','YaccKotoba.py',535),
  ('func_whileExp -> <empty>','func_whileExp',0,'p_func_whileExp','YaccKotoba.py',539),
  ('func_endWhile -> <empty>','func_endWhile',0,'p_func_endWhile','YaccKotoba.py',553),
  ('func_callFunc -> <empty>','func_callFunc',0,'p_func_callFunc','YaccKotoba.py',564),
  ('func_callFuncParameter -> <empty>','func_callFuncParameter',0,'p_func_callFuncParameter','YaccKotoba.py',576),
  ('func_endCallFunction -> <empty>','func_endCallFunction',0,'p_func_endCallFunction','YaccKotoba.py',589),
  ('func_clear -> <empty>','func_clear',0,'p_func_clear','YaccKotoba.py',601),
]
