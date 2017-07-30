import pylab
from ..Utilidades.Constantes import Constantes
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sklearn.covariance import EllipticEnvelope, EmpiricalCovariance, MinCovDet
from scipy import stats
from sklearn import svm
from sklearn.ensemble import IsolationForest
rng = np.random.RandomState(42)

class Graphics():
    def __init__(self):
        print("Clase Graphics Cargada Correctamente")


    def obtenerValoresLista(self, valores):
        listaFilas = list()
        for valor in valores:
                if (valor not in listaFilas):
                   listaFilas.append(valor)
        return listaFilas

    def showOutliersInliers(self, datosOriginales, datosATestear, labels, listaColumnas):
        print (1)
#        self.testMethod(datosOriginales, datosATestear, labels, listaColumnas)
#        max_Y = np.amax(datosOriginales)
#        print(datosOriginales)

        #   Obtenemos las fronteras de datos basandonos en los datos originales

#        xx1, yy1 = np.meshgrid(np.linspace(listaColumnas[0]-1, listaColumnas[len(listaColumnas)-1]+1, 500), np.linspace(-1, max_Y*2, 500)) #Seteamos a 13 debido a los meses        
#        clf = EllipticEnvelope(contamination=Constantes.ContaminacionEllipticEnvelope)
#        clf.fit(datosOriginales)
#        Z1 = clf.decision_function(np.c_[xx1.ravel(), yy1.ravel()])
#        Z1 = Z1.reshape(xx1.shape)
#        plt.contour(xx1, yy1, Z1, levels=[0], linewidths=1, colors='m')
#        pred_test = clf.predict(datosATestear)
#        plt.figure(1)  # two clusters
#        plt.title("Deteccion de Outliers")
#        
#        valores_originales = plt.scatter(datosOriginales[:, 0], datosOriginales[:, 1], color='black', label='Valores Originales')
#        inliers = plt.scatter(-2, -2)
##        print(pred_test)
#        #   Iteramos los valores marcando en rojo los elementos que sean outliers y en verde los inliners
#        for i in np.arange(0,len(pred_test)):
#            if pred_test[i] == -1:
#                color = 'red'
#                outliers = plt.scatter(datosATestear[i, 0], datosATestear[i, 1], color=color, label='Outliers')
#            else:
#                color = 'green'
#                inliers = plt.scatter(datosATestear[i, 0], datosATestear[i, 1], color=color, label='Inliners')
#        #   Definimos valores de la grafica
#        plt.xlim(listaColumnas[0]-1, listaColumnas[len(listaColumnas)-1]+1)
#        plt.ylim((yy1.min(), yy1.max()))
#        
#        plt.ylabel("Valores")
#        plt.xlabel(labels[0])
#        plt.legend(handles=[valores_originales, outliers, inliers])
#        
#        plt.show()
#        plt.savefig('grafica.png')     
        
        
   
        
        
    def MostrarGraficaInliersOutliers(self, datosOriginales, datosATestear, labels, listaColumnas):

        n_samples = len(datosOriginales)

        maxValoresOriginales = np.amax(datosOriginales[:, 1])
        maxValoresPrueba = np.amax(datosATestear[:,1])
        maxValor = max(maxValoresOriginales, maxValoresPrueba)

        xx, yy = np.meshgrid(np.linspace(listaColumnas[0]-1, listaColumnas[len(listaColumnas)-1]+1, len(listaColumnas)), 
                                        np.linspace(-1, maxValor*2, len(listaColumnas)))

        np.random.seed(42)

        # Fit the model
        clf = IsolationForest(max_samples=n_samples, random_state=rng)
        clf.fit(datosOriginales)
        y_pred_test = clf.predict(datosATestear)
        Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
        Z = Z.reshape(xx.shape)
        plt.contourf(xx, yy, Z, cmap=plt.cm.Blues_r)
        outliers = plt.scatter(-13, -13)
        inliers = plt.scatter(-13, -13)
        valores_originales = plt.scatter(datosOriginales[:, 0], datosOriginales[:, 1], color='black', label='Valores Originales')

        #   Iteramos los valores marcando en rojo los elementos que sean outliers y en verde los inliners
        for i in np.arange(0, len(y_pred_test)):
            if y_pred_test[i] == -1:
                color = 'red'
                outliers = plt.scatter(datosATestear[i, 0], datosATestear[i, 1], color=color, label='Outliers')
            else:
                color = 'green'
                inliers = plt.scatter(datosATestear[i, 0], datosATestear[i, 1], color=color, label='Inliners')
    #   Definimos valores de la grafica
        plt.xlim((xx.min(), xx.max()))
        plt.ylim((yy.min(), yy.max()))
        plt.savefig('grafica.png')
        plt.legend(handles=[valores_originales, outliers, inliers])


    #NO TOCAR
