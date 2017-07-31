import numpy as np
from ..Utilidades.Graphics import Graphics as Graphics
from sklearn.covariance import EllipticEnvelope
from ..Utilidades.Constantes import Constantes
from sklearn.ensemble import IsolationForest
rng = np.random.RandomState(42)

import pandas as pd

class DeteccionOutliers:
    
    ##Llamar a este metodo
    def getOutliersDadaMatrizAniosYTipo(self, matriz, anioTrainInicio, AnioTrainFin, AnioTest, listaLabels, tipo):
        datosOriginales, datosATestear = self.setDataValues(matriz, anioTrainInicio, AnioTrainFin, AnioTest, listaLabels)
        if tipo == "Elliptic":
            outliersValuesList, inliersValuesList =   self.GetOutliersInliersEllipticEnvelope(datosOriginales, datosATestear)
        elif tipo == "Forest":
            outliersValuesList, inliersValuesList =   self.ObtenerInliersOutliersIsolationForest(datosOriginales, datosATestear)

        return outliersValuesList, inliersValuesList
    
    
    
    
    
    def setDataValues(self, matriz, anioTrainInicio, AnioTrainFin, AnioTest, labels):
        if 'Anio' in labels[0] and 'Cantidad' in labels[1]:
            numColumnas = 1
            serieDataAnios = self.joinArrayAnios(anioTrainInicio, AnioTrainFin, matriz, numColumnas )

            indices = np.arange(int(anioTrainInicio), int(AnioTrainFin)+1,1)
            
            datosOriginales = np.column_stack((indices, serieDataAnios))

            datosATestear = np.column_stack((AnioTest, matriz.loc[AnioTest]))
 

            return datosOriginales, datosATestear
        elif 'Anio' in labels[0] and 'Mes' in labels[1] and 'Cantidad' in labels[2] or 'Numero_Vuelos' in labels[2]: #CONTINUAR
            numColumnas = 12 #Debido a que son 12 meses
            serieDataAnios = self.joinArrayAnios(anioTrainInicio, AnioTrainFin, matriz, numColumnas )
            indices = np.arange(0, numColumnas,1)
            indices = np.tile(indices, AnioTrainFin - anioTrainInicio +1)


            datosOriginales = np.column_stack((indices, serieDataAnios))
            datosATestear = np.column_stack((np.arange(0,numColumnas,1), matriz.loc[AnioTest]))

            return datosOriginales, datosATestear
        
    def showOutliersMedianteEnvolturaElipticaDadosDatos(self, matriz, anioTrainInicio, AnioTrainFin, AnioTest, listaFilas, listaColumnas):
        
        datosOriginales, datosATestear = self.setDataValues(matriz, anioTrainInicio, AnioTrainFin, AnioTest, listaFilas)
        
       
        graphics = Graphics()
        graphics.showOutliersInliers(datosOriginales, datosATestear, listaFilas, listaColumnas)

        
    
    
    def joinArrayAnios(self, anioInicio, AnioFin, matriz, numColumnas):
        num_anios = AnioFin - anioInicio +1
        array_1 = np.zeros(num_anios * numColumnas)

        anios = np.arange(anioInicio, AnioFin+1, 1)
        pos = 0
        
        for anio in anios:
            datos = matriz.loc[anio]
            for i in np.arange(0, numColumnas):
                array_1[pos] = datos[i]
                pos = pos +1
                
        s = pd.Series(array_1)
        s = s.astype(int)
        
        return s


    def GetOutliersInliersEllipticEnvelope(self, datosOriginales, datosATestear):

        clf = EllipticEnvelope(contamination=Constantes.ContaminacionEllipticEnvelope)
        clf.fit(datosOriginales)
        pred_test = clf.predict(datosATestear)


        listaInliers = list()
        listaOutliers = list()

    #   Iteramos los valores marcando en rojo los elementos que sean outliers y en verde los inliners
        for i in np.arange(0,len(pred_test)):
            if pred_test[i] == -1:
                listaOutliers.append(datosATestear[i])
            else:
                listaInliers.append(datosATestear[i])

        return listaOutliers, listaInliers


    def ObtenerInliersOutliersIsolationForest(self, datosOriginales, datosATestear):
        
        n_samples = len(datosOriginales)

        np.random.seed(42)

        # Fit the model
        clf = IsolationForest(max_samples=n_samples, random_state=rng)
        clf.fit(datosOriginales)
        y_pred_test = clf.predict(datosATestear)
#        Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
#        Z = Z.reshape(xx.shape)
#        plt.contourf(xx, yy, Z, cmap=plt.cm.Blues_r)
        outliers = list()
        inliers = list()
#        valores_originales = plt.scatter(datosOriginales[:, 0], datosOriginales[:, 1], color='black', label='Valores Originales')

        #   Iteramos los valores marcando en rojo los elementos que sean outliers y en verde los inliners
        for i in np.arange(0, len(y_pred_test)):
            if y_pred_test[i] == -1:
                outliers.append(datosATestear[i])
            else:
                inliers.append(datosATestear[i])
#                print(inliers)
    
        return outliers, inliers








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
        
    
    
#    def getOutliersMedianteEnvolturaElipticaDadosDatos(self, datosOriginales, datosATestear):
#
##        print("El tipo elegido es ", tipo)
#        clf = EllipticEnvelope(contamination=Constantes.ContaminacionEllipticEnvelope)
#    
#        clf.fit(datosOriginales)
#        pred_test = clf.predict(datosATestear)
#        
#        outliersList = list()
#        inliersList = list()
#
#    #   Iteramos los valores anadiendo inliers y outliers
#        for i in np.arange(0,len(pred_test)):
#            if pred_test[i] == -1:
#                outliersList.append(datosATestear[i][1])
#            else:
#                inliersList.append(datosATestear[i][1])
#
#
#        return outliersList, inliersList
        


