
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND BEGIN BOOL BOOLCTE CLOSEBRAC CLOSECURL CLOSEPAREN COMA DEC DIV DO DOT ELSE END ENDSTMT EQUAL EXISTS FREQUENCY FUNC ID IF KOTOBA LENGTH MEAN MEDIAN MINUS MODE MULT NOT NUMBER NUMBERCTE OPENBRAC OPENCURL OPENPAREN OR PLUS READ RELOP REMOVE RETURN SEARCH SENTENCE SENTENCECTE TOKENIZE VOID WHILE WORD WORDCOUNT WORDCTE WRITEstart : KOTOBA ID func_start ENDSTMT declare startaux BEGIN func_begin_main block END\n\t| KOTOBA ID func_start ENDSTMT startaux BEGIN func_begin_main block ENDstartaux : function startaux\n\t| emptyblock : OPENCURL blockaux CLOSECURLblockaux : action blockaux\n\t| emptyaction : input\n\t| output\n\t| statementinput : READ OPENPAREN ID func_read CLOSEPAREN ENDSTMToutput : WRITE OPENPAREN outputaux CLOSEPAREN ENDSTMToutputaux : expression func_print\n\t| expression func_print COMA outputauxdeclare : DEC decauxdecaux : type ID func_declare_var declareaux\n\t| type ID OPENBRAC func_isSize cte CLOSEBRAC func_declare_array declareauxdeclareaux : ENDSTMT\n\t| COMA decauxassign : ID func_constantID EQUAL func_assign assignaux\n\t| ID func_constantID OPENBRAC func_isSize cte CLOSEBRAC EQUAL assignauxassignaux : exp func_assign_value ENDSTMT\n\t| OPENCURL assiaux CLOSECURL ENDSTMTassiaux : exp\n\t| exp COMA assiauxcte : ID func_constantID\n\t| BOOLCTE func_constant func_boolCte\n\t| NUMBERCTE func_constant func_numberCte\n\t| WORDCTE func_constant func_wordCte\n\t| SENTENCECTE func_constant func_sentenceCtetype : BOOL func_type\n\t| NUMBER func_type\n\t| WORD func_type\n\t| SENTENCE func_typestatement : assign\n\t| expression\n\t| condition\n\t| cycle\n\t| callfunctionexpression : logexpression\n\t| NOT func_logicOp_operation logexpression func_logicOPlogexpression : relopexpression \n\t| relopexpression AND func_logicOp_operation logexpression func_logicOP\n\t| relopexpression OR func_logicOp_operation logexpression func_logicOPrelopexpression : exp \n\t| exp func_relop RELOP func_relop_operation exp func_relopexp : term\n\t| term PLUS func_term_operation exp func_term\n\t| term MINUS func_term_operation exp func_termterm : factor\n\t| factor MULT func_factor_operation term func_factor\n\t| factor DIV func_factor_operation term func_factorfactor : OPENPAREN expression CLOSEPAREN\n\t| ctecondition : IF OPENPAREN expression CLOSEPAREN func_if block func_endIf \n\t|  IF OPENPAREN expression CLOSEPAREN func_if block func_endIf ELSE func_else block func_endIfcycle : WHILE OPENPAREN expression CLOSEPAREN block\n\t| DO block WHILE OPENPAREN expression CLOSEPAREN ENDSTMTfunction : FUNC funcaux ID func_declare_function OPENPAREN parameter CLOSEPAREN OPENCURL declare blockaux returnaux ENDSTMT CLOSECURL func_clear\n\t| FUNC funcaux ID func_declare_function OPENPAREN parameter CLOSEPAREN OPENCURL blockaux returnaux ENDSTMT CLOSECURL func_clearfuncaux : type\n\t| VOIDparameter : type ID func_declare_var parameteraux\n\t| type ID OPENBRAC func_isSize cte CLOSEBRAC func_declare_array parameterauxparameteraux : COMA parameter\n\t| emptyreturnaux : RETURN ID\n\t| emptycallfunction : ID callaux OPENPAREN spaux CLOSEPAREN ENDSTMTcallaux : DOT special\n\t| emptyspaux : cte\n\t| cte COMA spaux\n\t| emptyspecial : LENGTH  \n\t| FREQUENCY\n    | SEARCH\n    | EXISTS\n    | MEAN\n\t| MEDIAN\n\t| MODE\n\t| WORDCOUNT\n\t| TOKENIZE\n\t| REMOVEempty : func_start :func_isSize : func_declare_var : func_declare_array : func_declare_function : func_type : func_constant : func_constantID : func_boolCte : func_numberCte : func_wordCte : func_sentenceCte : func_begin_main : func_read : func_print : func_assign : func_assign_value : func_term_operation : func_term : func_factor_operation : func_factor : func_relop_operation : func_relop : func_logicOp_operation : func_logicOP : func_if : func_endIf : func_else : func_clear : '
    
