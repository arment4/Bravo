import ply.lex as lex
import re 
import codecs
import os
import sys


reserved_word = ['INT','STRING','CLASS','SELF','IF','ELSE','CONST','FOR','WHILE','IN','DEF','FUNC','IMPORT','FROM','AS']

tokens = reserved_word + [ 'ID','CHAR','NUMBER','PLUS','MINUS','PRODUCT','DIVIDE','MODULE','ASSIGN','NE','LT','LTE','GT','GTE','LPARENT','RPARENT','DOT','COMMA','SEMMICOLON','COLON']


t_ignore = '\t'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_PRODUCT = r'\*'
t_DIVIDE = r'/'
t_MODULE = r'%'
t_ASSIGN = r'='
t_NE = r'!='
t_LT = r'<'
t_LTE = r'<='
t_GT = r'>'
t_GTE = r'>='
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_COMMA = r','
t_SEMMICOLON = r';'
t_DOT = r'\.'
t_COLON = r':'


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value.upper() in reserved_word:
        t.value = t.value.upper()
        t.type = t.value 
    return t

def t_CHAR(t):
    r'\".*"'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_COMMENT(t):
    r'\#.*'
    pass

def t_NUMBER(t):
    r'\d+'
    t.value=int(t.value)
    return t
    
def t_ccode_nonspace(t):
    r'\s+'
    pass

def t_error(t):
    print ("caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)


def searchFiles(path):
    ficheros=[]
    numOffiles = ''
    response = False
    cont = 1 

    for base, dirs, files in os.walk(path):
        ficheros.append(files)

    for file in files:
        print(str(cont)+". "+file)
        cont = cont+1

    while response==False:
        numOffiles = input('\nNumero del test: ')
        for file in files:
            if file == files[int(numOffiles)-1]:
                response = True
                break

    print("Has escogido \"%s\" \n" %files[int(numOffiles)-1])

    return files[int(numOffiles)-1]

path = 'codigo/'
archivo = searchFiles(path)
test = path + archivo
fb = codecs.open(test,"r","utf-8")
cadena = fb.read()
fb.close()

analizador = lex.lex()

analizador.input(cadena)

while True:
    tok = analizador.token()
    if not tok : break
    print(tok)


