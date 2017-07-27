import connexion
from swagger_server.models.body import Body
from ..Utilidades.UtilidadesTensorFlow import UtilidadesTensorFlow as Tensorflow
tensorflow = Tensorflow()
from ..Utilidades.Conversores import Conversores 
conversor = Conversores()


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

