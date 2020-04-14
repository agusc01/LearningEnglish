# -*- coding: utf-8 -*-
from aboutDictionaries import *

#la clave es singular, y el valor es el plural
irregularNouns={
								'man':'men',
								'woman':'women',
								'fish':'fish',
								'tooth':'teeth',
								'foot':'feet',
								'deer':'deer',
								'child':'children',
								'mouse':'mise',
								'analysis':'analyses',
								'thesis':'theses',
								'hypothesis':'hypotheses',
								'criterion':'criteria',
								'phenomenon':'phenomena',
								'nucleus':'nuclei',
								'stimulus':'stimuli',
								'person':'people',
								'sheep':'sheep',
								'means':'means',
								'adventure':'adventure'
								}

#============================================================
def printNiceIrregularNouns(dic):
	"""
		Esta función imprime los sustantivos irregulares
	"""
	print("")
	print("Singular -> Plural")
	
	lista=[] #lista vacia creada para operaciones auxiliaress

	for key in dic:
		lista.append(key)

	lista.sort()#ordeno las "keys" del diccionario

	#imprimo el diccionario ordenadamente, gracias a la "lista"
	for key in lista:
		print(key+" -> "+dic[key])


"""
	Esta función toma una palabra singular y la convierte en plural

	
"""

def	badIrregularesCases(singular,irregularNouns):
	""" Casos irregulares """
	print("Sustantivo irregular")
	singular=giveMeTheKey(singular,irregularNouns)
	print('Ingresaste el plural , '+irregularNouns[singular]+", el singular -> "+singular)

def goodIrregularesCases(singular):
	print("Sustantivo irregular")
	print(singular+" -> "+irregularNouns[singular])	

def commonCase(singular):
  """ Casos comunes agrego 's' """
  plural=singular+"s"
  print(singular+' -> '+plural)
  print('Casos comunes agrego "s"')

def feCase(singular):
	""" Si terminan con "f,fe" elimino "f,fe" y agrego "ves" """
	plural=singular[:len(singular)-2]+"ves"
	print(singular+" -> "+plural)
	print('Si terminan con "f,fe" elimino "f,fe" y agrego "ves"')

def fCase(singular):
  plural=singular[:len(singular)-1]+"ves"
  print(singular+" -> "+plural)
  print('Si terminan con "f,fe" elimino "f,fe" y agrego "ves"')

def multiplesCases(singular):
	""" Si terminan con "ch,s,sh,x,o" agrego "es" """
	print("Sustantivo regular")
	plural=singular+"es"
	print(singular+" -> "+plural)
	print('Si terminan con "ch,s,sh,x,o" agrego "es"')

def yCase(singular):

	plural=singular[:len(singular)-1]+"ies"
	print(singular+" -> "+plural)
	print('Si termina con "y" cambio "y" por "ies')