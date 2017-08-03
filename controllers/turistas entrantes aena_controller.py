from ..DB.DBRepositoryAena import DBRepositoryAena as DBRepository
from ..Utilidades.Conversores import Conversores as Conversor

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
    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz , lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

    ##Mostrar JSON Reducido
#    retval = conversor.convertirAJson(arrayTuplas)
#    return retval



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

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz , lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

    ##Mostrar JSON Reducido
#    retval = conversor.convertirAJson(arrayTuplas)
#    return retval


def obtener_cantidad_origen_rango_anios(PaisDestino, AnioInicio, AnioFin): ##MATRIZ MAS DE 4 VARIABLES
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

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
#    matriz , lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels)
#    retval = conversor.ObtenerDataJSONExtendido(matriz)
#    return retval

    ##Mostrar JSON Reducido
    retval = conversor.convertirAJson(arrayTuplas)
    return retval


def obtener_cantidad_origen_rango_anios_meses(PaisDestino, AnioInicio, AnioFin): ##MATRIZ MAS DE 4 VARIABLES
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

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
#    matriz , lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels)
#    retval = conversor.ObtenerDataJSONExtendido(matriz)
#    return retval

    ##Mostrar JSON Reducido
    retval = conversor.convertirAJson(arrayTuplas)
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

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz , lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

    ##Mostrar JSON Reducido
#    retval = conversor.convertirAJson(arrayTuplas)
#    return retval
