# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 12:28:06 2017

@author: wesrok
"""
from Utilidades.UtilidadesMatriz import UtilidadesMatriz as UtilidadesMatriz
from DB.DBRepository import DBRepository as DBRepository
from Utilidades.Graphics import Graphics as Graphics
from Utilidades.Conversores import ConversorCursorJson as Conversores
from Utilidades.DeteccionOutliers import DeteccionOutliers as DeteccionOutliers
############################################################################################
from pandas import DataFrame

#from decimal import Decimal
#import json

import pandas as pd
import numpy as np

#from sklearn import svm
###################################################################################

class Index():
       
    matrix = UtilidadesMatriz()
    graphics = Graphics()
    repository = DBRepository()
    deteccionOutliers = DeteccionOutliers()
#    conversor = Conversores()
    anioInicio = 2010
    anioFin  = 2015
    pais = 'Spain'
    pais_1 = 'Belgium'
    mes = 'Enero'
    ciudadDestino = 'Valencia'
    """Llamadas a BD"""
    
    
#    cursor, labels =  repository.ObtenerNumeroTuristasAenaAnualmenteDadoPaisDestinoAnioMinMaxSeparadoPorMeses("Spain", anioInicio, anioInicio)

#    cursor, labels =  repository.ObtenerDatosVuelosAenaSalientesDadoPaisOrigenAnio(pais_1, anioInicio) 
#    cursor, labels = repository.ObtenerDatosVuelosEntrantesAenaEnUnMesDadoPaisDestinoCiudadDestinoMesAnioMinMax("Spain", "Malaga", "Enero", anioInicio, anioFin)
    cursor, labels = repository.ObtenerDatosVuelosEntrantesAenaDadoPaisDestinoAnioMinMax('Spain', anioInicio, anioFin)
#    cursor, labels = repository.ObtenerDatosVuelosEntrantesAenaMensualmenteDadoPaisDestinoAnio('Spain', anioInicio)                    

#    cursor, labels = repository.ObtenerDatosVuelosEntrantesAenaDivididosPorCiudadesDadoPaisDestinoAnioMinMax(pais, anioInicio, anioFin)

#    cursor, labels = repository.ObtenerDatosTuristasMensualmenteAenaDadoPaisDestinoCiudadAnio(pais, 'Alicante', anioInicio)
    
#    cursor, labels = repository.ObtenerDatosVuelosEntrantesAenaMensualmenteDadoPaisDestinoAnioMinMax(pais, anioInicio, anioFin)
#    cursor, labels = repository.ObtenerDatosVuelosEntrantesEnUnMesAenaDivididosPorCiudadesDadoPaisDestinoMesAnioMinMax(pais, mes, anioInicio, anioFin)
#    cursor, labels = repository.ObtenerDatosVuelosEntrantesAenaEnUnAnioDivididosPorCiudadDadoPaisDestinoAnio(pais, anioInicio)
#    cursor, labels = repository.ObtenerDatosVuelosEntrantesAenaMensualmenteDivididosPorCiudadDadoPaisDestinoMesAnio(pais, mes, anioInicio)

#    cursor, labels = repository.ObtenerDatosTuristasMensualmenteAenaDadoPaisDestinoCiudadAnio(pais, ciudadDestino, anioInicio)

#    cursor, labels = repository.ObtenerPaisOrigenYNumeroTuristasAenaAnualmenteDadoPaisDestinoAnioMinMaxSeparadoPorCiudades(pais, anioInicio, anioFin)
#    cursor, labels = repository.ObtenerNumeroTuristasAenaAnualmenteDadoPaisDestinoAnioMinMaxSeparadoPorMeses(pais, anioInicio, anioFin)
        
###############################################################################################################################################################
#    json_output = Conversores.convertirAJson(Conversores, cursor = dataFromDB)
#    print(json_output)
####################################################################################################################################################################################
    if cursor.rowcount != 0:
#        progresionLineal.obtenerPrediccion(cursor, (AnioFin+1))

###############################################################################################################################################################
        np.set_printoptions(threshold='nan')
####################################################################################################################################################################################
        dataFromDB = list(cursor.fetchall())        
        print (dataFromDB, labels)
#        print (dataFromDB)
#        print (labels)
####################################################################################################################################################################################


#        matriz, lista = matrix.getMatrizDatos(cursor, labels, anioInicio, anioInicio)



#        tipo = "Eliptic"
#        deteccionOutliers.showOutliersMedianteEnvolturaElipticaDadosDatos(matriz, anioInicio_1, (anioInicio_1+2), (anioInicio_1+3), tipo)

#        outliersList, inliersList = deteccionOutliers.getOutliersMedianteEnvolturaElipticaDadaMatrizYAnios(matriz, AnioInicio_1, (AnioInicio_1+2), (AnioInicio_1+3), tipo)
#        

#        graphics.obtenerValoresParaDibujarGrafica(matriz, lista, labels)




#        mean = matriz.loc[2009].mean(axis = 0)
#        sd = matriz.loc[2009].std(axis = 0)
#        print('Media '+str(mean))
#        print('SD '+str(sd))
