# -*- coding: utf-8 -*-
# ! python3
"""
@author: wesrok
"""
from ..Utilidades.Constantes import Constantes
import numpy as np
from pandas import DataFrame
import pandas as pd



class UtilidadesMatriz:
    
    def __init__(self):
        print("Clase UtilidadesMatriz Cargada Correctamente")


    def obtenerValoresLista(self, valores):
        listaFilas = list()
        for valor in valores:
            
                if (valor not in listaFilas):
                    listaFilas.append(valor)
                   
        return listaFilas
    
    
    #Obtenemos los valores de las ciudades que se corresponden con las ciudades iniciales
    def GetValuesArrayStrings(self, valorInicial, ValorFinal, matriz, numColumnas):
        return matriz.loc[valorInicial : ValorFinal]["Cantidad"]
        #TODO COMPROBAR SI ALGO HA CAMBIADO
#        listaCiudades = list()
#        
#        for filas in matriz.iterrows():
#            
#            listaCiudades.append(filas[0])
#            if filas[0] == ValorFinal:
#                break
#        
#        valoresCiudades = np.zeros(len(listaCiudades) * numColumnas)
#        pos = 0
#        for ciudad in listaCiudades:
#            datos = matriz.loc[ciudad]
#            for i in np.arange(0, numColumnas):
#                valoresCiudades[pos] = datos[i]
#                pos = pos +1
##               
#        s = pd.Series(valoresCiudades)
#        s = s.astype(int)
#
#        return s
    
    #Obtenemos los valores de los anios que se corresponden con los anios iniciales y los devolvemos en una serie
    def GetValuesArrayIntegers(self, valorInicial, ValorFinal, matriz, numColumnas):
        #TODO COMPROBAR SI ALGO HA CAMBIADO

#        num_anios = AnioFin - AnioInicio +1
#        array_1 = np.zeros(num_anios * numColumnas)
#
#        anios = np.arange(AnioInicio, AnioFin+1, 1)
#        pos = 0
#        
#        for anio in anios:
#            datos = matriz.loc[anio]
#            for i in np.arange(0, numColumnas): #Valido tanto para meses como columna como para una sola columna
#                array_1[pos] = datos[i]
#                pos = pos +1
#                
#        s = pd.Series(array_1)
#        s = s.astype(int)
#        
#        return s
        return matriz.loc[valorInicial : ValorFinal]["Cantidad"]

    
    
    #posicion = 1 para columnas, posicion = 0 para filas
    def obtenerParametros(self, columnas, tuples, posicion):
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
        elif columnas[posicion] == 'Pais':
            valores = tuples.Pais
        elif columnas[posicion] == 'Ciudad_Destino':
            valores = tuples.Ciudad_Destino
        else: 
            print ('El valor"',columnas[posicion],'" no existe')
            
        listaValores = self.obtenerValoresLista(valores)
        
        return listaValores
    
    
    def createMatrizCantidad(self, tuples, columnas):
        
        #Obtenemos datos de Filas
        listaFilas = self.obtenerParametros(columnas, tuples, 0)
        
        #Obtenemos datos de columnas
        listaColumnas = self.obtenerParametros(columnas, tuples, 1)
        np.set_printoptions(threshold='nan')
        #Obtenemos valores a introducir en matriz
        posValores = len(columnas)-1
        valores = self.obtenerValoresMatriz(tuples, posValores, columnas)
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
    
    
    
    def ObtenerMatrizDatos(self, tuplas, columnas):

        num_columns = len(columnas)
#        print(columnas)
        lista = list()
        matriz = []
        if num_columns == 2:
             if ('Anio' in columnas[0] or 'Ciudad_Destino' in columnas[0] or 'Ciudad_Origen' in columnas[0] or 'Mes' in columnas[0] or 'Ciudad' in columnas[0] or 'Pais' in columnas[0])  and ('Cantidad' in columnas[1] or 'Numero_Vuelos' in columnas[1] or 'Numero_Turistas' in columnas[1]):
                matriz, lista =  self.createMatrizCantidad(tuplas, columnas)

        elif  num_columns == 3:
            if ('Mes' in columnas[0] or 'Anio' in columnas[0] or 'Ciudad_Origen' in columnas[0] or 'Ciudad_Destino' in columnas[0])  and  ('Pais' in columnas[1] or 'Pais_Origen' in columnas[1] or 'Mes' in columnas[1] or 'Ciudad_Origen' in columnas[1] or 'Ciudad_Destino' in columnas[1]) and ('Cantidad' in columnas[2] or 'Numero_Turistas' in columnas[2] or 'Numero_Vuelos' in columnas[2]):
                matriz, lista =  self.createMatrizCantidad(tuplas, columnas)
               
        return matriz, lista


