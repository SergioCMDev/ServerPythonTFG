from ..DB.DBRepositoryAmadeus import DBRepositoryAmadeus as DBRepository
from ..Utilidades.Conversores import Conversores as Conversor

def obtener_cantidad_ciudad_durante_mes_en_rango_anios(PaisOrigen, Mes, CiudadOrigen, AnioInicio, AnioFin): #OK
    """
    Dado un pais origen, una ciudad, un mes y un rango de años obtiene la cantidad de turistas salientes de ese pais diviendo por meses y años
    Dado un pais origen, una ciudad, un mes y un rango de años obtiene la cantidad de turistas salientes de ese pais diviendo por meses y años
    :param PaisOrigen: Pais del que salen los turistas
    :type PaisOrigen: str
    :param Mes: Mes
    :type Mes: str
    :param CiudadOrigen: Ciudad de la que salen los turistas
    :type CiudadOrigen: str
    :param AnioInicio: Anio Inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerPaisOrigenYNumeroTuristasAmadeusAnualmenteDadoPaisDestinoCiudadDestinoMesAnioMinMax(PaisOrigen, CiudadOrigen , Mes, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)


    ##Mostrar JSON Extendido
#    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels)
#    retval = conversor.ObtenerDataJSONExtendido(matriz)

#    return retval

    ##Mostrar JSON Reducido
    retval = conversor.convertirAJson(arrayTuplas)
    return retval


def obtener_cantidad_en_ciudad_en_rango_anios(PaisOrigen, CiudadOrigen, AnioInicio, AnioFin): #OK
    """
    Dado un pais origen, una ciudad y un rango de años obtiene la cantidad de turistas que salen de ese pais durante ese rango de años de esa ciudad
    Dado un pais origen, una ciudad y un rango de años obtiene la cantidad de vuelos salientes durante ese rango de años de esa ciudad
    :param PaisOrigen: Pais del que salen los turistas
    :type PaisOrigen: str
    :param CiudadOrigen: Ciudad de la que salen los turistas
    :type CiudadOrigen: str
    :param AnioInicio: Anio Inicio
    :type AnioInicio: int
    :param AnioFin: AnioFin
    :type AnioFin: int

    :rtype: None
    """
    
    
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerDatosTuristasSalientesAmadeusDadoPaisOrigenCiudadOrigenAnioMinMax(PaisOrigen, CiudadOrigen, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)


    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

    ##Mostrar JSON Reducido
#    retval = conversor.convertirAJson(arrayTuplas)
#    return retval


def obtener_cantidad_en_ciudades_mensualmente_en_rango_anios(PaisOrigen, AnioInicio, AnioFin): #OK
    """
    Dado un pais origen y un rango de años obtiene la cantidad de turistas salientes de ese pais durante esos años divididos por ciudad y mes
    Dado un pais origen y un rango de años obtiene la cantidad de turistas salientes de ese pais durante esos años divididos por ciudad y mes
    :param PaisOrigen: Pais del que salen los turistas
    :type PaisOrigen: str
    :param AnioInicio: Anio Inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerDatosTuristasSalientesAmadeusSeparadoPorCiudadesMensualmenteDadoPaisOrigenAnioMinMax(PaisOrigen, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)


    ##Mostrar JSON Extendido
#    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels)
#    retval = conversor.ObtenerDataJSONExtendido(matriz)
#
#    return retval

    ##Mostrar JSON Reducido
    retval = conversor.convertirAJson(arrayTuplas)
    return retval


def obtener_cantidad_en_pais_en_anio(PaisOrigen, Anio): #OK
    """
    Dado un pais origen y un anio obtiene la cantidad de turistas que salen de dicho pais durante ese año
    Dado un pais origen y un anio obtiene la cantidad de turistas que salen de dicho pais durante ese año dividiendo por ciudades
    :param PaisOrigen: Pais del que salen los turistas
    :type PaisOrigen: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerDatosTuristasSalientesAmadeusEnUnAnioDadoPaisOrigenAnio(PaisOrigen, Anio)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)


    ##Mostrar JSON Extendido
#    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, Anio, Anio)
#    retval = conversor.ObtenerDataJSONExtendido(matriz)
#
#    return retval

    ##Mostrar JSON Reducido
    retval = conversor.convertirAJson(arrayTuplas)
    return retval


def obtener_cantidad_en_pais_en_anio_mensualmente(PaisOrigen, Anio): #OK
    """
    Dado un pais origen y un año obtiene la cantidad de turistas salientes de ese pais durante ese año dividido por meses
    Dado un pais origen y un año obtiene la cantidad de turistas salientes de ese pais durante ese año dividido por meses
    :param PaisOrigen: Pais del que salen los turistas
    :type PaisOrigen: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerDatosTuristasSalientesAmadeusEnUnAnioDadoPaisOrigenAnioMensualmente(PaisOrigen, Anio)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)


    ##Mostrar JSON Extendido
#    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, Anio, Anio)
#    retval = conversor.ObtenerDataJSONExtendido(matriz)
#
#    return retval

    ##Mostrar JSON Reducido
    retval = conversor.convertirAJson(arrayTuplas)
    return retval


def obtener_cantidad_en_pais_en_ciudades_en_anio(PaisOrigen, Anio): #OK
    """
    Dado un pais origen y un año obtiene la cantidad de turistas salientes de ese pais durante ese año dividido por ciudades origen
    Dado un pais origen y un año obtiene la cantidad de turistas salientes de ese pais durante ese año dividido por ciudades origen
    :param PaisOrigen: Pais del que salen los turistas
    :type PaisOrigen: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerDatosTuristasSalientesAmadeusEnUnAnioDadoPaisOrigenAnioSeparandoPorCiudades(PaisOrigen, Anio)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)


    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, Anio, Anio)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

    ##Mostrar JSON Reducido
#    retval = conversor.convertirAJson(arrayTuplas)
#    return retval


def obtener_cantidad_en_pais_en_mes_en_rango_anios(PaisOrigen, Mes, AnioInicio, AnioFin): #OK
    """
    Dado un pais origen, un mes y un rango de años obtiene la cantidad de turistas salientes de ese pais durante esos años y ese mes
    Dado un pais origen, un mes y un rango de años obtiene la cantidad de turistas salientes de ese pais durante esos años y ese mes
    :param PaisOrigen: Pais del que salen los turistas
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

    cursor, labels = repository.ObtenerDatosTuristasSalientesAmadeusAnualmenteEnUnMesDadoPaisOrigenMesAnioMinMax(PaisOrigen, Mes, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)


    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

    ##Mostrar JSON Reducido
#    retval = conversor.convertirAJson(arrayTuplas)
#    return retval


def obtener_cantidad_en_pais_en_rango_anios(PaisOrigen, AnioInicio, AnioFin): #OK
    """
    Dado un pais origen y un rango de años obtiene la cantidad de turistas salientes de ese pais durante esos años
    Dado un pais origen y un rango de años obtiene la cantidad de turistas salientes de ese pais durante esos años
    :param PaisOrigen: Pais del que salen los turistas
    :type PaisOrigen: str
    :param AnioInicio: Anio Inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerDatosTuristasSalientesAmadeusAnualmenteDadoPaisOrigenAnioMinMax(PaisOrigen, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)


    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

    ##Mostrar JSON Reducido
#    retval = conversor.convertirAJson(arrayTuplas)
#    return retval
