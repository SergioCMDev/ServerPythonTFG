import pylab
from ..Utilidades.Constantes import Constantes
from ..Utilidades.UtilidadesMatriz import UtilidadesMatriz
utilidadesMatriz = UtilidadesMatriz()
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

    #Metodo Inicial de la clase
    def obtenerValoresParaDibujarGrafica(self, matriz, lista, labels):
       
        numeroColumnas = len(labels)

        if numeroColumnas == 2:
            valoresX = matriz.index
            valoresY = utilidadesMatriz.ObtenerParametros(labels, matriz, 1)
            self.dibujarGraficaLineal(valoresX, valoresY)
            
        if numeroColumnas == 3:
            if labels[0] == 'Anio':
                if len(matriz.index) == 1:
                    valoresX = matriz.columns
                    valoresY = matriz.loc[matriz.index[0]]  
                    self.dibujarGraficaLineal(valoresX, valoresY)
                else:
                    self.dibujarGraficaLinealSuperpuesta(lista, matriz)

   
    
      #Metodo privado 
      #listaColumnas: Valores para el eje x
    #Inicializa divesos parametros comunes a los diversos tipos de grafica de outliers que se usan para dibujar las graficas
    def inicializarDatosGrafica(self, listaFilas, listaColumnas, datosOriginales):
        valoresColumnas = list()
        textoInferior = ""
        max_Y = np.amax(datosOriginales)
        #TODO
        if 'Mes'in listaFilas[0] or 'Pais' in listaFilas[0] and 'Cantidad' in listaFilas[1]:
            valoresColumnas = listaColumnas
            x = np.arange(0, len(listaColumnas))
            xx1, yy1 = np.meshgrid(np.linspace(-2, len(listaColumnas), len(listaColumnas) ), np.linspace(-10, max_Y*2, len(listaFilas)))       
            textoInferior = listaFilas[0]
        
        elif 'Anio' in listaFilas[0] and 'Cantidad' in listaFilas[1]:
            valoresColumnas = listaColumnas
            x = valoresColumnas
            xx1, yy1 = np.meshgrid(np.linspace(listaColumnas[0]-1, listaColumnas[len(listaColumnas)-1]+1, len(listaColumnas)), np.linspace(-500, max_Y*2, len(listaFilas)))       
            textoInferior = listaFilas[0]
        elif 'Ciudad' in listaFilas[0] and 'Cantidad' in listaFilas[1]:
            valoresColumnas = listaColumnas
            x = np.arange(0, len(listaColumnas)-1)
            xx1, yy1 = np.meshgrid(np.linspace(-2, len(listaColumnas), len(listaColumnas)), np.linspace(-500, max_Y*2, len(listaFilas)))       
            textoInferior = listaFilas[0]    
        elif 'Pais' in listaFilas[0] and 'Cantidad' in listaFilas[1]:
            valoresColumnas = listaColumnas
            x = np.arange(0, len(listaColumnas))
            xx1, yy1 = np.meshgrid(np.linspace(-2, len(listaColumnas), len(listaColumnas)), np.linspace(-500, max_Y*2, len(listaFilas)))       
            textoInferior = listaFilas[0]   

        elif 'Anio' in listaFilas[0] and 'Mes' in listaFilas[1] or 'Ciudad' in listaFilas[1] and 'Cantidad' in listaFilas[2] or 'Numero_Vuelos' in listaFilas[2]:
            if 'Mes' in listaFilas[1]:
                x = np.arange(0, len(Constantes.Meses))
                valoresColumnas = Constantes.Meses
            else: #Para ciudades/paises
                x = np.arange(0, len(listaColumnas))
                valoresColumnas = listaColumnas
            xx1, yy1 = np.meshgrid(np.linspace(-1, len(x), 500), np.linspace(500, max_Y*2, 500)) 
            textoInferior = listaFilas[1]
        return valoresColumnas, textoInferior, xx1, yy1, x
    
    
    #CON MESES OK
    #CON AÑOS OK
    #CON CIUDAD OK
    #TODO PAISES
    #Metodo para obtener los outliers durante varios años separado por meses
    ##listaFilas Lista Anios
    #ListaColumnas lista Meses


    def showOutliersInliersEllipticEnvelope(self, datosOriginales, datosATestear, listaFilas, listaColumnas):

        valoresColumnas, textoInferior, xx1, yy1, x = self.inicializarDatosGrafica(listaFilas, listaColumnas, datosOriginales)
    #   Obtenemos las fronteras de datos basandonos en los datos originales
        clf = EllipticEnvelope(contamination=Constantes.ContaminacionEllipticEnvelope)
        
        #Llamamos al metodo para dibujar la grafica
        self.dibujarGraficaOutliersInliers(clf, datosOriginales, datosATestear, xx1, yy1, x , valoresColumnas, textoInferior, "Elliptic")
           
  
    
    
    def dibujarGraficaOutliersInliers(self, clf, datosOriginales, datosATestear, xx1, yy1, x , valoresColumnas, textoInferior, tipo):
        clf.fit(datosOriginales)
        Z = clf.decision_function(np.c_[xx1.ravel(), yy1.ravel()])
        Z = Z.reshape(xx1.shape)
        resultadoValoresATestear = clf.predict(datosATestear)
        plt.figure(1)  # two clusters
