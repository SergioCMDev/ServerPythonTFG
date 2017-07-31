import connexion
from swagger_server.models.body import Body
from swagger_server.models.body2 import Body2
from swagger_server.models.body13 import Body13

from ..Utilidades.UtilidadesTensorFlow import UtilidadesTensorFlow as Tensorflow
tensorflow = Tensorflow()
from ..Utilidades.Conversores import Conversores 
conversor = Conversores()
from ..Utilidades.DeteccionOutliers import DeteccionOutliers
outliers = DeteccionOutliers()


def obtener_outliers_inliers(AnioInicio, AnioFin, AnioAComprobar, body):
    """
    Obtener los valores fuera de lo comun dado unos valores iniciales y unos valores a tratar
    Obtener los valores fuera de lo comun dado unos valores iniciales y unos valores a tratar
    :param AnioInicio: Año inicial de la matriz de datos
    :type AnioInicio: str
    :param AnioFin: Año final de la matriz de datos
    :type AnioFin: str
    :param AnioAComprobar: Año a comprobar de la matriz de datos
    :type AnioAComprobar: str
    :param body: Datos de entrada obtenidos previamente
    :type body: list | bytes

    :rtype: Dict[str, int]
    """
    if connexion.request.is_json:
        body = [Body.from_dict(d) for d in connexion.request.get_json()]
        listaValores = list()
        listaLabels = list()
#        print(body)
        for item in body:
            if(hasattr(item, 'anio') and hasattr(item, 'cantidad')):

                tupla = (item.anio, item.cantidad)
                listaValores.append(tupla)
                if 'Anio' not in listaLabels and 'Cantidad' not in listaLabels:
                    
                    listaLabels.append('Anio')
                    listaLabels.append('Cantidad')


        matriz, listaColumnas =  conversor.ConvertirTuplasToMatriz(listaValores, listaLabels, AnioInicio, AnioFin )
#        outliers.showOutliersMedianteEnvolturaElipticaDadosDatos(matriz, AnioInicio, AnioFin, AnioAComprobar, listaLabels, listaColumnas)

        outliersValues, inliersValues = outliers.getOutliersMedianteEnvolturaElipticaDadaMatrizYAnios(matriz, AnioInicio, AnioFin, AnioAComprobar, listaLabels)

        if(len(inliersValues) > 0 and len(outliersValues) > 0):
            inliersJSON = conversor.convertirNumpyArrayAJson(inliersValues)
            outliersJSON = conversor.convertirNumpyArrayAJson(outliersValues)
            text = 'Outliers '+ str(outliersJSON) + ' Inliers ' + str(inliersJSON)
        elif(len(inliersValues) > 0 and len(outliersValues) == 0):
            inliersJSON = conversor.convertirNumpyArrayAJson(inliersValues)
            text = 'Inliers ' + str(inliersJSON)
        elif(len(inliersValues) == 0 and len(outliersValues > 0)):
            outliersJSON = conversor.convertirNumpyArrayAJson(outliersValues)
            text = " Outliers "+ str(outliersJSON)
        return text
#


def obtener_outliers_inliers_anios_mes_cantidad(AnioInicio, AnioFin, AnioAComprobar, body):
    """
    Obtener los valores fuera de lo comun dado unos valores iniciales y unos valores a tratar
    Este metodo trata los valores de cada mes de cada año y tras pasarle valores a probar decide los inliers y los outliers
    :param AnioInicio: Año inicial de la matriz de datos
    :type AnioInicio: int
    :param AnioFin: Año final de la matriz de datos
    :type AnioFin: int
    :param AnioAComprobar: Año a comprobar de la matriz de datos
    :type AnioAComprobar: int
    :param body: Datos de entrada obtenidos previamente junto con los datos a testear
    :type body: list | bytes

    :rtype: Dict[str, int]
    """

    if connexion.request.is_json:
        body = [Body13.from_dict(d) for d in connexion.request.get_json()]
        listaValores = list()
        listaLabels = list()
        for item in body:
            if(hasattr(item, 'anio') and hasattr(item, 'mes') and hasattr(item, 'numero_vuelos')):
                if 'Anio' not in listaLabels and 'Cantidad' not in listaLabels:
                    listaLabels.append('Anio')
                    listaLabels.append('Mes')
                    listaLabels.append('Numero_Vuelos')
                tupla = (item.anio, item.mes, item.numero_vuelos)
                listaValores.append(tupla)
                
        matriz, listaColumnas =  conversor.ConvertirTuplasToMatriz(listaValores, listaLabels, AnioInicio, AnioFin )

        outliersValuesElliptic, inliersValuesElliptic = outliers.getOutliersDadaMatrizAniosYTipo(matriz, AnioInicio, AnioFin, AnioAComprobar, listaLabels, "Elliptic")
        outliersValuesForest, inliersValuesForest = outliers.getOutliersDadaMatrizAniosYTipo(matriz, AnioInicio, AnioFin, AnioAComprobar, listaLabels, "Forest")
        print('Eliptic')

        print(outliersValuesElliptic)
        print(inliersValuesElliptic)
        print('FOREST')

        print(outliersValuesForest)
        print(inliersValuesForest)
        #TODO REALIZAR AMBAS GRAFICAS
        outliers.showOutliersMedianteEnvolturaElipticaDadosDatos(matriz, AnioInicio, AnioFin, AnioAComprobar, listaLabels, listaColumnas)
        outliers.showOutliersMedianteIsolationForestDadosDatos(matriz, AnioInicio, AnioFin, AnioAComprobar, listaLabels, listaColumnas)

    return 'do some magic!'



"""
    Probar en postman con entrada [{"Anio": 2009,"Cantidad": 46453}, {"Anio": 2010,"Cantidad": 44721}, {"Anio": 2011,"Cantidad": 61420}]
"""
def obtener_progresion_lineal(AnioPrediccion, body):

#def obtener_progresion_lineal_anio_cantidad(AnioPrediccion, body):
    """
    Obtener la prediccion para un año dado el año a predecir y los datos de varios años anteriores
    Obtener la prediccion para un año dado el año a predecir y los datos de varios años anteriores
    :param AnioPrediccion: Año para predecir la cantidad
    :type AnioPrediccion: str
    :param body: Datos de entrada obtenidos previamente
    :type body: list | bytes

    :rtype: int
    """
    prediccionCantidad = -1
    if connexion.request.is_json:
        body = [Body.from_dict(d) for d in connexion.request.get_json()]
        lista = list()
        
        print(body)
        for item in body:
            if(hasattr(item, 'Anio') and hasattr(item, 'Cantidad')):
                tupla = (item.Anio, item.Cantidad)
            elif (hasattr(item, 'Anio') and hasattr(item, 'Numero_Turistas')):
                tupla = (item.Anio, item.Numero_Turistas)
            elif (hasattr(item, 'Anio') and hasattr(item, 'Numero_Vuelos')):
                tupla = (item.Anio, item.Numero_Vuelos)
            else:
                tupla = None
            lista.append(tupla)

        prediccionCantidad = tensorflow.ObtenerProgresionLineal(lista, int(AnioPrediccion))

    return int(prediccionCantidad)

