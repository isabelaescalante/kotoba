import ply.lex as lex

tokens = ['KOTOBA', 'BEGIN', 'END', 'READ', 'WRITE', 'DEC', 'BOOL', 'NUMBER', 'WORD', 'SENTENCE', 'IF', 'ELSE', 'DO', 'WHILE', 'FUNC', 'RETURN', 'VOID', 'LENGTH', 'FREQUENCY', 'SEARCH', 'EXISTS', 'MEAN', 'MEDIAN', 'MODE', 'WORDCOUNT', 'TOKENIZE', 'REMOVE', 'AND', 'OR', 'ID', 'BOOLCTE', 'NUMBERCTE', 'WORDCTE', 'SENTENCECTE', 'RELOP', 'PLUS', 'MINUS', 'MULT', 'DIV', 'NOT', 'ENDSTMT', 'COMA', 'DOT', 'OPENCURL', 'CLOSECURL', 'OPENPAREN', 'CLOSEPAREN', 'OPENBRAC', 'CLOSEBRAC', 'EQUAL']

reserved = {
    'kotoba' : 'KOTOBA',
    'begin' : 'BEGIN',
    'end' : 'END',
    'kread' : 'READ',
    'kprint' : 'WRITE',
    'declare' : 'DEC',
    'bool' : 'BOOL',
    'number' : 'NUMBER',
    'word' : 'WORD',
    'sentence' : 'SENTENCE',
    'if' : 'IF',
    'else' : 'ELSE',
    'do' : 'DO',
    'while' : 'WHILE',
    'function' : 'FUNC',
    'return' : 'RETURN',
    'void' : 'VOID',
    'length' : 'LENGTH',
    'frequency' : 'FREQUENCY',
    'search' : 'SEARCH',
    'exists' : 'EXISTS',
    'mean' : 'MEAN',
    'median' : 'MEDIAN',
    'mode' : 'MODE',
    'wordCount' : 'WORDCOUNT',
    'tokenize' : 'TOKENIZE',
    'remove' : 'REMOVE'
}

t_ignore = ' \t\n'
t_KOTOBA = r'"kotoba"'
t_BEGIN = r'"begin"'
t_END = r'"end"'
t_READ = r'"kread"'
t_WRITE = r'"kwrite"'
t_DEC = r'"declare"'
t_BOOL = r'"bool"'
t_NUMBER = r'"number"'
t_WORD = r'"word"'
t_SENTENCE = r'"sentence"'
t_IF = r'"if"'
t_ELSE = r'"else"'
t_DO = r'"do"'
t_WHILE = r'"while"'
t_FUNC = r'"function"'
t_RETURN = r'"return"'
t_VOID = r'"void"'
t_LENGTH = r'"length"'
t_FREQUENCY = r'"frequency"'
t_SEARCH = r'"search"'
t_EXISTS = r'"exists"'
t_MEAN = r'"mean"'
t_MEDIAN = r'"median"'
t_MODE = r'"mode"'
t_WORDCOUNT = r'"wordCount"'
t_TOKENIZE = r'"tokenize"'
t_REMOVE = r'"remove"'
t_AND = r'\&'
t_OR = r'\|'
t_NUMBERCTE = r'[\+|\-]?[0-9]+(\.[0-9]+)'
t_WORDCTE = r'\"[a-zA-Z0-9]+\"'
t_SENTENCECTE = r'\"(.*?)\"'
t_RELOP = r'(< | > | == | !=)'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULT = r'\*'
t_DIV = r'\/'
t_NOT = r'\!'
t_ENDSTMT = r'\;'
t_COMA = r'\,'
t_DOT = r'\.'
t_OPENCURL = r'\{'
t_CLOSECURL = r'\}'
t_OPENPAREN = r'\('
t_CLOSEPAREN = r'\)'
t_OPENBRAC = r'\['
t_CLOSEBRAC = r'\]'
t_EQUAL = r'\='

def t_BOOLCTE(t) :
    r'true|false'
    t.value = bool(t.value)
    return t


def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

def t_error(t) :
    print("Error en token: %s" % t.value)
    t.lexer.skip(1)

#Build the lexer
lex.lex()
