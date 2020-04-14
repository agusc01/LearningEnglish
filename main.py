# -*- coding: utf-8 -*-
from irregularNouns import *
from menu import mainMenu

def main():

	option = mainMenu()

	if option == '1':
		printNiceIrregularNouns(irregularNouns)

	elif option == '2':
		singular = input("noun?: ").lower()
		print("")
		endWith = singular[len(singular)-2:]
		print(endWith)

		if not singular in irregularNouns:

			#Este if esta si ingresan el plural de un sust. irregular
			if checkValuesOfDictionary(singular,irregularNouns):
				badIrregularesCases(singular,irregularNouns)

			#Casos con sustantivo regulares
			elif endWith=="ch" or endWith[1]=="s" or endWith=="sh" or endWith[1]=="x" or endWith[1]=="o":
				multiplesCases(singular)

			elif len(singular)>3 and endWith[1]=="y":
				yCase(singular)

			#Casos con sustantivo que termina con "f"
			elif endWith[1]=="f" and endWith[0]!='f':
				fCase(singular)

			#Casos con sustantivo que termina con "fe"
			elif endWith=="fe":
				feCase(singular)

			else:
				commonCase(singular)
				# Casos comunes agrego "s"

		#Casos con sustantivo irregulares
		else:
			goodIrregularesCases(singular)
			
	else: #opcion!= a los valores mostrados
		pass





main()
