from ..DB.DBRepositoryAmadeus import DBRepositoryAmadeus as DBRepository
from ..Utilidades.Conversores import ConversorCursorJson as Conversor

def obtener_cantidad_ciudad_rango_anios(PaisDestino, CiudadDestino, AnioInicio, AnioFin):
    """
    Obtiene la cantidad de personas que van hacia una ciudad durante un rango de años
    Obtiene la cantidad de personas que van hacia una ciudad durante un rango de años
    :param PaisDestino: Pais al que llegan los turistas
    :type PaisDestino: str
    :param CiudadDestino: Ciudad a la que llegan los turistas
    :type CiudadDestino: str
    :param AnioInicio: Anio Inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerDatosTuristasAenaDadoPaisDestinoCiudadDestinoAnioMinMax(PaisDestino, CiudadDestino, AnioInicio, AnioFin)

    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)

    retval = conversor.convertirAJson(lista)
    return retval



def obtener_cantidad_entrantes_rango_anios(PaisDestino, AnioInicio, AnioFin):
    """
    Dado un pais destino obtiene la cantidad de personas que viajan hacia el organizado por años
    Dado un pais destino obtiene la cantidad de personas que viajan hacia el y sus localizaciones organizado por años
    :param PaisDestino: Pais al que llegan los turistas
    :type PaisDestino: str
    :param AnioInicio: Anio Inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerNumeroTuristasAenaAnualmenteDadoPaisDestinoAnioMinMax(PaisDestino, AnioInicio, AnioFin)

    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)

    retval = conversor.convertirAJson(lista)
    return retval


def obtener_cantidad_origen_rango_anios(PaisDestino, AnioInicio, AnioFin):
    """
    Dado un pais destino obtiene la cantidad de personas que viajan hacia el y sus localizaciones organizado por años
    Dado un pais destino obtiene la cantidad de personas que viajan hacia el y sus localizaciones
    :param PaisDestino: Pais al que llegan los turistas
    :type PaisDestino: str
    :param AnioInicio: Anio Inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerPaisOrigenYNumeroTuristasAenaAnualmenteDadoPaisDestinoAnioMinMaxSeparadoPorCiudades(PaisDestino, AnioInicio, AnioFin)

    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)

    retval = conversor.convertirAJson(lista)
    return retval


def obtener_cantidad_origen_rango_anios_meses(PaisDestino, AnioInicio, AnioFin):
    """
    Dado un pais destino obtiene la cantidad de personas que viajan hacia el y sus localizaciones organizado por años y meses
    Dado un pais destino obtiene la cantidad de personas que viajan hacia el y sus localizaciones organizado por años y meses
    :param PaisDestino: Pais al que llegan los turistas
    :type PaisDestino: str
    :param AnioInicio: Anio Inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int

    :rtype: None
    """

    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerPaisOrigenYNumeroTuristasAenaAnualmenteDadoPaisDestinoAnioMinMaxSeparadoPorCiudadesYMeses(PaisDestino, AnioInicio, AnioFin)

    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)

    retval = conversor.convertirAJson(lista)
    return retval


def obtener_cantidad_rango_anios_meses(PaisDestino, AnioInicio, AnioFin):
    """
    Dado un pais destino obtiene la cantidad de personas que viajan hacia el organizado por años
    Dado un pais destino obtiene la cantidad de personas que viajan hacia el y sus localizaciones organizado por años y meses
    :param PaisDestino: Pais al que llegan los turistas
    :type PaisDestino: str
    :param AnioInicio: Anio Inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int

    :rtype: None
    """

    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerNumeroTuristasAenaAnualmenteDadoPaisDestinoAnioMinMaxSeparadoPorMeses(PaisDestino, AnioInicio, AnioFin)

    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)

    retval = conversor.convertirAJson(lista)
    return retval
