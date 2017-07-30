import connexion
from swagger_server.models.body import Body
from ..Utilidades.UtilidadesTensorFlow import UtilidadesTensorFlow as Tensorflow
tensorflow = Tensorflow()
from ..Utilidades.Conversores import Conversores 
conversor = Conversores()
from ..Utilidades.DeteccionOutliers import DeteccionOutliers
outliers = DeteccionOutliers()
import json

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


        matriz, listaColumnas =  conversor.ConvertirTuplasToMatriz(listaValores, listaLabels, AnioFin, AnioFin )
#        print(lista)
#        outliers.showOutliersMedianteEnvolturaElipticaDadosDatos(matriz, AnioInicio, AnioFin, AnioAComprobar, listaLabels, listaColumnas)

        outlierse, inliers = outliers.getOutliersMedianteEnvolturaElipticaDadaMatrizYAnios(matriz, AnioInicio, AnioFin, AnioAComprobar, listaLabels)
#        print(outlierse.toList())
        print(outlierse[0])
#        print(inliers)
#        return conversor.convertirAJson(outlierse)
        return 6






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

