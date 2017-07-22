import connexion
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
from ..DB.DBRepository import DBRepository as DBRepository
from ..Utilidades.Conversores import ConversorCursorJson as Conversor
import mysql.connector


def obtener_cantidad_anio_ciudad(Pais, Ciudad, Anio):
    """
    Obtener cantidades de vuelos entrantes en la ciudad del pais divididas por meses
    Obtener cantidad de vuelos entrantes en las ciudades de un pais de divididas por meses
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

    cursor, labels = repository.ObtenerDatosVuelosEntrantesAenaEnUnAnioEnUnaCiudadMensualmenteDadoPaisDestinoCiudadAnio(Pais, Ciudad, Anio)
    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)
    retval = conversor.convertirAJson(lista)
    
    return retval



def obtener_cantidad_anio_por_ciudades(Pais, Anio):
    """
    Obtener cantidad de vuelos entrantes en las ciudades de un pais durante un año
    Obtener cantidad de vuelos entrantes en las ciudades de un pais durante un año
    :param Pais: Pais
    :type Pais: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerDatosVuelosEntrantesAenaEnUnAnioDivididosPorCiudadDadoPaisDestinoAnio(Pais, Anio)
    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)
    retval = conversor.convertirAJson(lista)
    
    return retval


def obtener_cantidad_anualmente(Pais, AnioInicio, AnioFin):
    """
    Obtener cantidad de vuelos entrantes anualmente dado un pais destino y un rango de años
    Obtiene la cantidad total de vuelos entrantes de cada año
    :param Pais: Pais
    :type Pais: str
    :param AnioInicio: Anio Inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int

    :rtype: Dict[str, int]
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerDatosVuelosEntrantesAenaDadoPaisDestinoAnioMinMax(Pais, AnioInicio, AnioFin)

    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)

    retval = conversor.convertirAJson(lista)
    return retval


def obtener_cantidad_ciudad(Pais, Ciudad, AnioInicio, AnioFin):
    """
    Obtener cantidad de vuelos entrantes en una ciudad de un pais durante el rango de años seleccionado
    Obtener cantidad de vuelos entrantes totales en las ciudades de un pais durante un rango de años
    :param Pais: Pais
    :type Pais: str
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

    cursor, labels = repository.ObtenerDatosVuelosEntrantesAenaDadoPaisDestinoCiudadDestinoAnioMinMax(Pais, Ciudad, AnioInicio, AnioFin)

    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)

    retval = conversor.convertirAJson(lista)
    return retval


def obtener_cantidad_entrantes_por_ciudades(Pais, AnioInicio, AnioFin):
    """
    Obtener cantidad de vuelos entrantes en las ciudades de un pais durante un rango de años
    Obtener cantidad de vuelos entrantes en las ciudades de un pais durante un rango de años
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

    cursor, labels = repository.ObtenerDatosVuelosEntrantesAenaDadoPaisDestinoAnioMinMax(Pais, AnioInicio, AnioFin)

    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)

    retval = conversor.convertirAJson(lista)
    return retval


def obtener_cantidad_mensual(Pais, Anio):
    """
    Obtener cantidad de vuelos entrantes durante los meses de un año 
    Obtiene la cantidad de vuelos totales de cada mes durante un año seleccionado
    :param Pais: Pais
    :type Pais: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerDatosVuelosEntrantesAenaMensualmenteDadoPaisDestinoAnio(Pais, Anio)

    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)

    retval = conversor.convertirAJson(lista)
    return retval



def obtener_cantidad_mensualmente(Pais, AnioInicio, AnioFin):
    """
    Obtener cantidad de vuelos entrantes de forma mensual dado un pais destino y un rango de años
    Obtiene la cantidad de vuelos en cada mes durante los años seleccionados
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

    cursor, labels = repository.ObtenerDatosVuelosEntrantesAenaMensualmenteDadoPaisDestinoAnioMinMax(Pais, AnioInicio, AnioFin)

    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)

    retval = conversor.convertirAJson(lista)
    return retval


def obtener_cantidad_mes(Pais, Mes, AnioInicio, AnioFin):
    """
    Obtener cantidad de vuelos entrantes durante el mismo mes en un rango de años
    Obtiene la cantidad de vuelos en un mes durante los años seleccionados
    :param Pais: Pais
    :type Pais: str
    :param Mes: Mes
    :type Mes: str
    :param AnioInicio: Año Inicio
    :type AnioInicio: int
    :param AnioFin: Año Fin
    :type AnioFin: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerDatosVuelosEntrantesAenaEnUnMesDadoPaisDestinoMesAnioMinMax(Pais, Mes, AnioInicio, AnioFin)

    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)

    retval = conversor.convertirAJson(lista)
    return retval


def obtener_cantidad_mes_anio_por_ciudades(Pais, Anio, Mes):
    """
    Obtener cantidad de vuelos entrantes en las ciudades del pais durante el mes del año seleccionado
    Obtener cantidad de vuelos entrantes en las ciudades de un pais durante un año
    :param Pais: Pais
    :type Pais: str
    :param Anio: Anio
    :type Anio: int
    :param Mes: Mes
    :type Mes: str

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerDatosVuelosEntrantesAenaMensualmenteDivididosPorCiudadDadoPaisDestinoMesAnio(Pais, Mes, Anio)

    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)


    retval = conversor.convertirAJson(lista)
    return retval


def obtener_cantidad_mes_ciudad(Pais, Ciudad, Mes, AnioInicio, AnioFin):
    """
    Obtener cantidad de vuelos entrantes en la ciudad del pais durante el mes del rango de años seleccionado
    Obtener cantidad de vuelos entrantes en las ciudades de un pais durante un año
    :param Pais: Pais
    :type Pais: str
    :param Ciudad: Ciudad
    :type Ciudad: str
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

    cursor, labels = repository.ObtenerDatosVuelosEntrantesAenaEnUnMesDadoPaisDestinoCiudadDestinoMesAnioMinMax(Pais, Ciudad, Mes, AnioInicio, AnioFin)

    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)

    retval = conversor.convertirAJson(lista)
    return retval


def obtener_cantidad_mes_por_ciudades(Pais, AnioInicio, AnioFin, Mes):
    """
    Obtener cantidad de vuelos entrantes en las ciudades de un pais durante un rango de años durante un mismo mes
    Obtener cantidad de vuelos entrantes en las ciudades de un pais durante un rango de años durante el mismo
    :param Pais: Pais
    :type Pais: str
    :param AnioInicio: AnioInicio
    :type AnioInicio: int
    :param AnioFin: AnioFin
    :type AnioFin: int
    :param Mes: Mes
    :type Mes: str

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerDatosVuelosEntrantesEnUnMesAenaDivididosPorCiudadesDadoPaisDestinoMesAnioMinMax(Pais, Mes, AnioInicio, AnioFin)

    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)

    retval = conversor.convertirAJson(lista)
    return retval

