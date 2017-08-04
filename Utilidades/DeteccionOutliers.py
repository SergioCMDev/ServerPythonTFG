import numpy as np
from ..Utilidades.Graphics import Graphics as Graphics
from sklearn.covariance import EllipticEnvelope
from ..Utilidades.Constantes import Constantes
from sklearn.ensemble import IsolationForest
rng = np.random.RandomState(42)
graphics = Graphics()
from ..Utilidades.UtilidadesMatriz import UtilidadesMatriz
utilidadesMatriz = UtilidadesMatriz()
import pandas as pd
from sklearn.covariance import EmpiricalCovariance, MinCovDet

class DeteccionOutliers:
    
    ##Llamar a este metodo
#    def ObtenerOutliersDadaMatrizAniosYTipo(self, matriz, anioTrainInicio, AnioTrainFin, AnioTest, listaLabels, Metodo):
    def ObtenerOutliersDadaMatrizAniosYTipo(self, matriz, DatoTrainInicio, DatoTrainFin, ValoresTest, listaLabels, Metodo):

        datosOriginales, datosATestear = self.setDataValues(matriz, DatoTrainInicio, DatoTrainFin, ValoresTest, listaLabels)
        
        
        print(datosOriginales)
        print("\n")
        print(datosATestear)
        
        
        if Metodo == "Elliptic":
            outliersValuesList, inliersValuesList =   self.obtenerOutliersInliersEllipticEnvelope(datosOriginales, datosATestear)
        elif Metodo == "Forest":
            outliersValuesList, inliersValuesList =   self.obtenerInliersOutliersIsolationForest(datosOriginales, datosATestear)
        elif Metodo == "Covarianza":
            outliersValuesList, inliersValuesList =   self.obtenerOutliersMinCovarianza(datosOriginales, datosATestear)

        return outliersValuesList, inliersValuesList
    
    
    
    
    #Metodo Privado
    #Inicalizacion datos para obtener outliers e inliers, otenemos valores originales y valores a testear
#    def setDataValues(self, matriz, anioTrainInicio, AnioTrainFin, AnioTest, labels):
    def setDataValues(self, matriz, DatoTrainInicio, DatoTrainFin, ValoresTest, labels):

        
        print(labels)
        if 'Anio' in labels[0] and 'Pais' in labels[1] and 'Cantidad' in labels[2]:
            print(matriz)
            print(labels)
            numColumnas = 1
            valoresDatosIniciales = utilidadesMatriz.GetValuesArrayIntegers(DatoTrainInicio, DatoTrainFin, matriz, numColumnas ) 

            
        elif  'Anio' in labels[0] or 'Mes' in labels[0] and 'Cantidad' in labels[1]:
            numColumnas = 1
            valoresDatosIniciales = utilidadesMatriz.GetValuesArrayIntegers(DatoTrainInicio, DatoTrainFin, matriz, numColumnas ) 
            if 'Mes' in labels[0]:
                indices = np.arange(0, len(valoresDatosIniciales), 1)
                print(indices)
            else:
                indices = np.arange(int(DatoTrainInicio), int(DatoTrainFin)+1, 1)
            
            datosOriginales = np.column_stack((indices, valoresDatosIniciales))
            
            if len(ValoresTest) == 1: #Un solo Año ####PROBAR PARA HACERLO DE UNA SOLO FORMA USANDO EL ELSE
                valorInicioTest = ValoresTest[0]
                datosATestear = np.column_stack((valorInicioTest, matriz.loc[valorInicioTest]))
            else: #Una lista de años
                if 'Mes' in labels[0]:
                    DatoTestInicio = ValoresTest[0]
                    DatoTestFin = ValoresTest[len(ValoresTest)-1]
                    indices = np.arange(len(valoresDatosIniciales), len(valoresDatosIniciales) + len(ValoresTest) , 1)

                else:
                    DatoTestInicio = int(ValoresTest[0])
                    DatoTestFin = int(ValoresTest[len(ValoresTest)-1])
                    indices = np.arange(int(DatoTestInicio), int(DatoTestFin)+1, 1)
                
                serieDataTestingAnios = utilidadesMatriz.GetValuesArrayIntegers(DatoTestInicio, DatoTestFin, matriz, numColumnas )
                datosATestear = np.column_stack((indices, serieDataTestingAnios))


                
            return datosOriginales, datosATestear

        elif 'Ciudad' in labels[0] or 'Pais' in labels[0] and 'Cantidad' in labels[1]:
            numColumnas = 1           
            valoresDatosIniciales = utilidadesMatriz.GetValuesArrayStrings(DatoTrainInicio, DatoTrainFin, matriz, numColumnas)
#            print(matriz.loc[DatoTrainInicio : DatoTrainFin]["Cantidad"])
            indices = np.arange(0, len(valoresDatosIniciales), 1)

            datosOriginales = np.column_stack((indices, valoresDatosIniciales))

            if len(ValoresTest) == 1: #Un solo valor de testeo
                ciudadTest = ValoresTest[0]
                datosATestear = np.column_stack((len(valoresDatosIniciales), matriz.loc[ciudadTest]))
