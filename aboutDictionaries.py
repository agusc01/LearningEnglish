# -*- coding: utf-8 -*-
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