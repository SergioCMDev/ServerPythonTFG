import connexion
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
from ..DB.DBRepositoryAena import DBRepositoryAena as DBRepository
from ..Utilidades.Conversores import ConversorCursorJson as Conversor
import mysql.connector


def obtener_cantidad_ciudad_anualmente_mensualmente(PaisOrigen, CiudadOrigen, Anio):
    """
    Obtiene la cantidad de vuelos salientes en una ciudad de un pais durante un año de forma mensual
    Obtiene la cantidad de vuelos salientes en una ciudad de un pais durante un año de forma mensual
    :param PaisOrigen: Pais del que salen los vuelos
    :type PaisOrigen: str
    :param CiudadOrigen: Ciudad de la que salen los vuelos
    :type CiudadOrigen: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadVuelosAenaSalientesMensualmenteDadoPaisOrigenCiudadDestinoAnio(PaisOrigen, CiudadOrigen, Anio)

    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)

    retval = conversor.convertirAJson(lista)
    return retval


def obtener_cantidad_ciudad_mensualmente(PaisOrigen, PaisDestino, CiudadDestino, AnioInicio, AnioFin):
    """
    Obtiene la cantidad de vuelos salientes de desde un pais hacia una ciudad destino durante un rango de años y lo organizamos mensualmente
    Obtiene la cantidad de vuelos salientes de desde un pais hacia una ciudad destino durante un rango de años
    :param PaisOrigen: Pais del que salen los vuelos
    :type PaisOrigen: str
    :param PaisDestino: Pais Destino
    :type PaisDestino: str
    :param CiudadDestino: Ciudad a la que llegan los vuelos
    :type CiudadDestino: str
    :param AnioInicio: Anio Inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadVuelosAenSalientesMensualmenteEnUnaCiudadDadoPaisOrigenCiudadDestinoAnioMinMax(PaisOrigen, PaisDestino, CiudadDestino, AnioInicio, AnioFin)
    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)
    retval = conversor.convertirAJson(lista)
    
    return retval


def obtener_cantidad_ciudades(Pais, AnioInicio, AnioFin):
    """
    Obtener cantidad de vuelos salientes de un pais en un rango de años
    Obtener cantidad de vuelos salientes de un pais en un rango de años
    :param Pais: Pais
    :type Pais: str
    :param AnioInicio: Año Inicio
    :type AnioInicio: int
    :param AnioFin: Año Fin
    :type AnioFin: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadVuelosAenaSalientesDadoPaisOrigenAnioMinMax(Pais, AnioInicio, AnioFin)
    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)
    retval = conversor.convertirAJson(lista)
    
    return retval


def obtener_cantidad_ciudades_durante_un_mes_en_rango_anios(PaisOrigen, Mes, AnioInicio, AnioFin):
    """
    Obtiene la cantidad de vuelos salientes en todas las ciudades de un pais durante un mes en un rango de años
    Obtiene la cantidad de vuelos salientes en todas las ciudades de un pais durante un mes en un rango de años
    :param PaisOrigen: Pais del que salen los vuelos
    :type PaisOrigen: str
    :param Mes: Mes
    :type Mes: str
    :param AnioInicio: Anio Inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadVuelosAenaSalientesAenaPaisesAlosQueSeViajaEnUnMesSeparadosPorAniosYCiudadesDadoPaisOrigenMesAniosMinMax(PaisOrigen, Mes, AnioInicio, AnioFin)
    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)
    retval = conversor.convertirAJson(lista)
    
    return retval



def obtener_cantidad_ciudades_en_anio(PaisOrigen, Anio):
    """
    Obtiene la cantidad de vuelos salientes en todas las ciudades de un pais durante un anio
    Obtiene la cantidad de vuelos salientes en todas las de un pais durante un anio
    :param PaisOrigen: Pais del que salen los vuelos
    :type PaisOrigen: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadVuelosAenaSalientesDivididosPorMesPorCiudadDadoPaisOrigenAnio(PaisOrigen, Anio)
    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)
    retval = conversor.convertirAJson(lista)
    
    return retval


def obtener_cantidad_por_ciudades_mensualmente(PaisOrigen):
    """
    Obtener cantidad de vuelos salientes por ciudades de un pais de forma mensual
    Obtener cantidad de vuelos salientes por ciudades de un pais de forma mensual
    :param PaisOrigen: Pais del que salen los vuelos
    :type PaisOrigen: str

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadVuelosAenaSalientesHaciaCiudadesPorAniosMesesDadoPaisOrigen(PaisOrigen)
    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)
    retval = conversor.convertirAJson(lista)
    
    return retval


def obtener_cantidad_por_ciudades_mensualmentey_anualmente(PaisOrigen, AnioInicio, AnioFin):
    """
    Obtener cantidad de vuelos salientes totales en todas las ciudad de un pais durante un rango de años separando por meses
    Obtiene la cantidad de vuelos salientes en todas las ciudades de un pais durante un rango de años separando por meses
    :param PaisOrigen: Pais del que salen los vuelos
    :type PaisOrigen: str
    :param AnioInicio: Anio Inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadVuelosSalientesHaciaCiudadesPorDadoPaisOrigenAnioMinMaxMensualmente(PaisOrigen, AnioInicio, AnioFin)
    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)
    retval = conversor.convertirAJson(lista)
    
    return retval


def obtener_cantidad_salientes_ciudad(PaisOrigen, CiudadOrigen, Anio):
    """
    Obtener cantidad de vuelos salientes en una ciudad de un pais durante un año
    Obtener cantidad de vuelos salientes en una ciudad de un pais durante un año
    :param PaisOrigen: Pais del que salen los vuelos
    :type PaisOrigen: str
    :param CiudadOrigen: Ciudad de la que salen los vuelos
    :type CiudadOrigen: str
    :param Anio: Año
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadVuelosAenaSalientesDadoPaisOrigenCiudadDestinoAnio(PaisOrigen, CiudadOrigen, Anio)
    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)
    retval = conversor.convertirAJson(lista)
    
    return retval


def obtener_cantidad_salientes_por_ciudades(Pais, AnioInicio, AnioFin): #Borrar
    """
    Obtener cantidad de vuelos salientes totales en las ciudades de un pais durante un rango de años mensualmente
    Obtener cantidad de vuelos salientes en las ciudades de un pais durante un año separando por meses
    :param Pais: Pais
    :type Pais: str
    :param AnioInicio: Anio Inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadVuelosSalientesHaciaCiudadesPorDadoPaisOrigenAnioMinMaxMensualmente(Pais, AnioInicio, AnioFin)
    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)
    retval = conversor.convertirAJson(lista)
    
    return retval
