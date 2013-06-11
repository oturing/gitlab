#!/usr/bin/env python
# coding: utf-8

"""
Também gera arquivos de amostra para exercícios de controle de versão.
"""

import sys, re

PALAVRAS = '''Alfa Bravo Charlie Delta Echo Foxtrot Golf Hotel India Juliett
              Kilo Lima Mike November Oscar Papa Quebec Romeo Sierra Tango
              Uniform Victor Whiskey Xray Yankee Zulu'''.split()

QT_EXIBIR = 3

nao_palavra = re.compile(r'\W+')

uso_incorreto = False

num_palavras = -1
if len(sys.argv) != 2:
    uso_incorreto = True
else:    
    arg = sys.argv[1]
    try:
        num_palavras = int(arg)
    except ValueError:
        uso_incorreto = True

if uso_incorreto or num_palavras == -1:
    print 'modo de usar:'
    print '\t%s -<N>                     # gerar lista de N palavras (-0 = todas)' % sys.argv[0]
    sys.exit(1)

if num_palavras > -1:
    if num_palavras == 0:
        num_palavras = len(PALAVRAS)
    pular = len(PALAVRAS)/num_palavras
    if pular == 0:
        pular = 1
    for palavra in PALAVRAS[::pular][:num_palavras]:
        print palavra
    sys.exit(0)
