import numpy as np
from ..Utilidades.Graphics import Graphics as Graphics
from sklearn.covariance import EllipticEnvelope
from ..Utilidades.Constantes import Constantes
from sklearn.ensemble import IsolationForest
rng = np.random.RandomState(42)

import pandas as pd

class DeteccionOutliers:
    
    def setDataValues(self, matriz, anioTrainInicio, AnioTrainFin, AnioTest, labels):
        if 'Anio' in labels[0] and 'Cantidad' in labels[1]:
            numColumnas = 1
        if 'Anio' in label[0] and 'Mes' in label[1] and 'Cantidad' in label[2] #CONTINUAR
            serieDataAnios = self.joinArrayAnios(anioTrainInicio, AnioTrainFin, matriz, numColumnas )


            indices = np.arange(int(anioTrainInicio), int(AnioTrainFin)+1,1)
            
            datosOriginales = np.column_stack((indices, serieDataAnios))

            datosATestear = np.column_stack((AnioTest, matriz.loc[AnioTest]))
            return datosOriginales, datosATestear
        
        
        
        
    ##Llamar a este metodo
    def getOutliersMedianteEnvolturaElipticaDadaMatrizYAnios(self, matriz, anioTrainInicio, AnioTrainFin, AnioTest, listaLabels):
        datosOriginales, datosATestear = self.setDataValues(matriz, anioTrainInicio, AnioTrainFin, AnioTest, listaLabels)

        outliersValuesList, inliersValuesList =   self.ObtenerInliersOutliers(datosOriginales, datosATestear)
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

    def ObtenerInliersOutliers(self, datosOriginales, datosATestear):
        
        n_samples = len(datosOriginales)

#        maxValoresOriginales = np.amax(datosOriginales[:, 1])
#        maxValoresPrueba = np.amax(datosATestear[:,1])
#        maxValor = max(maxValoresOriginales, maxValoresPrueba)

#        xx, yy = np.meshgrid(np.linspace(listaColumnas[0]-1, listaColumnas[len(listaColumnas)-1]+1, len(listaColumnas)), 
#                                        np.linspace(-1, maxValor*2, len(listaColumnas)))

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

