
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND BEGIN BOOL BOOLCTE CLOSEBRAC CLOSECURL CLOSEPAREN COMA DEC DIV DO DOT ELSE END ENDSTMT EQUAL EXISTS FREQUENCY FUNC ID IF KOTOBA LENGTH MEAN MEDIAN MINUS MODE MULT NOT NUMBER NUMBERCTE OPENBRAC OPENCURL OPENPAREN OR PLUS READ RELOP REMOVE RETURN SEARCH SENTENCE SENTENCECTE TOKENIZE VOID WHILE WORD WORDCOUNT WORDCTE WRITEstart : KOTOBA ID ENDSTMT declare startaux BEGIN block END\n\t| KOTOBA ID ENDSTMT startaux BEGIN block ENDstartaux : function startaux\n\t| emptyblock : OPENCURL blockaux CLOSECURLblockaux : action blockaux\n\t| emptyaction : input\n\t| output\n\t| statementinput : READ OPENPAREN ID CLOSEPAREN ENDSTMToutput : WRITE OPENPAREN outputaux CLOSEPAREN ENDSTMToutputaux : expression\n\t| expression COMA outputauxdeclare : DEC decauxdecaux : type ID declareaux\n\t| type ID OPENBRAC cte CLOSEBRAC declareauxdeclareaux : ENDSTMT\n\t| COMA decauxassign : ID EQUAL assignaux\n\t| ID OPENBRAC cte CLOSEBRAC EQUAL assignauxassignaux : exp ENDSTMT\n\t| OPENCURL assiaux CLOSECURL ENDSTMTassiaux : exp\n\t| exp COMA assiauxcte : ID\n\t| BOOLCTE\n\t| NUMBERCTE\n\t| WORDCTE\n\t| SENTENCECTEtype : BOOL\n\t| NUMBER\n\t| WORD\n\t| SENTENCEstatement : assign\n\t| expression\n\t| condition\n\t| cycle\n\t| specialfunctionexpression : relopexpression\n\t| relopexpression AND expression\n\t| relopexpression OR expressionrelopexpression : exp\n\t| exp RELOP exp\n\t| NOT expexp : term\n\t| term PLUS exp\n\t| term MINUS expterm : factor\n\t| factor MULT term\n\t| factor DIV termfactor : OPENPAREN expression CLOSEPAREN\n\t| ctecondition : IF OPENPAREN expression CLOSEPAREN block\n\t|  IF OPENPAREN expression CLOSEPAREN block ELSE blockcycle : WHILE OPENPAREN expression CLOSEPAREN block\n\t| DO block WHILE OPENPAREN expression CLOSEPAREN ENDSTMTfunction : FUNC funcaux ID OPENPAREN parameteraux CLOSEPAREN OPENCURL declare blockaux returnaux ENDSTMT CLOSECURL\n\t| FUNC funcaux ID OPENPAREN parameteraux CLOSEPAREN OPENCURL blockaux returnaux ENDSTMT CLOSECURLfuncaux : type\n\t| VOIDparameteraux : type ID\n\t| type ID COMA parameteraux\n\t| emptyreturnaux : RETURN ID\n\t| emptyspecialfunction : ID DOT special OPENPAREN spaux CLOSEPAREN ENDSTMTspaux : cte\n\t| emptyspecial : LENGTH\n\t| FREQUENCY\n    | SEARCH\n    | EXISTS\n    | MEAN\n\t| MEDIAN\n\t| MODE\n\t| WORDCOUNT\n\t| TOKENIZE\n\t| REMOVEempty : '
    
