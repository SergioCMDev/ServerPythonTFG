# -*- coding: utf-8 -*-
# ! python3
"""
@author: wesrok
"""
from ..Utilidades.Constantes import Constantes
import numpy as np
from pandas import DataFrame



class UtilidadesMatriz:
    
    def __init__(self):
        print("Clase UtilidadesMatriz Cargada Correctamente")


    def obtenerValoresLista(self, valores):
        listaFilas = list()
        for valor in valores:
            
                if (valor not in listaFilas):
                    listaFilas.append(valor)
                   
        return listaFilas
    
    
    #posicion = 1 para columnas, posicion = 0 para filas
    def ObtenerParametros(self, columnas, tuples, posicion):
        listaValores = list()
        
        if columnas[posicion] == 'Mes': #OK
            valores = Constantes.Meses
        elif columnas[posicion] == 'Ciudad': #OK
            valores = tuples.Ciudad
        elif columnas[posicion] == 'Anio': #OK
            valores = tuples.Anio    
        elif columnas[posicion] == 'Cantidad': #OK
            valores = ['Cantidad']
        elif columnas[posicion] == 'Numero_Vuelos':
            valores = ['Numero_Vuelos']
        elif columnas[posicion] == 'Numero_Turistas':
            valores = ['Numero_Vuelos']
        elif columnas[posicion] == 'Pais_Origen':
            valores = tuples.Pais_Origen
        elif columnas[posicion] == 'Ciudad_Origen':
            valores = tuples.Ciudad_Origen
        elif columnas[posicion] == 'Ciudad_Destino':
            valores = tuples.Ciudad_Destino
        else: 
            print ('El valor"',columnas[posicion],'" no existe')
            
        listaValores = self.obtenerValoresLista(valores)
        
        return listaValores
    
    
    def createMatrizCantidad(self, tuples, anioInicio, anioFin, columnas):
        
        #Obtenemos datos de Filas
        listaFilas = self.ObtenerParametros(columnas, tuples, 0)
        
        #Obtenemos datos de columnas
        listaColumnas = self.ObtenerParametros(columnas, tuples, 1)
        np.set_printoptions(threshold='nan')
        #Obtenemos valores a introducir en matriz
        posValores = len(columnas)-1
        valores = self.obtenerValoresMatriz(tuples, posValores, columnas)
#        print(listaFilas)
#        print("\n")
#        print(len(listaColumnas))
#        print("\n")
#        print(valores)
#        print("\n")
        np.set_printoptions(threshold='nan')

        #Creamos y Rellenamos matriz
        matrizRellena = self.rellenarMatriz(listaFilas, listaColumnas, valores)
        
        #Creamos DataFrame de la matriz
        retval = DataFrame(matrizRellena, index = listaFilas, columns = listaColumnas)
        retval.index.name = columnas[0]
        return retval, listaFilas     
    

    def rellenarMatriz(self, listaFilas, listaColumnas, valores):
        #Creamos filas y colummnas en matriz
        matriz = []   
        for f in np.arange(0, len(listaFilas),1):
            matriz.append([f] * len(listaColumnas))
            
            
        #Rellenamos matriz
        for filas in np.arange(0, len(listaFilas), 1):
            for columnas in np.arange(0, len(listaColumnas),1):
                pos = filas * len(listaColumnas) + columnas
#                print(filas,  columnas, valores[pos])
                matriz[filas][columnas] = int(valores[pos])
        return matriz
    
    
    def obtenerValoresMatriz(self, tuples, posValores, columnas):
        if columnas[posValores] == 'Cantidad':
            valores =  tuples.Cantidad
        elif columnas[posValores] == 'Numero_Turistas':
            valores = tuples.Numero_Turistas
        elif columnas[posValores] == 'Numero_Vuelos':
            valores = tuples.Numero_Vuelos
        else:
            print ('El valor',columnas[posValores],' no existe')
            
        return valores
    
    
    
    def getMatrizDatos(self, tuplas, columnas, anioInicio, anioFin):

        num_columns = len(columnas)
        lista = list()
        matriz = []
   
        if num_columns == 2:
             if ('Anio' in columnas[0] or 'Ciudad_Destino' in columnas[0] or 'Ciudad_Origen' in columnas[0] or 'Mes' in columnas[0])  and ('Cantidad' in columnas[1] or 'Numero_Vuelos' in columnas[1] or 'Numero_Turistas' in columnas[1]):
                 matriz, lista =  self.createMatrizCantidad(tuplas, anioInicio, anioFin, columnas)

        elif  num_columns == 3:
            if ('Anio' in columnas[0] or 'Ciudad_Origen' in columnas[0] or 'Ciudad_Destino' in columnas[0])  and  ('Mes' in columnas[1] or 'Ciudad_Origen' in columnas[1] or 'Ciudad_Destino' in columnas[1]) and ('Cantidad' in columnas[2] or 'Numero_Turistas' in columnas[2] or 'Numero_Vuelos' in columnas[2]):
               matriz, lista =  self.createMatrizCantidad(tuplas, anioInicio, anioFin, columnas)
               
        return matriz, lista


