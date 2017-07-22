import connexion
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
from ..DB.DBRepository import DBRepository as DBRepository
from ..Utilidades.Conversores import ConversorCursorJson as Conversor
import mysql.connector


def obtener_cantidad_ciudad_anualmente_mensualmente(Pais, Ciudad, Anio): #OK
    """
    Obtiene la cantidad de vuelos salientes en una ciudad de un pais durante un año de forma mensual
    Obtiene la cantidad de vuelos salientes en una ciudad de un pais durante un año de forma mensual
    :param Pais: Pais
    :type Pais: str
    :param Ciudad: Ciudad
    :type Ciudad: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadVuelosAenaSalientesMensualmenteDadoPaisOrigenCiudadDestinoAnio(Pais, Ciudad, Anio)

    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)

    retval = conversor.convertirAJson(lista)
    return retval


def obtener_cantidad_ciudad_mensualmente(Pais, PaisDestino, Ciudad, AnioInicio, AnioFin): #OK
    """
    Obtiene la cantidad de vuelos salientes de desde un pais hacia una ciudad destino durante un rango de años y lo organizamos mensualmente
    Obtiene la cantidad de vuelos salientes de desde un pais hacia una ciudad destino durante un rango de años
    :param Pais: Pais
    :type Pais: str
    :param PaisDestino: Pais Destino
    :type PaisDestino: str
    :param Ciudad: Ciudad
    :type Ciudad: str
    :param AnioInicio: Anio Inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadVuelosAenSalientesMensualmenteEnUnaCiudadDadoPaisOrigenCiudadDestinoAnioMinMax(Pais, PaisDestino, Ciudad, AnioInicio, AnioFin)
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


def obtener_cantidad_ciudades_durante_un_mes_en_rango_anios(Pais, Mes, AnioInicio, AnioFin): #OK
    """
    Obtiene la cantidad de vuelos salientes en todas las ciudades de un pais durante un mes en un rango de años
    Obtiene la cantidad de vuelos salientes en todas las ciudades de un pais durante un mes en un rango de años
    :param Pais: Pais
    :type Pais: str
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

    cursor, labels = repository.ObtenerCantidadVuelosAenaSalientesAenaPaisesAlosQueSeViajaEnUnMesSeparadosPorAniosYCiudadesDadoPaisOrigenMesAniosMinMax(Pais, Mes, AnioInicio, AnioFin)
    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)
    retval = conversor.convertirAJson(lista)
    
    return retval


def obtener_cantidad_ciudades_en_anio(Pais, Anio): #OK
    """
    Obtiene la cantidad de vuelos salientes en todas las ciudades de un pais durante un anio
    Obtiene la cantidad de vuelos salientes en todas las de un pais durante un anio
    :param Pais: Pais
    :type Pais: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadVuelosAenaSalientesDivididosPorMesPorCiudadDadoPaisOrigenAnio(Pais, Anio)
    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)
    retval = conversor.convertirAJson(lista)
    
    return retval


def obtener_cantidad_por_ciudades_mensualmente(Pais): #OK
    """
    Obtener cantidad de vuelos salientes en una ciudad de un pais durante un año de forma mensual
    Obtener cantidad de vuelos salientes en una ciudad de un pais durante un año separando por meses
    :param Pais: Pais
    :type Pais: str

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadVuelosAenaSalientesHaciaCiudadesPorAniosMesesDadoPaisOrigen(Pais)
    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)
    retval = conversor.convertirAJson(lista)
    
    return retval


def obtener_cantidad_por_ciudades_mensualmentey_anualmente(Pais, AnioInicio, AnioFin): #OK
    """
    Obtener cantidad de vuelos salientes totales en todas las ciudad de un pais durante un rango de años separando por meses
    Obtiene la cantidad de vuelos salientes en todas las ciudades de un pais durante un rango de años separando por meses
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


def obtener_cantidad_salientes_ciudad(Pais, Ciudad, Anio): #OK
    """
    Obtener cantidad de vuelos salientes en una ciudad de un pais durante un año
    Obtener cantidad de vuelos salientes en una ciudad de un pais durante un año
    :param Pais: Pais
    :type Pais: str
    :param Ciudad: Ciudad
    :type Ciudad: str
    :param Anio: Año
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadVuelosAenaSalientesDadoPaisOrigenCiudadDestinoAnio(Pais, Ciudad, Anio)
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
