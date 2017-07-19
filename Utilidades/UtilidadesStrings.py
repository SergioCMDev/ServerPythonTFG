# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 12:28:06 2017

@author: wesrok
"""
from decimal import *
class UtilidadesString():
	def __init__(self):
		#super(ClassName, self).__init__()
		print("Clase UtilsString Cargada Correctamente")

	def showList(self, lista):
		for row in lista:
			print(str(row[0])+": "+str(row[1]) +"->"+str(row[2]))

	def save_data(self, lista):
		X_values = []
		Y_values = []
		for pares in lista:
			#print(pares[1])
			X_values.append(int(pares[0]))
			Y_values.append(int(pares[1]))
		return (X_values, Y_values)