#    
            else: #Una lista de valores de testeo
                DatoTestInicio = ValoresTest[0]
                DatoTestFin = ValoresTest[len(ValoresTest)-1]

                indices = np.arange(len(valoresDatosIniciales), len(valoresDatosIniciales) + len(ValoresTest), 1)
                print(indices)
                serieDataTestingAnios = utilidadesMatriz.GetValuesArrayStrings(DatoTestInicio, DatoTestFin, matriz, numColumnas )

                datosATestear = np.column_stack((indices, serieDataTestingAnios))
            
            return datosOriginales, datosATestear

# TODO
#        elif 'Anio' in labels[0] and 'Mes' in labels[1]  and 'Cantidad' in labels[2] or 'Numero_Vuelos' in labels[2]: 
#            if 'Mes' in labels[1]:
#                numColumnas = 12 #Debido a que son 12 meses
#            else:
#                numColumnas = 21
#                
#            serieDataAnios = utilidadesMatriz.GetValuesArrayIntegers(anioTrainInicio, AnioTrainFin, matriz, numColumnas )
#            indices = np.arange(0, numColumnas,1)
#            indices = np.tile(indices, AnioTrainFin - anioTrainInicio +1)
#
#
#            datosOriginales = np.column_stack((indices, serieDataAnios))
#            datosATestear = np.column_stack((np.arange(0,numColumnas,1), matriz.loc[AnioTest]))
#
#            return datosOriginales, datosATestear
#        
        
        
        

    def MostrarOutliersMedianteEnvolturaElipticaDadosDatos(self, matriz, DatoTrainInicio, DatoTrainFin, ValoresTest, listaFilas, listaColumnas):
        
        datosOriginales, datosATestear = self.setDataValues(matriz, DatoTrainInicio, DatoTrainFin, ValoresTest, listaFilas)
        
        graphics.showOutliersInliersEllipticEnvelope(datosOriginales, datosATestear, listaFilas, listaColumnas)



    def MostrarOutliersMedianteIsolationForestDadosDatos(self, matriz, DatoTrainInicio, DatoTrainFin, ValoresTest, listaFilas, listaColumnas):
        
        datosOriginales, datosATestear = self.setDataValues(matriz, DatoTrainInicio, DatoTrainFin, ValoresTest, listaFilas)
        
        graphics.MostrarGraficaInliersOutliersIsolationForest(datosOriginales, datosATestear, listaFilas, listaColumnas)

    
    def obtenerOutliersMinCovarianza(self, datosOriginales, datosATestear):
        clf = MinCovDet().fit(datosOriginales)
        resultadoValoresATestear = clf.predict(datosATestear)
        
        listaOutliers, listaInliers = self.getListasOutliersInliers(resultadoValoresATestear, datosATestear)
        return listaOutliers, listaInliers


    #Metodo Privado
    #Genera el modelo Elliptic Envelope, prueba los datos enviados y devuelve las listas de outliers y inliers
    def obtenerOutliersInliersEllipticEnvelope(self, datosOriginales, datosATestear):

        # Fit the model
        clf = EllipticEnvelope(contamination=Constantes.ContaminacionEllipticEnvelope)
        clf.fit(datosOriginales)
        resultadoValoresATestear = clf.predict(datosATestear)
        
        listaOutliers, listaInliers = self.getListasOutliersInliers(resultadoValoresATestear, datosATestear)
        return listaOutliers, listaInliers
    
    #Metodo Privado
    #Genera el modelo Isolation Forest, prueba los datos enviados y devuelve las listas de outliers y inliers
    def obtenerInliersOutliersIsolationForest(self, datosOriginales, datosATestear):
        
        n_samples = len(datosOriginales)
        np.random.seed(42)
        
        # Fit the model
        clf = IsolationForest(max_samples=n_samples, random_state=rng)
        clf.fit(datosOriginales)
        resultadoValoresATestear = clf.predict(datosATestear)


        #Obtenemos las listas de outliers e inliers y las devolvemos
        listaOutliers, listaInliers = self.getListasOutliersInliers(resultadoValoresATestear, datosATestear)
        return listaOutliers, listaInliers

    #Metodo Privado
    #Obtiene las listas de inliers y outliers
    def getListasOutliersInliers(self, resultadoValoresATestear, datosATestear):
        listaInliers = list()
        listaOutliers = list()
        #   Iteramos los valores almacenando los outliers y los inliers
        for i in np.arange(0, len(resultadoValoresATestear)):
            if resultadoValoresATestear[i] == -1:
                listaOutliers.append(datosATestear[i])
            else:
                listaInliers.append(datosATestear[i])
   
        return listaOutliers, listaInliers




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
        


