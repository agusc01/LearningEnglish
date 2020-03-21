# -*- coding: utf-8 -*-
#poniendo acentos 
print ("áéíóú àèìòù Ñ")

print("\n#==========================================================",end="\n\n")
#==========================================================

def printNice(thing):
	print(type(thing))

stuff=(
			0,
			1.2,
			"str",
			["list"],
			("tuple",),
			{'dic':8}
			)

for c in stuff:
	printNice(c)


print("\n#==========================================================",end="\n\n")
#==========================================================

a="watch"
print(a[len(a)-2:])
plural=a[:len(a)-1]
print(plural)

print("\n#==========================================================",end="\n\n")
#==========================================================

"""
import sys
import os

if sys.platform == "win32":
	print('Yes')
	cmd="color a"
else:
	print('No')

"""

import time
fecha_actual = time.strftime("%Y-%m-%d")
print(fecha_actual)

print("\n#==========================================================",end="\n\n")
#==========================================================