#    def showOutliersInliers(self, datosOriginales, datosATestear):
#        max_Y = np.amax(datosOriginales)
#
#
#    #   Obtenemos las fronteras de datos basandonos en los datos originales
#        xx1, yy1 = np.meshgrid(np.linspace(-1, 13, 500), np.linspace(-1, max_Y*2, 500)) #Seteamos a 13 debido a los meses        
#        clf = EllipticEnvelope(contamination=0.26161)
#        clf.fit(datosOriginales)
#        Z1 = clf.decision_function(np.c_[xx1.ravel(), yy1.ravel()])
#        Z1 = Z1.reshape(xx1.shape)
#        plt.contour(xx1, yy1, Z1, levels=[0], linewidths=1, colors='m')
#        pred_test = clf.predict(datosATestear)
#        plt.figure(1)  # two clusters
#        plt.title("Deteccion de Outliers")
#        valores_originales = plt.scatter(datosOriginales[:, 0], datosOriginales[:, 1], color='black', label='Valores Originales')
#        inliers = plt.scatter(-1, -1)
#        
#    #   Iteramos los valores marcando en rojo los elementos que sean outliers y en verde los inliners
#        for i in np.arange(0,len(pred_test)):
#            if pred_test[i] == -1:
#                color = 'red'
#                outliers = plt.scatter(datosATestear[i, 0], datosATestear[i, 1], color=color, label='Outliers')
#            else:
#                color = 'green'
#                inliers = plt.scatter(datosATestear[i, 0], datosATestear[i, 1], color=color, label='Inliners')
#    #   Definimos valores de la grafica
#        plt.xlim((xx1.min(), xx1.max()))
#        plt.ylim((yy1.min(), yy1.max()))
#    
#        plt.ylabel("Valores")
#        plt.xlabel("Meses")
#        plt.legend(handles=[valores_originales, outliers, inliers])
#    
#        plt.show()
#        savefig('grafica.png')


    def get_cmap(self, n, name='hsv'):
        '''Returns a function that maps each index in 0, 1, ..., n-1 to a distinct 
        RGB color; the keyword argument name must be a standard mpl colormap name.'''
        return plt.cm.get_cmap(name, n)
    
    

        
    def obtenerValoresMatrizLista(self, labels, matriz, posicion):
#        posicion = 1
        valores = list()
        if labels[posicion] == 'Mes': #OK
            valores = Constantes.Meses
        elif labels[posicion] == 'Ciudad': #OK
            valores = matriz.Ciudad
        elif labels[posicion] == 'Cantidad': #OK
            valores = matriz.Cantidad
        elif labels[posicion] == 'Numero_Vuelos': #OK
            valores = matriz.Numero_Vuelos
        elif labels[posicion] == 'Numero_Turistas': #OK
            valores = matriz.Numero_Turistas
        elif labels[posicion] == 'Anio': #OK
            valores = matriz.Anio    
        elif labels[posicion] == 'Pais_Origen':
            valores = matriz.Pais_Origen
        elif labels[posicion] == 'Ciudad_Origen':
            valores = matriz.Ciudad_Origen
        elif labels[posicion] == 'Ciudad_Destino':
            valores = matriz.Ciudad_Destino
        if labels[posicion] == 'Anio':
            valores = matriz.Anio

            
        return valores
    
    #Metodo Generico para dibujar Graficas
    def dibujarGraficaLineal(self, valoresX, valoresY):
        pylab.figure(1)
        pylab.figure( figsize=(12.0, 6.0))   
        x = np.arange(0, len(valoresX))

        coloresMapped = self.get_cmap(len(valoresX))
        for item in np.arange(0, len(valoresX)):
            valorX =  valoresX[item]
            pylab.scatter(item, valoresY.loc[valorX], color=coloresMapped(item), label = valorX)
#            pylab.plot(item, valoresY.loc[valorX], color=coloresMapped(item), label = valorX)

        pylab.xticks(x, valoresX)
        
        pylab.legend(loc='upper right')
        pylab.savefig("grafica.png")
        pylab.show()
        
    
    #Metodo Generico para dibujar Graficas durante varios anios
    def dibujarGraficaLinealSuperpuesta(self, listaFilas, matriz):
        pylab.figure(1)
        pylab.figure( figsize=(12.0, 6.0)) 
        index = 0
        listaColumnas =  matriz.columns
        for item in listaFilas:
            valores =  matriz.loc[item]
            coloresMapped = self.get_cmap(len(valores))
            x = np.arange(0, len(valores))
            pylab.scatter(x, valores, color=coloresMapped(index), label = item)
            index = index +1
        
            pylab.xticks(x, listaColumnas)

        pylab.legend(loc='upper right')
#        savefig("grafica.png")
        pylab.show()


    #Metodo Inicial de la clase
    def obtenerValoresParaDibujarGrafica(self, matriz, lista, labels):
       
        numeroColumnas = len(labels)

        if numeroColumnas == 2:
            valoresX = matriz.index
            valoresY = self.obtenerValoresMatrizLista(labels, matriz, 1)
            self.dibujarGraficaLineal(valoresX, valoresY)
            
        if numeroColumnas == 3:
            if labels[0] == 'Anio':
                if len(matriz.index) == 1:
                    valoresX = matriz.columns
                    valoresY = matriz.loc[matriz.index[0]]  
                    self.dibujarGraficaLineal(valoresX, valoresY)
                else:
                    self.dibujarGraficaLinealSuperpuesta(lista, matriz)

 
