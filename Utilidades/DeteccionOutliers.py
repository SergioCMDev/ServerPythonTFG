import numpy as np
from Utilidades.Graphics import Graphics as Graphics
from sklearn.covariance import EllipticEnvelope

from sklearn.svm import OneClassSVM
import matplotlib.pyplot as plt
import pandas as pd

class DeteccionOutliers:
    
    def setDataValues(self, matriz, anioTrainInicio, AnioTrainFin,AnioTest):
        serieDataAnios = self.joinArrayAnios(anioTrainInicio, AnioTrainFin, matriz )
       
        indices = np.arange(0,12,1)
        indices = np.tile(indices, AnioTrainFin - anioTrainInicio)
        datosOriginales = np.column_stack((indices, serieDataAnios))
        datosATestear = np.column_stack((np.arange(1,13,1), matriz.loc[AnioTest]))
        return datosOriginales, datosATestear
        
        
    def getOutliersMedianteEnvolturaElipticaDadaMatrizYAnios(self, matriz, anioTrainInicio, AnioTrainFin, AnioTest, tipo):
        datosOriginales, datosATestear = self.setDataValues(matriz, anioTrainInicio, AnioTrainFin, AnioTest)

        outliersValuesList, inliersValuesList =   self.getOutliersMedianteEnvolturaElipticaDadosDatos(datosOriginales, datosATestear, tipo)
        return outliersValuesList, inliersValuesList
        
    def joinArrayAnios(self, anioInicio, AnioFin, matriz):
        num_anios = AnioFin - anioInicio
        array_1 = np.zeros(num_anios * 12)

        anios = np.arange(anioInicio, AnioFin, 1)
        pos = 0
        
        for anio in anios:
            datos = matriz.loc[anio]
            for i in np.arange(0,12):
                array_1[pos] = datos[i]
                pos = pos +1
                
        s = pd.Series(array_1)
        s = s.astype(int)
        
        return s
        
    
    
    def getOutliersMedianteEnvolturaElipticaDadosDatos(self, datosOriginales, datosATestear, tipo):

        print("El tipo elegido es ", tipo)
        clf = EllipticEnvelope(contamination=0.26161)
    
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
        
    def showOutliersMedianteEnvolturaElipticaDadosDatos(self, matriz, anioTrainInicio, AnioTrainFin, AnioTest, tipo):
        
        datosOriginales, datosATestear = self.setDataValues(matriz, anioTrainInicio, AnioTrainFin, AnioTest)
        
        graphics = Graphics()
        
        graphics.showOutliersInliers(datosOriginales, datosATestear)

