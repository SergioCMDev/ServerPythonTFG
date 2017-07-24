from ..DB.DBRepositoryAmadeus import DBRepositoryAmadeus as DBRepository
from ..Utilidades.Conversores import ConversorCursorJson as Conversor


def obtener_cantidad_entrantes_rango_anios(Pais, AnioInicio, AnioFin):
    """
    Dado un pais destino obtiene la cantidad de personas que viajan hacia el organizado por años
    Dado un pais destino obtiene la cantidad de personas que viajan hacia el y sus localizaciones organizado por años
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

    cursor, labels = repository.ObtenerNumeroTuristasAenaAnualmenteDadoPaisDestinoAnioMinMax(Pais, AnioInicio, AnioFin)

    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)

    retval = conversor.convertirAJson(lista)
    return retval


def obtener_cantidad_origen_rango_anios(Pais, AnioInicio, AnioFin):
    """
    Dado un pais destino obtiene la cantidad de personas que viajan hacia el y sus localizaciones organizado por años
    Dado un pais destino obtiene la cantidad de personas que viajan hacia el y sus localizaciones
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

    cursor, labels = repository.ObtenerPaisOrigenYNumeroTuristasAenaAnualmenteDadoPaisDestinoAnioMinMaxSeparadoPorCiudades(Pais, AnioInicio, AnioFin)

    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)

    retval = conversor.convertirAJson(lista)
    return retval


def obtener_cantidad_origen_rango_anios_meses(Pais, AnioInicio, AnioFin):
    """
    Dado un pais destino obtiene la cantidad de personas que viajan hacia el y sus localizaciones organizado por años y meses
    Dado un pais destino obtiene la cantidad de personas que viajan hacia el y sus localizaciones organizado por años y meses
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

    cursor, labels = repository.ObtenerPaisOrigenYNumeroTuristasAenaAnualmenteDadoPaisDestinoAnioMinMaxSeparadoPorCiudadesYMeses(Pais, AnioInicio, AnioFin)

    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)

    retval = conversor.convertirAJson(lista)
    return retval


def obtener_cantidad_rango_anios_meses(Pais, AnioInicio, AnioFin):
    """
    Dado un pais destino obtiene la cantidad de personas que viajan hacia el organizado por años
    Dado un pais destino obtiene la cantidad de personas que viajan hacia el y sus localizaciones organizado por años y meses
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

    cursor, labels = repository.ObtenerNumeroTuristasAenaAnualmenteDadoPaisDestinoAnioMinMaxSeparadoPorMeses(Pais, AnioInicio, AnioFin)

    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)

    retval = conversor.convertirAJson(lista)
    return retval
