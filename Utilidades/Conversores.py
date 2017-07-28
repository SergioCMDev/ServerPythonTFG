# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 15:10:19 2017

@author: wesrok
"""
from decimal import Decimal
import json
from pandas import DataFrame
from ..Utilidades.UtilidadesMatriz import UtilidadesMatriz as UtilidadesMatriz
matrix = UtilidadesMatriz()

class Conversores:   
    def __init__(self):
        print("Clase Conversores Cargada Correctamente ")
        
    @staticmethod
    def default(obj):
        if isinstance(obj, Decimal):
            return str(obj)
        raise TypeError
        
    def convertirAJson(self, data):
#        retval =  json.dumps(cursor, use_decimal = True)
        retval =  json.dumps(data, default=self.default, separators=(',', ':'))

        return retval 
    
    def ObtenerDataJSONExtendido(self, matriz):
        #    print(matriz)
        data = matriz.to_json(orient ='table')
#        print(test+"\n")
        pos = data.find('"data": ')
#    print(pos)
        tamRestante = len(data) - pos
#    print(tamRestante)
        data = data[pos+8 :pos + tamRestante-1]
        return data
    
    def ConvertirCursorToTuplas(self, cursor):
        retVal = list()
        listaCursor = list()
        for elem in cursor.description:
            listaCursor.append(elem[0])
        

        for (listaCursor) in cursor:
            tuples = listaCursor
#            print(tuples)
            retVal.append(tuples)
        
        return retVal

    def ConvertirTuplasToMatriz(self, tuplas, labels, anioInicio, anioFin):
#        print(labels)
#        print(tuplas)
        tuplasMatriz = DataFrame(tuplas, columns = labels)
        
#        print(tuplasMatriz)
        
        matriz, lista = matrix.getMatrizDatos(tuplasMatriz, labels, anioInicio, anioFin)
        return matriz, lista

    def GetComponentesXY(self, lista):
        X_values = []
        Y_values = []
        for pares in lista:
			#print(pares[1])
            X_values.append(int(pares[0]))
            Y_values.append(int(pares[1]))
        return (X_values, Y_values)
    
class DecimalEncoder(json.JSONEncoder):
    def _iterencode(self, obj, markers=None):
         if isinstance(obj, Decimal):
            return str(obj)
         raise TypeError
         
