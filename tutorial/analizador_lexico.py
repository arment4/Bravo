import ply.lex as lex
import re 
import codecs
import os
import sys


reserved_word = ['BEGIN','END','IF','THEN','WHILE','DO','CALL','CONST','VAR','PROCEDURE','OUT','IN','ELSE']

tokens = reserved_word + [ 'ID','NUMBER','PLUS','MINUS','TIMES','DIVIDE','ODD','ASSIGN','NE','LT','LTE','GT','GTE','LPARENT','RPARENT','COMMA','SEMMICOLOM','DOT','UPDATE'
]


t_ignore = '\t'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_ODD = r'ODD'
t_ASSIGN = r'='
t_NE = r'<>'
t_LT = r'<'
t_LTE = r'<='
t_GT = r'>'
t_GTE = r'>='
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_COMMA = r','
t_SEMMICOLOM = r';'
t_DOT = r'\.'
t_UPDATE = r':='


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value.upper() in reserved_word:
        t.value = t.value.upper()
        t.type = t.value 
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

path = 'test/'
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