_lr_action_items = {'KOTOBA':([0,],[2,]),'$end':([1,39,74,],[0,-2,-1,]),'ID':([2,14,15,16,17,18,19,21,22,23,27,28,29,30,34,36,41,43,44,45,47,48,50,51,52,53,54,55,56,57,61,62,63,64,65,66,67,68,69,70,72,75,77,79,80,84,85,86,87,89,90,92,93,94,95,96,97,98,99,100,103,105,106,107,108,109,123,127,128,129,130,131,132,133,134,135,136,137,142,143,149,152,153,154,155,156,157,158,159,161,163,165,167,170,171,172,174,176,177,178,179,180,181,182,183,184,189,190,195,198,200,203,207,209,210,211,212,217,219,228,230,],[3,-15,26,-91,-91,-91,-91,31,-61,-62,-31,-32,-33,-34,48,-87,48,-8,-9,-10,79,-93,-35,-36,-37,-38,-39,-54,-40,-109,-42,-45,-47,-50,-92,-92,-92,-92,-16,-18,79,-5,104,-93,-26,79,79,79,79,-109,-109,-103,-103,-105,-105,-94,-95,-96,-97,-19,140,-53,-26,-101,-87,79,-110,79,79,-107,79,79,79,79,-27,-28,-29,-30,79,79,-41,79,-110,-110,79,-104,-104,-106,-106,48,-87,-20,79,79,-12,79,-57,-43,-44,-108,-48,-49,-51,-52,-17,48,79,-11,-69,-112,-46,215,-22,79,79,-55,-58,-23,-21,-112,-56,]),'ENDSTMT':([3,4,14,26,35,41,42,43,44,45,48,50,51,52,53,54,55,56,61,62,63,64,65,66,67,68,69,70,75,76,79,80,96,97,98,99,100,105,106,123,134,135,136,137,138,147,149,153,154,156,157,158,159,160,161,164,165,166,169,171,174,176,177,178,179,180,181,182,183,184,185,190,191,195,198,199,200,201,202,204,207,208,211,212,213,215,217,219,228,230,],[-86,5,-15,-88,70,-85,-7,-8,-9,-10,-93,-35,-36,-37,-38,-39,-54,-40,-42,-45,-47,-50,-92,-92,-92,-92,-16,-18,-5,-6,-93,-26,-94,-95,-96,-97,-19,-53,-26,-110,-27,-28,-29,-30,-89,171,-41,-110,-110,-104,-104,-106,-106,70,-85,190,-20,-102,195,-12,-57,-43,-44,-108,-48,-49,-51,-52,-17,-85,-85,-11,207,-69,-112,212,-46,-85,214,-68,-22,217,-55,-58,221,-67,-23,-21,-112,-56,]),'DEC':([5,161,],[8,8,]),'FUNC':([5,6,9,14,69,70,100,183,222,225,226,229,],[11,11,11,-15,-16,-18,-19,-17,-114,-114,-60,-59,]),'BEGIN':([5,6,7,9,10,12,14,20,69,70,100,183,222,225,226,229,],[-85,-85,13,-85,-4,24,-15,-3,-16,-18,-19,-17,-114,-114,-60,-59,]),'BOOL':([8,11,71,73,187,],[16,16,16,16,16,]),'NUMBER':([8,11,71,73,187,],[17,17,17,17,17,]),'WORD':([8,11,71,73,187,],[18,18,18,18,18,]),'SENTENCE':([8,11,71,73,187,],[19,19,19,19,19,]),'VOID':([11,],[23,]),'OPENCURL':([13,24,25,32,60,107,139,142,150,151,173,210,220,224,],[-98,-98,34,34,34,-101,161,167,-111,34,34,167,-113,34,]),'READ':([14,34,41,43,44,45,48,50,51,52,53,54,55,56,61,62,63,64,65,66,67,68,69,70,75,79,80,96,97,98,99,100,105,106,123,134,135,136,137,149,153,154,156,157,158,159,161,165,171,174,176,177,178,179,180,181,182,183,184,190,195,198,200,207,211,212,217,219,228,230,],[-15,46,46,-8,-9,-10,-93,-35,-36,-37,-38,-39,-54,-40,-42,-45,-47,-50,-92,-92,-92,-92,-16,-18,-5,-93,-26,-94,-95,-96,-97,-19,-53,-26,-110,-27,-28,-29,-30,-41,-110,-110,-104,-104,-106,-106,46,-20,-12,-57,-43,-44,-108,-48,-49,-51,-52,-17,46,-11,-69,-112,-46,-22,-55,-58,-23,-21,-112,-56,]),'WRITE':([14,34,41,43,44,45,48,50,51,52,53,54,55,56,61,62,63,64,65,66,67,68,69,70,75,79,80,96,97,98,99,100,105,106,123,134,135,136,137,149,153,154,156,157,158,159,161,165,171,174,176,177,178,179,180,181,182,183,184,190,195,198,200,207,211,212,217,219,228,230,],[-15,49,49,-8,-9,-10,-93,-35,-36,-37,-38,-39,-54,-40,-42,-45,-47,-50,-92,-92,-92,-92,-16,-18,-5,-93,-26,-94,-95,-96,-97,-19,-53,-26,-110,-27,-28,-29,-30,-41,-110,-110,-104,-104,-106,-106,49,-20,-12,-57,-43,-44,-108,-48,-49,-51,-52,-17,49,-11,-69,-112,-46,-22,-55,-58,-23,-21,-112,-56,]),'NOT':([14,34,41,43,44,45,47,48,50,51,52,53,54,55,56,61,62,63,64,65,66,67,68,69,70,75,79,80,84,86,87,96,97,98,99,100,105,106,123,134,135,136,137,149,152,153,154,156,157,158,159,161,165,171,172,174,176,177,178,179,180,181,182,183,184,190,195,198,200,207,211,212,217,219,228,230,],[-15,57,57,-8,-9,-10,57,-93,-35,-36,-37,-38,-39,-54,-40,-42,-45,-47,-50,-92,-92,-92,-92,-16,-18,-5,-93,-26,57,57,57,-94,-95,-96,-97,-19,-53,-26,-110,-27,-28,-29,-30,-41,57,-110,-110,-104,-104,-106,-106,57,-20,-12,57,-57,-43,-44,-108,-48,-49,-51,-52,-17,57,-11,-69,-112,-46,-22,-55,-58,-23,-21,-112,-56,]),'IF':([14,34,41,43,44,45,48,50,51,52,53,54,55,56,61,62,63,64,65,66,67,68,69,70,75,79,80,96,97,98,99,100,105,106,123,134,135,136,137,149,153,154,156,157,158,159,161,165,171,174,176,177,178,179,180,181,182,183,184,190,195,198,200,207,211,212,217,219,228,230,],[-15,58,58,-8,-9,-10,-93,-35,-36,-37,-38,-39,-54,-40,-42,-45,-47,-50,-92,-92,-92,-92,-16,-18,-5,-93,-26,-94,-95,-96,-97,-19,-53,-26,-110,-27,-28,-29,-30,-41,-110,-110,-104,-104,-106,-106,58,-20,-12,-57,-43,-44,-108,-48,-49,-51,-52,-17,58,-11,-69,-112,-46,-22,-55,-58,-23,-21,-112,-56,]),'WHILE':([14,34,41,43,44,45,48,50,51,52,53,54,55,56,61,62,63,64,65,66,67,68,69,70,75,79,80,88,96,97,98,99,100,105,106,123,134,135,136,137,149,153,154,156,157,158,159,161,165,171,174,176,177,178,179,180,181,182,183,184,190,195,198,200,207,211,212,217,219,228,230,],[-15,59,59,-8,-9,-10,-93,-35,-36,-37,-38,-39,-54,-40,-42,-45,-47,-50,-92,-92,-92,-92,-16,-18,-5,-93,-26,126,-94,-95,-96,-97,-19,-53,-26,-110,-27,-28,-29,-30,-41,-110,-110,-104,-104,-106,-106,59,-20,-12,-57,-43,-44,-108,-48,-49,-51,-52,-17,59,-11,-69,-112,-46,-22,-55,-58,-23,-21,-112,-56,]),'DO':([14,34,41,43,44,45,48,50,51,52,53,54,55,56,61,62,63,64,65,66,67,68,69,70,75,79,80,96,97,98,99,100,105,106,123,134,135,136,137,149,153,154,156,157,158,159,161,165,171,174,176,177,178,179,180,181,182,183,184,190,195,198,200,207,211,212,217,219,228,230,],[-15,60,60,-8,-9,-10,-93,-35,-36,-37,-38,-39,-54,-40,-42,-45,-47,-50,-92,-92,-92,-92,-16,-18,-5,-93,-26,-94,-95,-96,-97,-19,-53,-26,-110,-27,-28,-29,-30,-41,-110,-110,-104,-104,-106,-106,60,-20,-12,-57,-43,-44,-108,-48,-49,-51,-52,-17,60,-11,-69,-112,-46,-22,-55,-58,-23,-21,-112,-56,]),'OPENPAREN':([14,31,34,37,41,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,61,62,63,64,65,66,67,68,69,70,75,79,80,81,83,84,85,86,87,89,90,92,93,94,95,96,97,98,99,100,105,106,107,110,111,112,113,114,115,116,117,118,119,120,123,126,127,128,129,130,131,132,133,134,135,136,137,142,149,152,153,154,155,156,157,158,159,161,165,167,171,172,174,176,177,178,179,180,181,182,183,184,190,195,198,200,207,209,210,211,212,217,219,228,230,],[-15,-90,47,73,47,-8,-9,-10,77,47,-85,84,-35,-36,-37,-38,-39,-54,-40,-109,86,87,-42,-45,-47,-50,-92,-92,-92,-92,-16,-18,-5,-93,-26,109,-71,47,47,47,47,-109,-109,-103,-103,-105,-105,-94,-95,-96,-97,-19,-53,-26,-101,-70,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-110,152,47,47,-107,47,47,47,47,-27,-28,-29,-30,47,-41,47,-110,-110,47,-104,-104,-106,-106,47,-20,47,-12,47,-57,-43,-44,-108,-48,-49,-51,-52,-17,47,-11,-69,-112,-46,-22,47,47,-55,-58,-23,-21,-112,-56,]),'BOOLCTE':([14,34,36,41,43,44,45,47,48,50,51,52,53,54,55,56,57,61,62,63,64,65,66,67,68,69,70,72,75,79,80,84,85,86,87,89,90,92,93,94,95,96,97,98,99,100,105,106,107,108,109,123,127,128,129,130,131,132,133,134,135,136,137,142,143,149,152,153,154,155,156,157,158,159,161,163,165,167,170,171,172,174,176,177,178,179,180,181,182,183,184,189,190,195,198,200,207,209,210,211,212,217,219,228,230,],[-15,65,-87,65,-8,-9,-10,65,-93,-35,-36,-37,-38,-39,-54,-40,-109,-42,-45,-47,-50,-92,-92,-92,-92,-16,-18,65,-5,-93,-26,65,65,65,65,-109,-109,-103,-103,-105,-105,-94,-95,-96,-97,-19,-53,-26,-101,-87,65,-110,65,65,-107,65,65,65,65,-27,-28,-29,-30,65,65,-41,65,-110,-110,65,-104,-104,-106,-106,65,-87,-20,65,65,-12,65,-57,-43,-44,-108,-48,-49,-51,-52,-17,65,65,-11,-69,-112,-46,-22,65,65,-55,-58,-23,-21,-112,-56,]),'NUMBERCTE':([14,34,36,41,43,44,45,47,48,50,51,52,53,54,55,56,57,61,62,63,64,65,66,67,68,69,70,72,75,79,80,84,85,86,87,89,90,92,93,94,95,96,97,98,99,100,105,106,107,108,109,123,127,128,129,130,131,132,133,134,135,136,137,142,143,149,152,153,154,155,156,157,158,159,161,163,165,167,170,171,172,174,176,177,178,179,180,181,182,183,184,189,190,195,198,200,207,209,210,211,212,217,219,228,230,],[-15,66,-87,66,-8,-9,-10,66,-93,-35,-36,-37,-38,-39,-54,-40,-109,-42,-45,-47,-50,-92,-92,-92,-92,-16,-18,66,-5,-93,-26,66,66,66,66,-109,-109,-103,-103,-105,-105,-94,-95,-96,-97,-19,-53,-26,-101,-87,66,-110,66,66,-107,66,66,66,66,-27,-28,-29,-30,66,66,-41,66,-110,-110,66,-104,-104,-106,-106,66,-87,-20,66,66,-12,66,-57,-43,-44,-108,-48,-49,-51,-52,-17,66,66,-11,-69,-112,-46,-22,66,66,-55,-58,-23,-21,-112,-56,]),'WORDCTE':([14,34,36,41,43,44,45,47,48,50,51,52,53,54,55,56,57,61,62,63,64,65,66,67,68,69,70,72,75,79,80,84,85,86,87,89,90,92,93,94,95,96,97,98,99,100,105,106,107,108,109,123,127,128,129,130,131,132,133,134,135,136,137,142,143,149,152,153,154,155,156,157,158,159,161,163,165,167,170,171,172,174,176,177,178,179,180,181,182,183,184,189,190,195,198,200,207,209,210,211,212,217,219,228,230,],[-15,67,-87,67,-8,-9,-10,67,-93,-35,-36,-37,-38,-39,-54,-40,-109,-42,-45,-47,-50,-92,-92,-92,-92,-16,-18,67,-5,-93,-26,67,67,67,67,-109,-109,-103,-103,-105,-105,-94,-95,-96,-97,-19,-53,-26,-101,-87,67,-110,67,67,-107,67,67,67,67,-27,-28,-29,-30,67,67,-41,67,-110,-110,67,-104,-104,-106,-106,67,-87,-20,67,67,-12,67,-57,-43,-44,-108,-48,-49,-51,-52,-17,67,67,-11,-69,-112,-46,-22,67,67,-55,-58,-23,-21,-112,-56,]),'SENTENCECTE':([14,34,36,41,43,44,45,47,48,50,51,52,53,54,55,56,57,61,62,63,64,65,66,67,68,69,70,72,75,79,80,84,85,86,87,89,90,92,93,94,95,96,97,98,99,100,105,106,107,108,109,123,127,128,129,130,131,132,133,134,135,136,137,142,143,149,152,153,154,155,156,157,158,159,161,163,165,167,170,171,172,174,176,177,178,179,180,181,182,183,184,189,190,195,198,200,207,209,210,211,212,217,219,228,230,],[-15,68,-87,68,-8,-9,-10,68,-93,-35,-36,-37,-38,-39,-54,-40,-109,-42,-45,-47,-50,-92,-92,-92,-92,-16,-18,68,-5,-93,-26,68,68,68,68,-109,-109,-103,-103,-105,-105,-94,-95,-96,-97,-19,-53,-26,-101,-87,68,-110,68,68,-107,68,68,68,68,-27,-28,-29,-30,68,68,-41,68,-110,-110,68,-104,-104,-106,-106,68,-87,-20,68,68,-12,68,-57,-43,-44,-108,-48,-49,-51,-52,-17,68,68,-11,-69,-112,-46,-22,68,68,-55,-58,-23,-21,-112,-56,]),'RETURN':([14,41,42,43,44,45,48,50,51,52,53,54,55,56,61,62,63,64,65,66,67,68,69,70,75,76,79,80,96,97,98,99,100,105,106,123,134,135,136,137,149,153,154,156,157,158,159,161,165,171,174,176,177,178,179,180,181,182,183,184,185,190,195,198,200,201,207,211,212,217,219,228,230,],[-15,-85,-7,-8,-9,-10,-93,-35,-36,-37,-38,-39,-54,-40,-42,-45,-47,-50,-92,-92,-92,-92,-16,-18,-5,-6,-93,-26,-94,-95,-96,-97,-19,-53,-26,-110,-27,-28,-29,-30,-41,-110,-110,-104,-104,-106,-106,-85,-20,-12,-57,-43,-44,-108,-48,-49,-51,-52,-17,-85,203,-11,-69,-112,-46,203,-22,-55,-58,-23,-21,-112,-56,]),'OPENBRAC':([26,48,80,140,],[36,-93,108,163,]),'COMA':([26,35,55,56,61,62,63,64,65,66,67,68,79,96,97,98,99,105,106,122,123,134,135,136,137,138,140,145,148,149,153,154,156,157,158,159,160,162,176,177,178,179,180,181,182,193,200,216,223,],[-88,71,-54,-40,-42,-45,-47,-50,-92,-92,-92,-92,-93,-94,-95,-96,-97,-53,-26,-100,-110,-27,-28,-29,-30,-89,-88,170,172,-41,-110,-110,-104,-104,-106,-106,71,187,-43,-44,-108,-48,-49,-51,-52,209,-46,-89,187,]),'END':([33,38,75,],[39,74,-5,]),'CLOSECURL':([34,40,41,42,43,44,45,48,50,51,52,53,54,55,56,61,62,63,64,65,66,67,68,75,76,79,80,96,97,98,99,105,106,123,134,135,136,137,149,153,154,156,157,158,159,165,171,174,176,177,178,179,180,181,182,190,192,193,195,198,200,207,211,212,214,217,218,219,221,228,230,],[-85,75,-85,-7,-8,-9,-10,-93,-35,-36,-37,-38,-39,-54,-40,-42,-45,-47,-50,-92,-92,-92,-92,-5,-6,-93,-26,-94,-95,-96,-97,-53,-26,-110,-27,-28,-29,-30,-41,-110,-110,-104,-104,-106,-106,-20,-12,-57,-43,-44,-108,-48,-49,-51,-52,-11,208,-24,-69,-112,-46,-22,-55,-58,222,-23,-25,-21,225,-112,-56,]),'EQUAL':([48,80,194,],[-93,107,210,]),'MULT':([48,55,64,65,66,67,68,79,80,96,97,98,99,105,106,134,135,136,137,],[-93,-54,94,-92,-92,-92,-92,-93,-26,-94,-95,-96,-97,-53,-26,-27,-28,-29,-30,]),'DIV':([48,55,64,65,66,67,68,79,80,96,97,98,99,105,106,134,135,136,137,],[-93,-54,95,-92,-92,-92,-92,-93,-26,-94,-95,-96,-97,-53,-26,-27,-28,-29,-30,]),'PLUS':([48,55,63,64,65,66,67,68,79,80,96,97,98,99,105,106,134,135,136,137,158,159,181,182,],[-93,-54,92,-50,-92,-92,-92,-92,-93,-26,-94,-95,-96,-97,-53,-26,-27,-28,-29,-30,-106,-106,-51,-52,]),'MINUS':([48,55,63,64,65,66,67,68,79,80,96,97,98,99,105,106,134,135,136,137,158,159,181,182,],[-93,-54,93,-50,-92,-92,-92,-92,-93,-26,-94,-95,-96,-97,-53,-26,-27,-28,-29,-30,-106,-106,-51,-52,]),'RELOP':([48,55,62,63,64,65,66,67,68,79,80,91,96,97,98,99,105,106,134,135,136,137,156,157,158,159,179,180,181,182,],[-93,-54,-108,-47,-50,-92,-92,-92,-92,-93,-26,129,-94,-95,-96,-97,-53,-26,-27,-28,-29,-30,-104,-104,-106,-106,-48,-49,-51,-52,]),'AND':([48,55,61,62,63,64,65,66,67,68,79,80,96,97,98,99,105,106,134,135,136,137,156,157,158,159,178,179,180,181,182,200,],[-93,-54,89,-45,-47,-50,-92,-92,-92,-92,-93,-26,-94,-95,-96,-97,-53,-26,-27,-28,-29,-30,-104,-104,-106,-106,-108,-48,-49,-51,-52,-46,]),'OR':([48,55,61,62,63,64,65,66,67,68,79,80,96,97,98,99,105,106,134,135,136,137,156,157,158,159,178,179,180,181,182,200,],[-93,-54,90,-45,-47,-50,-92,-92,-92,-92,-93,-26,-94,-95,-96,-97,-53,-26,-27,-28,-29,-30,-104,-104,-106,-106,-108,-48,-49,-51,-52,-46,]),'DOT':([48,],[82,]),'CLOSEPAREN':([55,56,61,62,63,64,65,66,67,68,78,79,96,97,98,99,102,104,105,106,109,121,122,123,124,125,134,135,136,137,140,141,144,145,146,148,149,153,154,156,157,158,159,162,170,175,176,177,178,179,180,181,182,186,188,196,197,200,205,216,223,227,],[-54,-40,-42,-45,-47,-50,-92,-92,-92,-92,105,-93,-94,-95,-96,-97,139,-99,-53,-26,-85,147,-100,-110,150,151,-27,-28,-29,-30,-88,164,169,-72,-74,-13,-41,-110,-110,-104,-104,-106,-106,-85,-85,199,-43,-44,-108,-48,-49,-51,-52,-63,-66,-73,-14,-46,-65,-89,-85,-64,]),'CLOSEBRAC':([65,66,67,68,79,96,97,98,99,101,106,134,135,136,137,168,206,],[-92,-92,-92,-92,-93,-94,-95,-96,-97,138,-26,-27,-28,-29,-30,194,216,]),'ELSE':([75,198,211,],[-5,-112,220,]),'LENGTH':([82,],[111,]),'FREQUENCY':([82,],[112,]),'SEARCH':([82,],[113,]),'EXISTS':([82,],[114,]),'MEAN':([82,],[115,]),'MEDIAN':([82,],[116,]),'MODE':([82,],[117,]),'WORDCOUNT':([82,],[118,]),'TOKENIZE':([82,],[119,]),'REMOVE':([82,],[120,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'func_start':([3,],[4,]),'declare':([5,161,],[6,184,]),'startaux':([5,6,9,],[7,12,20,]),'function':([5,6,9,],[9,9,9,]),'empty':([5,6,9,34,41,48,109,161,162,170,184,185,201,223,],[10,10,10,42,42,83,146,42,188,146,42,204,204,188,]),'decaux':([8,71,],[14,100,]),'type':([8,11,71,73,187,],[15,22,15,103,103,]),'funcaux':([11,],[21,]),'func_begin_main':([13,24,],[25,32,]),'func_type':([16,17,18,19,],[27,28,29,30,]),'block':([25,32,60,151,173,224,],[33,38,88,174,198,228,]),'func_declare_var':([26,140,],[35,162,]),'func_declare_function':([31,],[37,]),'blockaux':([34,41,161,184,],[40,76,185,201,]),'action':([34,41,161,184,],[41,41,41,41,]),'input':([34,41,161,184,],[43,43,43,43,]),'output':([34,41,161,184,],[44,44,44,44,]),'statement':([34,41,161,184,],[45,45,45,45,]),'assign':([34,41,161,184,],[50,50,50,50,]),'expression':([34,41,47,84,86,87,152,161,172,184,],[51,51,78,122,124,125,175,51,122,51,]),'condition':([34,41,161,184,],[52,52,52,52,]),'cycle':([34,41,161,184,],[53,53,53,53,]),'callfunction':([34,41,161,184,],[54,54,54,54,]),'cte':([34,41,47,72,84,85,86,87,109,127,128,130,131,132,133,142,143,152,155,161,167,170,172,184,189,209,210,],[55,55,55,101,55,55,55,55,145,55,55,55,55,55,55,55,168,55,55,55,55,145,55,55,206,55,55,]),'logexpression':([34,41,47,84,85,86,87,127,128,152,161,172,184,],[56,56,56,56,123,56,56,153,154,56,56,56,56,]),'relopexpression':([34,41,47,84,85,86,87,127,128,152,161,172,184,],[61,61,61,61,61,61,61,61,61,61,61,61,61,]),'exp':([34,41,47,84,85,86,87,127,128,130,131,142,152,155,161,167,172,184,209,210,],[62,62,62,62,62,62,62,62,62,156,157,166,62,178,62,193,62,62,193,166,]),'term':([34,41,47,84,85,86,87,127,128,130,131,132,133,142,152,155,161,167,172,184,209,210,],[63,63,63,63,63,63,63,63,63,63,63,158,159,63,63,63,63,63,63,63,63,63,]),'factor':([34,41,47,84,85,86,87,127,128,130,131,132,133,142,152,155,161,167,172,184,209,210,],[64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,]),'declareaux':([35,160,],[69,183,]),'func_isSize':([36,108,163,],[72,143,189,]),'func_constantID':([48,79,],[80,106,]),'callaux':([48,],[81,]),'func_logicOp_operation':([57,89,90,],[85,127,128,]),'func_relop':([62,178,],[91,200,]),'func_constant':([65,66,67,68,],[96,97,98,99,]),'parameter':([73,187,],[102,205,]),'special':([82,],[110,]),'outputaux':([84,172,],[121,197,]),'func_term_operation':([92,93,],[130,131,]),'func_factor_operation':([94,95,],[132,133,]),'func_boolCte':([96,],[134,]),'func_numberCte':([97,],[135,]),'func_wordCte':([98,],[136,]),'func_sentenceCte':([99,],[137,]),'func_read':([104,],[141,]),'func_assign':([107,],[142,]),'spaux':([109,170,],[144,196,]),'func_print':([122,],[148,]),'func_logicOP':([123,153,154,],[149,176,177,]),'func_relop_operation':([129,],[155,]),'func_declare_array':([138,216,],[160,223,]),'assignaux':([142,210,],[165,219,]),'func_if':([150,],[173,]),'func_term':([156,157,],[179,180,]),'func_factor':([158,159,],[181,182,]),'parameteraux':([162,223,],[186,227,]),'func_assign_value':([166,],[191,]),'assiaux':([167,209,],[192,218,]),'returnaux':([185,201,],[202,213,]),'func_endIf':([198,228,],[211,230,]),'func_else':([220,],[224,]),'func_clear':([222,225,],[226,229,]),}

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
  ('startaux -> function startaux','startaux',2,'p_startaux','YaccKotoba.py',21),
  ('startaux -> empty','startaux',1,'p_startaux','YaccKotoba.py',22),
  ('block -> OPENCURL blockaux CLOSECURL','block',3,'p_block','YaccKotoba.py',25),
  ('blockaux -> action blockaux','blockaux',2,'p_blockaux','YaccKotoba.py',28),
  ('blockaux -> empty','blockaux',1,'p_blockaux','YaccKotoba.py',29),
  ('action -> input','action',1,'p_action','YaccKotoba.py',32),
  ('action -> output','action',1,'p_action','YaccKotoba.py',33),
  ('action -> statement','action',1,'p_action','YaccKotoba.py',34),
  ('input -> READ OPENPAREN ID func_read CLOSEPAREN ENDSTMT','input',6,'p_input','YaccKotoba.py',37),
  ('output -> WRITE OPENPAREN outputaux CLOSEPAREN ENDSTMT','output',5,'p_output','YaccKotoba.py',41),
  ('outputaux -> expression func_print','outputaux',2,'p_outputaux','YaccKotoba.py',44),
  ('outputaux -> expression func_print COMA outputaux','outputaux',4,'p_outputaux','YaccKotoba.py',45),
  ('declare -> DEC decaux','declare',2,'p_declare','YaccKotoba.py',48),
  ('decaux -> type ID func_declare_var declareaux','decaux',4,'p_decaux','YaccKotoba.py',51),
  ('decaux -> type ID OPENBRAC func_isSize cte CLOSEBRAC func_declare_array declareaux','decaux',8,'p_decaux','YaccKotoba.py',52),
  ('declareaux -> ENDSTMT','declareaux',1,'p_declareaux','YaccKotoba.py',55),
  ('declareaux -> COMA decaux','declareaux',2,'p_declareaux','YaccKotoba.py',56),
  ('assign -> ID func_constantID EQUAL func_assign assignaux','assign',5,'p_assign','YaccKotoba.py',59),
  ('assign -> ID func_constantID OPENBRAC func_isSize cte CLOSEBRAC EQUAL assignaux','assign',8,'p_assign','YaccKotoba.py',60),
  ('assignaux -> exp func_assign_value ENDSTMT','assignaux',3,'p_assignaux','YaccKotoba.py',63),
  ('assignaux -> OPENCURL assiaux CLOSECURL ENDSTMT','assignaux',4,'p_assignaux','YaccKotoba.py',64),
  ('assiaux -> exp','assiaux',1,'p_assiaux','YaccKotoba.py',67),
  ('assiaux -> exp COMA assiaux','assiaux',3,'p_assiaux','YaccKotoba.py',68),
  ('cte -> ID func_constantID','cte',2,'p_cte','YaccKotoba.py',71),
  ('cte -> BOOLCTE func_constant func_boolCte','cte',3,'p_cte','YaccKotoba.py',72),
  ('cte -> NUMBERCTE func_constant func_numberCte','cte',3,'p_cte','YaccKotoba.py',73),
  ('cte -> WORDCTE func_constant func_wordCte','cte',3,'p_cte','YaccKotoba.py',74),
  ('cte -> SENTENCECTE func_constant func_sentenceCte','cte',3,'p_cte','YaccKotoba.py',75),
  ('type -> BOOL func_type','type',2,'p_type','YaccKotoba.py',78),
  ('type -> NUMBER func_type','type',2,'p_type','YaccKotoba.py',79),
  ('type -> WORD func_type','type',2,'p_type','YaccKotoba.py',80),
  ('type -> SENTENCE func_type','type',2,'p_type','YaccKotoba.py',81),
  ('statement -> assign','statement',1,'p_statement','YaccKotoba.py',84),
  ('statement -> expression','statement',1,'p_statement','YaccKotoba.py',85),
  ('statement -> condition','statement',1,'p_statement','YaccKotoba.py',86),
  ('statement -> cycle','statement',1,'p_statement','YaccKotoba.py',87),
  ('statement -> callfunction','statement',1,'p_statement','YaccKotoba.py',88),
  ('expression -> logexpression','expression',1,'p_expression','YaccKotoba.py',91),
  ('expression -> NOT func_logicOp_operation logexpression func_logicOP','expression',4,'p_expression','YaccKotoba.py',92),
  ('logexpression -> relopexpression','logexpression',1,'p_logexpression','YaccKotoba.py',95),
  ('logexpression -> relopexpression AND func_logicOp_operation logexpression func_logicOP','logexpression',5,'p_logexpression','YaccKotoba.py',96),
  ('logexpression -> relopexpression OR func_logicOp_operation logexpression func_logicOP','logexpression',5,'p_logexpression','YaccKotoba.py',97),
  ('relopexpression -> exp','relopexpression',1,'p_relopexression','YaccKotoba.py',100),
  ('relopexpression -> exp func_relop RELOP func_relop_operation exp func_relop','relopexpression',6,'p_relopexression','YaccKotoba.py',101),
  ('exp -> term','exp',1,'p_exp','YaccKotoba.py',104),
  ('exp -> term PLUS func_term_operation exp func_term','exp',5,'p_exp','YaccKotoba.py',105),
  ('exp -> term MINUS func_term_operation exp func_term','exp',5,'p_exp','YaccKotoba.py',106),
  ('term -> factor','term',1,'p_term','YaccKotoba.py',109),
  ('term -> factor MULT func_factor_operation term func_factor','term',5,'p_term','YaccKotoba.py',110),
  ('term -> factor DIV func_factor_operation term func_factor','term',5,'p_term','YaccKotoba.py',111),
  ('factor -> OPENPAREN expression CLOSEPAREN','factor',3,'p_factor','YaccKotoba.py',114),
  ('factor -> cte','factor',1,'p_factor','YaccKotoba.py',115),
  ('condition -> IF OPENPAREN expression CLOSEPAREN func_if block func_endIf','condition',7,'p_condition','YaccKotoba.py',118),
  ('condition -> IF OPENPAREN expression CLOSEPAREN func_if block func_endIf ELSE func_else block func_endIf','condition',11,'p_condition','YaccKotoba.py',119),
  ('cycle -> WHILE OPENPAREN expression CLOSEPAREN block','cycle',5,'p_cycle','YaccKotoba.py',122),
  ('cycle -> DO block WHILE OPENPAREN expression CLOSEPAREN ENDSTMT','cycle',7,'p_cycle','YaccKotoba.py',123),
  ('function -> FUNC funcaux ID func_declare_function OPENPAREN parameter CLOSEPAREN OPENCURL declare blockaux returnaux ENDSTMT CLOSECURL func_clear','function',14,'p_function','YaccKotoba.py',126),
  ('function -> FUNC funcaux ID func_declare_function OPENPAREN parameter CLOSEPAREN OPENCURL blockaux returnaux ENDSTMT CLOSECURL func_clear','function',13,'p_function','YaccKotoba.py',127),
  ('funcaux -> type','funcaux',1,'p_funcaux','YaccKotoba.py',130),
  ('funcaux -> VOID','funcaux',1,'p_funcaux','YaccKotoba.py',131),
  ('parameter -> type ID func_declare_var parameteraux','parameter',4,'p_parameter','YaccKotoba.py',134),
  ('parameter -> type ID OPENBRAC func_isSize cte CLOSEBRAC func_declare_array parameteraux','parameter',8,'p_parameter','YaccKotoba.py',135),
  ('parameteraux -> COMA parameter','parameteraux',2,'p_parameteraux','YaccKotoba.py',138),
  ('parameteraux -> empty','parameteraux',1,'p_parameteraux','YaccKotoba.py',139),
  ('returnaux -> RETURN ID','returnaux',2,'p_returnaux','YaccKotoba.py',142),
  ('returnaux -> empty','returnaux',1,'p_returnaux','YaccKotoba.py',143),
  ('callfunction -> ID callaux OPENPAREN spaux CLOSEPAREN ENDSTMT','callfunction',6,'p_callfunction','YaccKotoba.py',146),
  ('callaux -> DOT special','callaux',2,'p_callaux','YaccKotoba.py',149),
  ('callaux -> empty','callaux',1,'p_callaux','YaccKotoba.py',150),
  ('spaux -> cte','spaux',1,'p_spaux','YaccKotoba.py',153),
  ('spaux -> cte COMA spaux','spaux',3,'p_spaux','YaccKotoba.py',154),
  ('spaux -> empty','spaux',1,'p_spaux','YaccKotoba.py',155),
  ('special -> LENGTH','special',1,'p_special','YaccKotoba.py',158),
  ('special -> FREQUENCY','special',1,'p_special','YaccKotoba.py',159),
  ('special -> SEARCH','special',1,'p_special','YaccKotoba.py',160),
  ('special -> EXISTS','special',1,'p_special','YaccKotoba.py',161),
  ('special -> MEAN','special',1,'p_special','YaccKotoba.py',162),
  ('special -> MEDIAN','special',1,'p_special','YaccKotoba.py',163),
  ('special -> MODE','special',1,'p_special','YaccKotoba.py',164),
  ('special -> WORDCOUNT','special',1,'p_special','YaccKotoba.py',165),
  ('special -> TOKENIZE','special',1,'p_special','YaccKotoba.py',166),
  ('special -> REMOVE','special',1,'p_special','YaccKotoba.py',167),
  ('empty -> <empty>','empty',0,'p_empty','YaccKotoba.py',170),
  ('func_start -> <empty>','func_start',0,'p_func_start','YaccKotoba.py',177),
  ('func_isSize -> <empty>','func_isSize',0,'p_func_isSize','YaccKotoba.py',186),
  ('func_declare_var -> <empty>','func_declare_var',0,'p_func_declare_var','YaccKotoba.py',191),
  ('func_declare_array -> <empty>','func_declare_array',0,'p_func_declare_array','YaccKotoba.py',198),
  ('func_declare_function -> <empty>','func_declare_function',0,'p_func_declare_function','YaccKotoba.py',207),
  ('func_type -> <empty>','func_type',0,'p_func_type','YaccKotoba.py',215),
  ('func_constant -> <empty>','func_constant',0,'p_func_constant','YaccKotoba.py',220),
  ('func_constantID -> <empty>','func_constantID',0,'p_func_constantID','YaccKotoba.py',227),
  ('func_boolCte -> <empty>','func_boolCte',0,'p_func_boolCte','YaccKotoba.py',238),
  ('func_numberCte -> <empty>','func_numberCte',0,'p_func_numberCte','YaccKotoba.py',243),
  ('func_wordCte -> <empty>','func_wordCte',0,'p_func_wordCte','YaccKotoba.py',248),
  ('func_sentenceCte -> <empty>','func_sentenceCte',0,'p_func_sentenceCte','YaccKotoba.py',253),
  ('func_begin_main -> <empty>','func_begin_main',0,'p_func_begin_main','YaccKotoba.py',260),
  ('func_read -> <empty>','func_read',0,'p_func_read','YaccKotoba.py',265),
  ('func_print -> <empty>','func_print',0,'p_func_print','YaccKotoba.py',277),
  ('func_assign -> <empty>','func_assign',0,'p_func_assign','YaccKotoba.py',286),
  ('func_assign_value -> <empty>','func_assign_value',0,'p_func_assign_value','YaccKotoba.py',290),
  ('func_term_operation -> <empty>','func_term_operation',0,'p_func_term_operation','YaccKotoba.py',311),
  ('func_term -> <empty>','func_term',0,'p_func_term','YaccKotoba.py',318),
  ('func_factor_operation -> <empty>','func_factor_operation',0,'p_func_factor_operation','YaccKotoba.py',339),
  ('func_factor -> <empty>','func_factor',0,'p_func_factor','YaccKotoba.py',346),
  ('func_relop_operation -> <empty>','func_relop_operation',0,'p_func_relop_operation','YaccKotoba.py',368),
  ('func_relop -> <empty>','func_relop',0,'p_func_relop','YaccKotoba.py',379),
  ('func_logicOp_operation -> <empty>','func_logicOp_operation',0,'p_func_logicOp_operation','YaccKotoba.py',402),
  ('func_logicOP -> <empty>','func_logicOP',0,'p_func_logicOP','YaccKotoba.py',411),
  ('func_if -> <empty>','func_if',0,'p_func_if','YaccKotoba.py',449),
  ('func_endIf -> <empty>','func_endIf',0,'p_func_endIf','YaccKotoba.py',463),
  ('func_else -> <empty>','func_else',0,'p_func_else','YaccKotoba.py',469),
  ('func_clear -> <empty>','func_clear',0,'p_func_clear','YaccKotoba.py',480),
]
