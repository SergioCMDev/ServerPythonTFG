from ..DB.DBRepositoryAmadeus import DBRepositoryAmadeus as DBRepository
from ..Utilidades.Conversores import ConversorCursorJson as Conversor

def obtener_cantidad_ciudad_durante_mes_en_rango_anios(Pais, Mes, Ciudad, AnioInicio, AnioFin):
    """
    Dado un pais origen, una ciudad, un mes y un rango de años obtiene la cantidad de turistas salientes de ese pais diviendo por meses y años
    Dado un pais origen, una ciudad, un mes y un rango de años obtiene la cantidad de turistas salientes de ese pais diviendo por meses y años
    :param Pais: Pais
    :type Pais: str
    :param Mes: Mes
    :type Mes: str
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

    cursor, labels = repository.ObtenerCantidadCiudadDuranteMesEnRangoAnios(Pais, Mes, Ciudad, AnioInicio, AnioFin)

    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)

    retval = conversor.convertirAJson(lista)
    return retval


def obtener_cantidad_en_ciudad_en_rango_anios(Pais, Mes, AnioInicio, AnioFin):
    """
    Dado un pais origen, una ciudad y un rango de años obtiene la cantidad de turistas que salen de ese pais durante ese rango de años de esa ciudad
    Dado un pais origen, una ciudad y un rango de años obtiene la cantidad de vuelos salientes durante ese rango de años de esa ciudad
    :param Pais: Pais
    :type Pais: str
    :param Mes: Ciudad
    :type Mes: str
    :param Anio_Inicio: AnioInicio
    :type Anio_Inicio: int
    :param AnioFin: AnioFin
    :type AnioFin: int

    :rtype: None
    """
    
    
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadEnCiudadEnRangoAnios(Pais, Mes, AnioInicio, AnioFin)

    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)

    retval = conversor.convertirAJson(lista)
    return retval


def obtener_cantidad_en_ciudades_mensualmente_en_anio(Pais, AnioInicio, AnioFin):
    """
    Dado un pais origen y un rango de años obtiene la cantidad de turistas salientes de ese pais durante esos años divididos por ciudad y mes
    Dado un pais origen y un rango de años obtiene la cantidad de turistas salientes de ese pais durante esos años divididos por ciudad y mes
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

    cursor, labels = repository.ObtenerDatosTuristasSalientesAmadeusSeparadoPorCiudadesMensualmenteDadoPaisOrigenAnioMinMax(Pais, AnioInicio, AnioFin)

    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)

    retval = conversor.convertirAJson(lista)
    return retval


def obtener_cantidad_en_pais_en_anio(Pais, Anio):
    """
    Dado un pais origen y un anio obtiene la cantidad de turistas que salen de dicho pais durante ese año
    Dado un pais origen y un anio obtiene la cantidad de turistas que salen de dicho pais durante ese año dividiendo por ciudades
    :param Pais: Pais
    :type Pais: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerDatosTuristasSalientesAmadeusEnUnAnioDadoPaisOrigenAnio(Pais, Anio)

    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)

    retval = conversor.convertirAJson(lista)
    return retval


def obtener_cantidad_en_pais_en_anio_mensualmente(Pais, Anio):
    """
    Dado un pais origen y un año obtiene la cantidad de turistas salientes de ese pais durante ese año dividido por meses
    Dado un pais origen y un año obtiene la cantidad de turistas salientes de ese pais durante ese año dividido por meses
    :param Pais: Pais
    :type Pais: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadEnPaisEnAnioMensualmente(Pais, Anio)

    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)

    retval = conversor.convertirAJson(lista)
    return retval


def obtener_cantidad_en_pais_en_ciudades_en_anio(Pais, Anio):
    """
    Dado un pais origen y un año obtiene la cantidad de turistas salientes de ese pais durante ese año dividido por ciudades origen
    Dado un pais origen y un año obtiene la cantidad de turistas salientes de ese pais durante ese año dividido por ciudades origen
    :param Pais: Pais
    :type Pais: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadEnPaisEnCiudadesEnAnio(Pais, Anio)

    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)

    retval = conversor.convertirAJson(lista)
    return retval


def obtener_cantidad_en_pais_en_mes_en_rango_anios(Pais, Mes, AnioInicio, AnioFin):
    """
    Dado un pais origen, un mes y un rango de años obtiene la cantidad de turistas salientes de ese pais durante esos años y ese mes
    Dado un pais origen, un mes y un rango de años obtiene la cantidad de turistas salientes de ese pais durante esos años y ese mes
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

    cursor, labels = repository.ObtenerCantidadEnPaisEnMesEnRangoAnios(Pais, Mes, AnioInicio, AnioFin)

    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)

    retval = conversor.convertirAJson(lista)
    return retval


def obtener_cantidad_en_pais_en_rango_anios(Pais, AnioInicio, AnioFin):
    """
    Dado un pais origen y un rango de años obtiene la cantidad de turistas salientes de ese pais durante esos años
    Dado un pais origen y un rango de años obtiene la cantidad de turistas salientes de ese pais durante esos años
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

    cursor, labels = repository.ObtenerCantidadEnPaisEnRangoAnios(Pais, AnioInicio, AnioFin)

    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)

    retval = conversor.convertirAJson(lista)
    return retval
