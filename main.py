# -*- coding: utf-8 -*-

def printNiceIrregularNouns(dic):
	"""
		Esta función imprime los sustantivos irregulares
	"""
	print("")
	print("Singular -> Plural")
	
	lista=[]

	for key in dic:
		lista.append(key)

	lista.sort()#ordeno las "keys" del diccionario

	#imprimo el diccionario ordenadamente, gracias a la "lista"
	for key in lista:
		print(key+" -> "+dic[key])
	
#============================================================

def checkValuesOfDictionary(value,dic):
	"""
		Esta función devuelve [False] si encuentra "value" como un
		valor de una clave del diccionario "dic", si llegase a
		entrontrar algun valor del diccionario igual a "value",
		entonces devolvera [True].
	"""
	flag=False

	for key in dic:
		if dic[key]==value:
			flag=True
			break

	return flag

#============================================================

def giveMeTheKey(value,dic):
	"""
		Esta función devuelve la clave 'key', atribuida a "value",
		en el diccionario 'dics'
	"""

	for key in dic:
		if dic[key]==value:
			return key

#============================================================
def main():

	"""
		Esta función toma una palabra singular y la convierte en plural

		Casos comunes agrego "s"
		Si terminan con "ch,s,sh,x,o" agrego "es"
		Si terminan con "f,fe" elimino "f,fe" y agrego "ves"
	"""

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


	#printNiceIrregularNouns(irregularNouns)
	print("What do you want to do? / ¿Qué quieres hacer?")
	print("1- List of irregular nouns / Lista de sustantivos irregulares")
	print("2- Know the plural of a noun / Saber el plural de un sustantivo")
	print("3- Exit / salir")

	option = input("Option? / ¿Opción?: ")

	if option == '1':
		printNiceIrregularNouns(irregularNouns)

	elif option == '2':
		singular = input("noun?: ")
		print("")
		endWith = singular[len(singular)-2:]
		plural = ""

		if not singular in irregularNouns:

			#Este if esta si ingresan el plural de un sust. irregular
			if checkValuesOfDictionary(singular,irregularNouns):
				print("Sustantivo irregular")
				singular=giveMeTheKey(singular,irregularNouns)
				print('Ingresaste el plural , '+irregularNouns[singular]+", el singular -> "+singular)


			#Casos con sustantivo regulares
			elif endWith=="ch" or endWith[1]=="s" or endWith=="sh" or endWith[1]=="x" or endWith[1]=="o":
				print("Sustantivo regular")
				plural=singular+"es"
				print(singular+" -> "+plural)
				print('Si terminan con "ch,s,sh,x,o" agrego "es"')

			elif len(singular)>3 and endWith[1]=="y":
			  plural=singular[:len(singular)-1]+"ies"
			  print(singular+" -> "+plural)
			  print('Si termina con "y" cambio "y" por "ies')


			#Casos con sustantivo que termina con "f"
			elif endWith[1]=="f":
			  plural=singular[:len(singular)-1]+"ves"
			  print(singular+" -> "+plural)
			  print('Si terminan con "f,fe" elimino "f,fe" y agrego "ves"')

			#Casos con sustantivo que termina con "fe"
			elif endWith=="fe":
				plural=singular[:len(singular)-2]+"ves"
				print(singular+" -> "+plural)
				print('Si terminan con "f,fe" elimino "f,fe" y agrego "ves"')

			else:
				plural=singular+"s"
				print(singular+" -> "+plural)
				print('Casos comunes agrego "s"')

		#Casos con sustantivo irregulares
		else:
			print("Sustantivo irregular")
			print(singular+" -> "+irregularNouns[singular])

	else: #opcion!= a los valores mostrados
		pass





main()