def mainMenu():
	import time
	print('Date: '+time.strftime("%m-%d-%Y"))
	del time
	language=input('English or Spanish (enter E or S):').lower()
	print('')
	option=3
	if language=='e':
		print("What do you want to do? ")
		print("1-List of irregular nouns")
		print("2-Know the plural of a noun")
		print("3-Exit")
		option=input("Option?: ")
	elif language=='s':
		print("¿Qué quieres hacer?")
		print("1-Lista de sustantivos irregulares")
		print("2-Saber el plural de un sustantivo")
		print("3-Salir")
		option=input("Opcion?: ")
	else:
		print('Error!')

	return option