_lr_action_items = {'KOTOBA':([0,],[2,]),'$end':([1,29,63,],[0,-2,-1,]),'ID':([2,13,14,15,16,17,18,20,21,22,25,31,33,34,35,37,38,40,41,42,43,44,45,46,50,51,52,53,54,55,56,57,58,59,60,64,66,68,69,70,72,73,74,75,76,78,79,80,81,82,83,85,87,90,91,93,108,109,113,114,115,116,117,122,126,128,131,132,133,135,137,138,142,144,145,147,150,152,158,160,161,162,],[3,-15,26,-31,-32,-33,-34,27,-60,-61,38,38,-8,-9,-10,68,-26,-35,-36,-37,-38,-39,-53,-40,-43,68,-46,-49,-27,-28,-29,-30,-16,68,-18,-5,89,-26,68,68,68,68,68,68,68,68,-45,68,68,68,68,-19,120,-52,-20,68,-41,-42,-44,-47,-48,-50,-51,-22,68,68,68,-17,38,-11,68,68,-12,-54,-56,38,-23,-21,165,-67,-55,-57,]),'ENDSTMT':([3,13,26,31,32,33,34,35,38,40,41,42,43,44,45,46,50,52,53,54,55,56,57,58,60,64,65,68,79,85,90,91,92,108,109,113,114,115,116,117,118,121,122,127,132,133,135,136,142,144,145,147,148,150,152,153,155,156,157,159,160,161,162,163,165,],[4,-15,60,-80,-7,-8,-9,-10,-26,-35,-36,-37,-38,-39,-53,-40,-43,-46,-49,-27,-28,-29,-30,-16,-18,-5,-6,-26,-45,-19,-52,-20,122,-41,-42,-44,-47,-48,-50,-51,60,135,-22,142,-17,-80,-11,150,-12,-54,-56,-80,-80,-23,-21,160,162,-80,164,-66,-67,-55,-57,166,-65,]),'DEC':([4,133,],[7,7,]),'FUNC':([4,5,8,13,58,60,85,132,167,168,],[10,10,10,-15,-16,-18,-19,-17,-59,-58,]),'BEGIN':([4,5,6,8,9,11,13,19,58,60,85,132,167,168,],[-80,-80,12,-80,-4,23,-15,-3,-16,-18,-19,-17,-59,-58,]),'BOOL':([7,10,61,62,134,],[15,15,15,15,15,]),'NUMBER':([7,10,61,62,134,],[16,16,16,16,16,]),'WORD':([7,10,61,62,134,],[17,17,17,17,17,]),'SENTENCE':([7,10,61,62,134,],[18,18,18,18,18,]),'VOID':([10,],[22,]),'OPENCURL':([12,23,49,69,119,129,130,138,154,],[25,25,25,93,133,25,25,93,25,]),'READ':([13,25,31,33,34,35,38,40,41,42,43,44,45,46,50,52,53,54,55,56,57,58,60,64,68,79,85,90,91,108,109,113,114,115,116,117,122,132,133,135,142,144,145,147,150,152,160,161,162,],[-15,36,36,-8,-9,-10,-26,-35,-36,-37,-38,-39,-53,-40,-43,-46,-49,-27,-28,-29,-30,-16,-18,-5,-26,-45,-19,-52,-20,-41,-42,-44,-47,-48,-50,-51,-22,-17,36,-11,-12,-54,-56,36,-23,-21,-67,-55,-57,]),'WRITE':([13,25,31,33,34,35,38,40,41,42,43,44,45,46,50,52,53,54,55,56,57,58,60,64,68,79,85,90,91,108,109,113,114,115,116,117,122,132,133,135,142,144,145,147,150,152,160,161,162,],[-15,39,39,-8,-9,-10,-26,-35,-36,-37,-38,-39,-53,-40,-43,-46,-49,-27,-28,-29,-30,-16,-18,-5,-26,-45,-19,-52,-20,-41,-42,-44,-47,-48,-50,-51,-22,-17,39,-11,-12,-54,-56,39,-23,-21,-67,-55,-57,]),'IF':([13,25,31,33,34,35,38,40,41,42,43,44,45,46,50,52,53,54,55,56,57,58,60,64,68,79,85,90,91,108,109,113,114,115,116,117,122,132,133,135,142,144,145,147,150,152,160,161,162,],[-15,47,47,-8,-9,-10,-26,-35,-36,-37,-38,-39,-53,-40,-43,-46,-49,-27,-28,-29,-30,-16,-18,-5,-26,-45,-19,-52,-20,-41,-42,-44,-47,-48,-50,-51,-22,-17,47,-11,-12,-54,-56,47,-23,-21,-67,-55,-57,]),'WHILE':([13,25,31,33,34,35,38,40,41,42,43,44,45,46,50,52,53,54,55,56,57,58,60,64,68,77,79,85,90,91,108,109,113,114,115,116,117,122,132,133,135,142,144,145,147,150,152,160,161,162,],[-15,48,48,-8,-9,-10,-26,-35,-36,-37,-38,-39,-53,-40,-43,-46,-49,-27,-28,-29,-30,-16,-18,-5,-26,112,-45,-19,-52,-20,-41,-42,-44,-47,-48,-50,-51,-22,-17,48,-11,-12,-54,-56,48,-23,-21,-67,-55,-57,]),'DO':([13,25,31,33,34,35,38,40,41,42,43,44,45,46,50,52,53,54,55,56,57,58,60,64,68,79,85,90,91,108,109,113,114,115,116,117,122,132,133,135,142,144,145,147,150,152,160,161,162,],[-15,49,49,-8,-9,-10,-26,-35,-36,-37,-38,-39,-53,-40,-43,-46,-49,-27,-28,-29,-30,-16,-18,-5,-26,-45,-19,-52,-20,-41,-42,-44,-47,-48,-50,-51,-22,-17,49,-11,-12,-54,-56,49,-23,-21,-67,-55,-57,]),'NOT':([13,25,31,33,34,35,37,38,40,41,42,43,44,45,46,50,52,53,54,55,56,57,58,60,64,68,72,73,74,75,76,79,85,90,91,108,109,113,114,115,116,117,122,128,131,132,133,135,142,144,145,147,150,152,160,161,162,],[-15,51,51,-8,-9,-10,51,-26,-35,-36,-37,-38,-39,-53,-40,-43,-46,-49,-27,-28,-29,-30,-16,-18,-5,-26,51,51,51,51,51,-45,-19,-52,-20,-41,-42,-44,-47,-48,-50,-51,-22,51,51,-17,51,-11,-12,-54,-56,51,-23,-21,-67,-55,-57,]),'OPENPAREN':([13,25,27,31,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,50,51,52,53,54,55,56,57,58,60,64,68,69,72,73,74,75,76,78,79,80,81,82,83,85,90,91,93,95,96,97,98,99,100,101,102,103,104,105,108,109,112,113,114,115,116,117,122,128,131,132,133,135,137,138,142,144,145,147,150,152,160,161,162,],[-15,37,62,37,-8,-9,-10,66,37,-26,72,-35,-36,-37,-38,-39,-53,-40,75,76,-43,37,-46,-49,-27,-28,-29,-30,-16,-18,-5,-26,37,37,37,37,37,37,37,-45,37,37,37,37,-19,-52,-20,37,126,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-41,-42,131,-44,-47,-48,-50,-51,-22,37,37,-17,37,-11,37,37,-12,-54,-56,37,-23,-21,-67,-55,-57,]),'BOOLCTE':([13,25,31,33,34,35,37,38,40,41,42,43,44,45,46,50,51,52,53,54,55,56,57,58,59,60,64,68,69,70,72,73,74,75,76,78,79,80,81,82,83,85,90,91,93,108,109,113,114,115,116,117,122,126,128,131,132,133,135,137,138,142,144,145,147,150,152,160,161,162,],[-15,54,54,-8,-9,-10,54,-26,-35,-36,-37,-38,-39,-53,-40,-43,54,-46,-49,-27,-28,-29,-30,-16,54,-18,-5,-26,54,54,54,54,54,54,54,54,-45,54,54,54,54,-19,-52,-20,54,-41,-42,-44,-47,-48,-50,-51,-22,54,54,54,-17,54,-11,54,54,-12,-54,-56,54,-23,-21,-67,-55,-57,]),'NUMBERCTE':([13,25,31,33,34,35,37,38,40,41,42,43,44,45,46,50,51,52,53,54,55,56,57,58,59,60,64,68,69,70,72,73,74,75,76,78,79,80,81,82,83,85,90,91,93,108,109,113,114,115,116,117,122,126,128,131,132,133,135,137,138,142,144,145,147,150,152,160,161,162,],[-15,55,55,-8,-9,-10,55,-26,-35,-36,-37,-38,-39,-53,-40,-43,55,-46,-49,-27,-28,-29,-30,-16,55,-18,-5,-26,55,55,55,55,55,55,55,55,-45,55,55,55,55,-19,-52,-20,55,-41,-42,-44,-47,-48,-50,-51,-22,55,55,55,-17,55,-11,55,55,-12,-54,-56,55,-23,-21,-67,-55,-57,]),'WORDCTE':([13,25,31,33,34,35,37,38,40,41,42,43,44,45,46,50,51,52,53,54,55,56,57,58,59,60,64,68,69,70,72,73,74,75,76,78,79,80,81,82,83,85,90,91,93,108,109,113,114,115,116,117,122,126,128,131,132,133,135,137,138,142,144,145,147,150,152,160,161,162,],[-15,56,56,-8,-9,-10,56,-26,-35,-36,-37,-38,-39,-53,-40,-43,56,-46,-49,-27,-28,-29,-30,-16,56,-18,-5,-26,56,56,56,56,56,56,56,56,-45,56,56,56,56,-19,-52,-20,56,-41,-42,-44,-47,-48,-50,-51,-22,56,56,56,-17,56,-11,56,56,-12,-54,-56,56,-23,-21,-67,-55,-57,]),'SENTENCECTE':([13,25,31,33,34,35,37,38,40,41,42,43,44,45,46,50,51,52,53,54,55,56,57,58,59,60,64,68,69,70,72,73,74,75,76,78,79,80,81,82,83,85,90,91,93,108,109,113,114,115,116,117,122,126,128,131,132,133,135,137,138,142,144,145,147,150,152,160,161,162,],[-15,57,57,-8,-9,-10,57,-26,-35,-36,-37,-38,-39,-53,-40,-43,57,-46,-49,-27,-28,-29,-30,-16,57,-18,-5,-26,57,57,57,57,57,57,57,57,-45,57,57,57,57,-19,-52,-20,57,-41,-42,-44,-47,-48,-50,-51,-22,57,57,57,-17,57,-11,57,57,-12,-54,-56,57,-23,-21,-67,-55,-57,]),'RETURN':([13,31,32,33,34,35,38,40,41,42,43,44,45,46,50,52,53,54,55,56,57,58,60,64,65,68,79,85,90,91,108,109,113,114,115,116,117,122,132,133,135,142,144,145,147,148,150,152,156,160,161,162,],[-15,-80,-7,-8,-9,-10,-26,-35,-36,-37,-38,-39,-53,-40,-43,-46,-49,-27,-28,-29,-30,-16,-18,-5,-6,-26,-45,-19,-52,-20,-41,-42,-44,-47,-48,-50,-51,-22,-17,-80,-11,-12,-54,-56,-80,158,-23,-21,158,-67,-55,-57,]),'END':([24,28,64,],[29,63,-5,]),'CLOSECURL':([25,30,31,32,33,34,35,38,40,41,42,43,44,45,46,50,52,53,54,55,56,57,64,65,68,79,90,91,108,109,113,114,115,116,117,122,123,124,135,142,144,145,150,151,152,160,161,162,164,166,],[-80,64,-80,-7,-8,-9,-10,-26,-35,-36,-37,-38,-39,-53,-40,-43,-46,-49,-27,-28,-29,-30,-5,-6,-26,-45,-52,-20,-41,-42,-44,-47,-48,-50,-51,-22,136,-24,-11,-12,-54,-56,-23,-25,-21,-67,-55,-57,167,168,]),'OPENBRAC':([26,38,],[59,70,]),'COMA':([26,45,46,50,52,53,54,55,56,57,68,79,90,107,108,109,113,114,115,116,117,118,120,124,],[61,-53,-40,-43,-46,-49,-27,-28,-29,-30,-26,-45,-52,128,-41,-42,-44,-47,-48,-50,-51,61,134,137,]),'EQUAL':([38,125,],[69,138,]),'DOT':([38,],[71,]),'MULT':([38,45,53,54,55,56,57,68,90,],[-26,-53,82,-27,-28,-29,-30,-26,-52,]),'DIV':([38,45,53,54,55,56,57,68,90,],[-26,-53,83,-27,-28,-29,-30,-26,-52,]),'PLUS':([38,45,52,53,54,55,56,57,68,90,116,117,],[-26,-53,80,-49,-27,-28,-29,-30,-26,-52,-50,-51,]),'MINUS':([38,45,52,53,54,55,56,57,68,90,116,117,],[-26,-53,81,-49,-27,-28,-29,-30,-26,-52,-50,-51,]),'RELOP':([38,45,50,52,53,54,55,56,57,68,90,114,115,116,117,],[-26,-53,78,-46,-49,-27,-28,-29,-30,-26,-52,-47,-48,-50,-51,]),'AND':([38,45,46,50,52,53,54,55,56,57,68,79,90,113,114,115,116,117,],[-26,-53,73,-43,-46,-49,-27,-28,-29,-30,-26,-45,-52,-44,-47,-48,-50,-51,]),'OR':([38,45,46,50,52,53,54,55,56,57,68,79,90,113,114,115,116,117,],[-26,-53,74,-43,-46,-49,-27,-28,-29,-30,-26,-45,-52,-44,-47,-48,-50,-51,]),'CLOSEPAREN':([45,46,50,52,53,54,55,56,57,62,67,68,79,86,88,89,90,106,107,108,109,110,111,113,114,115,116,117,120,126,134,139,140,141,143,146,149,],[-53,-40,-43,-46,-49,-27,-28,-29,-30,-80,90,-26,-45,119,-64,121,-52,127,-13,-41,-42,129,130,-44,-47,-48,-50,-51,-62,-80,-80,153,-68,-69,-14,155,-63,]),'CLOSEBRAC':([54,55,56,57,68,84,94,],[-27,-28,-29,-30,-26,118,125,]),'ELSE':([64,144,],[-5,154,]),'LENGTH':([71,],[96,]),'FREQUENCY':([71,],[97,]),'SEARCH':([71,],[98,]),'EXISTS':([71,],[99,]),'MEAN':([71,],[100,]),'MEDIAN':([71,],[101,]),'MODE':([71,],[102,]),'WORDCOUNT':([71,],[103,]),'TOKENIZE':([71,],[104,]),'REMOVE':([71,],[105,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'declare':([4,133,],[5,147,]),'startaux':([4,5,8,],[6,11,19,]),'function':([4,5,8,],[8,8,8,]),'empty':([4,5,8,25,31,62,126,133,134,147,148,156,],[9,9,9,32,32,88,141,32,88,32,159,159,]),'decaux':([7,61,],[13,85,]),'type':([7,10,61,62,134,],[14,21,14,87,87,]),'funcaux':([10,],[20,]),'block':([12,23,49,129,130,154,],[24,28,77,144,145,161,]),'blockaux':([25,31,133,147,],[30,65,148,156,]),'action':([25,31,133,147,],[31,31,31,31,]),'input':([25,31,133,147,],[33,33,33,33,]),'output':([25,31,133,147,],[34,34,34,34,]),'statement':([25,31,133,147,],[35,35,35,35,]),'assign':([25,31,133,147,],[40,40,40,40,]),'expression':([25,31,37,72,73,74,75,76,128,131,133,147,],[41,41,67,107,108,109,110,111,107,146,41,41,]),'condition':([25,31,133,147,],[42,42,42,42,]),'cycle':([25,31,133,147,],[43,43,43,43,]),'specialfunction':([25,31,133,147,],[44,44,44,44,]),'cte':([25,31,37,51,59,69,70,72,73,74,75,76,78,80,81,82,83,93,126,128,131,133,137,138,147,],[45,45,45,45,84,45,94,45,45,45,45,45,45,45,45,45,45,45,140,45,45,45,45,45,45,]),'relopexpression':([25,31,37,72,73,74,75,76,128,131,133,147,],[46,46,46,46,46,46,46,46,46,46,46,46,]),'exp':([25,31,37,51,69,72,73,74,75,76,78,80,81,93,128,131,133,137,138,147,],[50,50,50,79,92,50,50,50,50,50,113,114,115,124,50,50,50,124,92,50,]),'term':([25,31,37,51,69,72,73,74,75,76,78,80,81,82,83,93,128,131,133,137,138,147,],[52,52,52,52,52,52,52,52,52,52,52,52,52,116,117,52,52,52,52,52,52,52,]),'factor':([25,31,37,51,69,72,73,74,75,76,78,80,81,82,83,93,128,131,133,137,138,147,],[53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),'declareaux':([26,118,],[58,132,]),'parameteraux':([62,134,],[86,149,]),'assignaux':([69,138,],[91,152,]),'special':([71,],[95,]),'outputaux':([72,128,],[106,143,]),'assiaux':([93,137,],[123,151,]),'spaux':([126,],[139,]),'returnaux':([148,156,],[157,163,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> KOTOBA ID ENDSTMT declare startaux BEGIN block END','start',8,'p_start','YaccKotoba.py',7),
  ('start -> KOTOBA ID ENDSTMT startaux BEGIN block END','start',7,'p_start','YaccKotoba.py',8),
  ('startaux -> function startaux','startaux',2,'p_startaux','YaccKotoba.py',12),
  ('startaux -> empty','startaux',1,'p_startaux','YaccKotoba.py',13),
  ('block -> OPENCURL blockaux CLOSECURL','block',3,'p_block','YaccKotoba.py',16),
  ('blockaux -> action blockaux','blockaux',2,'p_blockaux','YaccKotoba.py',19),
  ('blockaux -> empty','blockaux',1,'p_blockaux','YaccKotoba.py',20),
  ('action -> input','action',1,'p_action','YaccKotoba.py',23),
  ('action -> output','action',1,'p_action','YaccKotoba.py',24),
  ('action -> statement','action',1,'p_action','YaccKotoba.py',25),
  ('input -> READ OPENPAREN ID CLOSEPAREN ENDSTMT','input',5,'p_input','YaccKotoba.py',28),
  ('output -> WRITE OPENPAREN outputaux CLOSEPAREN ENDSTMT','output',5,'p_output','YaccKotoba.py',31),
  ('outputaux -> expression','outputaux',1,'p_outputaux','YaccKotoba.py',34),
  ('outputaux -> expression COMA outputaux','outputaux',3,'p_outputaux','YaccKotoba.py',35),
  ('declare -> DEC decaux','declare',2,'p_declare','YaccKotoba.py',38),
  ('decaux -> type ID declareaux','decaux',3,'p_decaux','YaccKotoba.py',41),
  ('decaux -> type ID OPENBRAC cte CLOSEBRAC declareaux','decaux',6,'p_decaux','YaccKotoba.py',42),
  ('declareaux -> ENDSTMT','declareaux',1,'p_declareaux','YaccKotoba.py',45),
  ('declareaux -> COMA decaux','declareaux',2,'p_declareaux','YaccKotoba.py',46),
  ('assign -> ID EQUAL assignaux','assign',3,'p_assign','YaccKotoba.py',49),
  ('assign -> ID OPENBRAC cte CLOSEBRAC EQUAL assignaux','assign',6,'p_assign','YaccKotoba.py',50),
  ('assignaux -> exp ENDSTMT','assignaux',2,'p_assignaux','YaccKotoba.py',53),
  ('assignaux -> OPENCURL assiaux CLOSECURL ENDSTMT','assignaux',4,'p_assignaux','YaccKotoba.py',54),
  ('assiaux -> exp','assiaux',1,'p_assiaux','YaccKotoba.py',57),
  ('assiaux -> exp COMA assiaux','assiaux',3,'p_assiaux','YaccKotoba.py',58),
  ('cte -> ID','cte',1,'p_cte','YaccKotoba.py',61),
  ('cte -> BOOLCTE','cte',1,'p_cte','YaccKotoba.py',62),
  ('cte -> NUMBERCTE','cte',1,'p_cte','YaccKotoba.py',63),
  ('cte -> WORDCTE','cte',1,'p_cte','YaccKotoba.py',64),
  ('cte -> SENTENCECTE','cte',1,'p_cte','YaccKotoba.py',65),
  ('type -> BOOL','type',1,'p_type','YaccKotoba.py',68),
  ('type -> NUMBER','type',1,'p_type','YaccKotoba.py',69),
  ('type -> WORD','type',1,'p_type','YaccKotoba.py',70),
  ('type -> SENTENCE','type',1,'p_type','YaccKotoba.py',71),
  ('statement -> assign','statement',1,'p_statement','YaccKotoba.py',74),
  ('statement -> expression','statement',1,'p_statement','YaccKotoba.py',75),
  ('statement -> condition','statement',1,'p_statement','YaccKotoba.py',76),
  ('statement -> cycle','statement',1,'p_statement','YaccKotoba.py',77),
  ('statement -> specialfunction','statement',1,'p_statement','YaccKotoba.py',78),
  ('expression -> relopexpression','expression',1,'p_expression','YaccKotoba.py',81),
  ('expression -> relopexpression AND expression','expression',3,'p_expression','YaccKotoba.py',82),
  ('expression -> relopexpression OR expression','expression',3,'p_expression','YaccKotoba.py',83),
  ('relopexpression -> exp','relopexpression',1,'p_relopexression','YaccKotoba.py',86),
  ('relopexpression -> exp RELOP exp','relopexpression',3,'p_relopexression','YaccKotoba.py',87),
  ('relopexpression -> NOT exp','relopexpression',2,'p_relopexression','YaccKotoba.py',88),
  ('exp -> term','exp',1,'p_exp','YaccKotoba.py',91),
  ('exp -> term PLUS exp','exp',3,'p_exp','YaccKotoba.py',92),
  ('exp -> term MINUS exp','exp',3,'p_exp','YaccKotoba.py',93),
  ('term -> factor','term',1,'p_term','YaccKotoba.py',96),
  ('term -> factor MULT term','term',3,'p_term','YaccKotoba.py',97),
  ('term -> factor DIV term','term',3,'p_term','YaccKotoba.py',98),
  ('factor -> OPENPAREN expression CLOSEPAREN','factor',3,'p_factor','YaccKotoba.py',101),
  ('factor -> cte','factor',1,'p_factor','YaccKotoba.py',102),
  ('condition -> IF OPENPAREN expression CLOSEPAREN block','condition',5,'p_condition','YaccKotoba.py',105),
  ('condition -> IF OPENPAREN expression CLOSEPAREN block ELSE block','condition',7,'p_condition','YaccKotoba.py',106),
  ('cycle -> WHILE OPENPAREN expression CLOSEPAREN block','cycle',5,'p_cycle','YaccKotoba.py',109),
  ('cycle -> DO block WHILE OPENPAREN expression CLOSEPAREN ENDSTMT','cycle',7,'p_cycle','YaccKotoba.py',110),
  ('function -> FUNC funcaux ID OPENPAREN parameteraux CLOSEPAREN OPENCURL declare blockaux returnaux ENDSTMT CLOSECURL','function',12,'p_function','YaccKotoba.py',113),
  ('function -> FUNC funcaux ID OPENPAREN parameteraux CLOSEPAREN OPENCURL blockaux returnaux ENDSTMT CLOSECURL','function',11,'p_function','YaccKotoba.py',114),
  ('funcaux -> type','funcaux',1,'p_funcaux','YaccKotoba.py',117),
  ('funcaux -> VOID','funcaux',1,'p_funcaux','YaccKotoba.py',118),
  ('parameteraux -> type ID','parameteraux',2,'p_parameteraux','YaccKotoba.py',121),
  ('parameteraux -> type ID COMA parameteraux','parameteraux',4,'p_parameteraux','YaccKotoba.py',122),
  ('parameteraux -> empty','parameteraux',1,'p_parameteraux','YaccKotoba.py',123),
  ('returnaux -> RETURN ID','returnaux',2,'p_returnaux','YaccKotoba.py',126),
  ('returnaux -> empty','returnaux',1,'p_returnaux','YaccKotoba.py',127),
  ('specialfunction -> ID DOT special OPENPAREN spaux CLOSEPAREN ENDSTMT','specialfunction',7,'p_specialfunction','YaccKotoba.py',130),
  ('spaux -> cte','spaux',1,'p_spaux','YaccKotoba.py',133),
  ('spaux -> empty','spaux',1,'p_spaux','YaccKotoba.py',134),
  ('special -> LENGTH','special',1,'p_special','YaccKotoba.py',137),
  ('special -> FREQUENCY','special',1,'p_special','YaccKotoba.py',138),
  ('special -> SEARCH','special',1,'p_special','YaccKotoba.py',139),
  ('special -> EXISTS','special',1,'p_special','YaccKotoba.py',140),
  ('special -> MEAN','special',1,'p_special','YaccKotoba.py',141),
  ('special -> MEDIAN','special',1,'p_special','YaccKotoba.py',142),
  ('special -> MODE','special',1,'p_special','YaccKotoba.py',143),
  ('special -> WORDCOUNT','special',1,'p_special','YaccKotoba.py',144),
  ('special -> TOKENIZE','special',1,'p_special','YaccKotoba.py',145),
  ('special -> REMOVE','special',1,'p_special','YaccKotoba.py',146),
  ('empty -> <empty>','empty',0,'p_empty','YaccKotoba.py',149),
]