import numpy as np
from ..Utilidades.Graphics import Graphics as Graphics
from sklearn.covariance import EllipticEnvelope
from ..Utilidades.Constantes import Constantes

import pandas as pd

class DeteccionOutliers:
    
    def setDataValues(self, matriz, anioTrainInicio, AnioTrainFin, AnioTest, labels):
        if 'Anio' in labels[0] and 'Cantidad' in labels[1]:
            numColumnas = 1
#            print (1)
#        serieDataAniosCantidad = 
            serieDataAnios = self.joinArrayAnios(anioTrainInicio, AnioTrainFin, matriz, numColumnas )
#            print(serieDataAnios)
#            print (anioTrainInicio)
#            print (AnioTrainFin)

            indices = np.arange(int(anioTrainInicio), int(AnioTrainFin)+1,1)
            
            datosOriginales = np.column_stack((indices, serieDataAnios))
#            print(datosOriginales[0][1])

            datosATestear = np.column_stack((AnioTest, matriz.loc[AnioTest]))
            return datosOriginales, datosATestear
        
        
        
        
    ##Llamar a este metodo
    def getOutliersMedianteEnvolturaElipticaDadaMatrizYAnios(self, matriz, anioTrainInicio, AnioTrainFin, AnioTest, listaLabels):
        datosOriginales, datosATestear = self.setDataValues(matriz, anioTrainInicio, AnioTrainFin, AnioTest, listaLabels)
#        print(datosOriginales)
#        print(datosATestear)
        outliersValuesList, inliersValuesList =   self.getOutliersMedianteEnvolturaElipticaDadosDatos(datosOriginales, datosATestear)
#        print('ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff')
        return outliersValuesList, inliersValuesList
        
    
    
    
    def joinArrayAnios(self, anioInicio, AnioFin, matriz, numColumnas):
#        numColumnas = 12
        num_anios = AnioFin - anioInicio +1
        array_1 = np.zeros(num_anios * numColumnas)

        anios = np.arange(anioInicio, AnioFin+1, 1)
        pos = 0
        
        for anio in anios:
            datos = matriz.loc[anio]
            for i in np.arange(0,numColumnas):
                array_1[pos] = datos[i]
                pos = pos +1
                
        s = pd.Series(array_1)
        s = s.astype(int)
        
        return s



#NO TOCAR
#    def setDataValues(self, matriz, anioTrainInicio, AnioTrainFin, AnioTest, labels):
#        if 'Anio' in labels[0] and 'Cantidad' in labels[1]:
#            numColumnas = 1
##        serieDataAniosCantidad = 
#            serieDataAnios = self.joinArrayAnios(anioTrainInicio, AnioTrainFin, matriz, numColumnas )
#            print(serieDataAnios)
##       
#            indices = np.arange(0,12,1)
##        indices = np.tile(indices, AnioTrainFin - anioTrainInicio)
##        datosOriginales = np.column_stack((indices, serieDataAnios))
##        datosATestear = np.column_stack((np.arange(1,13,1), matriz.loc[AnioTest]))
##        return datosOriginales, datosATestear
        






#    def joinArrayAnios(self, anioInicio, AnioFin, matriz):
#        numColumnas = 12
#        num_anios = AnioFin - anioInicio
#        array_1 = np.zeros(num_anios * numColumnas)
#
#        anios = np.arange(anioInicio, AnioFin, 1)
#        pos = 0
#        
#        for anio in anios:
#            datos = matriz.loc[anio]
#            for i in np.arange(0,numColumnas):
#                array_1[pos] = datos[i]
#                pos = pos +1
#                
#        s = pd.Series(array_1)
#        s = s.astype(int)
#        
#        return s
        
    
    
    def getOutliersMedianteEnvolturaElipticaDadosDatos(self, datosOriginales, datosATestear):

#        print("El tipo elegido es ", tipo)
        clf = EllipticEnvelope(contamination=Constantes.ContaminacionEllipticEnvelope)
    
        clf.fit(datosOriginales)
        pred_test = clf.predict(datosATestear)
        
        outliersList = list()
        inliersList = list()

    #   Iteramos los valores anadiendo inliers y outliers
        for i in np.arange(0,len(pred_test)):
            if pred_test[i] == -1:
                outliersList.append(datosATestear[i][1])
            else:
                inliersList.append(datosATestear[i][1])


        return outliersList, inliersList
        
    def showOutliersMedianteEnvolturaElipticaDadosDatos(self, matriz, anioTrainInicio, AnioTrainFin, AnioTest, labels, listaColumnas):
        
        datosOriginales, datosATestear = self.setDataValues(matriz, anioTrainInicio, AnioTrainFin, AnioTest, labels)
        
        graphics = Graphics()
#        print(listaColumnas)
        graphics.showOutliersInliers(datosOriginales, datosATestear, labels, listaColumnas)