#        plt.title("Deteccion de Outliers")
        if tipo == "Elliptic":
            plt.title("Deteccion de Outliers Metodo Elliptic Envelope")
            plt.contour(xx1, yy1, Z, levels=[0], linewidths=1, colors='m')
        else:
            plt.title("Deteccion de Outliers Metodo Isolation Forest")
            plt.contourf(xx1, yy1, Z, cmap=plt.cm.Blues_r)
            
        outliers = plt.scatter(-13, -13)
        inliers = plt.scatter(-13, -13)
        valores_originales = plt.scatter(datosOriginales[:, 0], datosOriginales[:, 1], color='black', label='Valores Originales')

        #   Iteramos los valores marcando en rojo los elementos que sean outliers y en verde los inliners
        for i in np.arange(0, len(resultadoValoresATestear)):
            if resultadoValoresATestear[i] == -1:
                color = 'red'
                outliers = plt.scatter(datosATestear[i, 0], datosATestear[i, 1], color=color, label='Outliers')
            else:
                color = 'green'
                inliers = plt.scatter(datosATestear[i, 0], datosATestear[i, 1], color=color, label='Inliners')
                
    #   Definimos valores de la grafica
        plt.xlim((xx1.min(), xx1.max()))
        plt.ylim((yy1.min(), yy1.max()))
        print(valoresColumnas)
        print(x)
        pylab.xticks(x, valoresColumnas, size='small', rotation='vertical')
#        plt.savefig('grafica.png')
        plt.ylabel("Cantidad")
        plt.xlabel(textoInferior)
        plt.legend(handles=[valores_originales, outliers, inliers])
        plt.show()
        
        
 
        
        
        
        
        
        
        
        
        
        
        
        
    
   #CON MESES OK
   #CON AÑOS OK
    #NO TOCAR
    #Metodo para obtenerla grafica de outliers/inliers durante varios años
    def MostrarGraficaInliersOutliersIsolationForest(self, datosOriginales, datosATestear, listaFilas, listaColumnas):

        valoresColumnas, textoInferior, xx1, yy1, x = self.inicializarDatosGrafica(listaFilas, listaColumnas, datosOriginales)
        
        # Fit the model
        n_samples = len(datosOriginales)
        clf = IsolationForest(max_samples=n_samples, random_state=rng)
        
        #Llamamos al metodo para dibujar la grafica
        self.dibujarGraficaOutliersInliers(clf, datosOriginales, datosATestear, xx1, yy1, x , valoresColumnas, textoInferior, "Forest")
#


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
#        plt.savefig('grafica.png')

    #Metodo para obtener colores aleatorios sin repeticion
    def get_cmap(self, n, name='hsv'):
        '''Returns a function that maps each index in 0, 1, ..., n-1 to a distinct 
        RGB color; the keyword argument name must be a standard mpl colormap name.'''
        return plt.cm.get_cmap(name, n)
    
        
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




 
