def mainMenu():
	import time
	print('Date: '+time.strftime("%m-%d-%Y"))
	print("What do you want to do? / ¿Qué quieres hacer?")
	print("1- List of irregular nouns / Lista de sustantivos irregulares")
	print("2- Know the plural of a noun / Saber el plural de un sustantivo")
	print("3- Exit / salir")
	del time
	return input("Option? / ¿Opción?: ")