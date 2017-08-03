from ..DB.DBRepositoryAmadeus import DBRepositoryAmadeus as DBRepository
from ..Utilidades.Conversores import Conversores as Conversor


def obtener_cantidad_total_vuelos_pais_en_ciudad_en_mes_en_anio(PaisDestino, CiudadDestino, Mes, Anio): #OK
    """
    Dado un pais, una ciudad, un mes y un año obtiene la cantidad total de vuelos que llegan a esa ciudad durante ese año y mes
    Dado un pais, una ciudad, un mes y un año obtiene la cantidad total de vuelos que llegan a esa ciudad durante ese año y mes
    :param PaisDestino: Pais al que llegan los vuelos
    :type PaisDestino: str
    :param CiudadDestino: Ciudad a la que llegan los vuelos
    :type CiudadDestino: str
    :param Mes: Mes
    :type Mes: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerDatosVuelosEntrantesAmadeusEnUnMesEnUnAnioDadoPaisDestinoCiudadDestinoAnio(PaisDestino, CiudadDestino, Mes, Anio)
    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
#    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas, labels)
#    retval = conversor.ObtenerDataJSONExtendido(matriz)
#
#    return retval

    ##Mostrar JSON Reducido
    retval = conversor.convertirAJson(arrayTuplas)
    return retval



def obtener_cantidad_total_vuelos_pais_en_ciudad_mensual_en_anio(PaisDestino, CiudadDestino, Anio): #OK
    """
    Dado un pais, una ciudad y un año obtiene la cantidad total de vuelos que llegan a esa ciudad durante ese año separando por meses
    Dado un pais, una ciudad y un año obtiene la cantidad total de vuelos que llegan a esa ciudad durante ese año separando por meses
    :param PaisDestino: Pais al que llegan los vuelos
    :type PaisDestino: str
    :param CiudadDestino: Ciudad a la que llegan los vuelos
    :type CiudadDestino: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerDatosVuelosEntrantesAmadeusEnUnAnioMensualmenteDadoPaisDestinoCiudadDestinoAnio(PaisDestino, CiudadDestino, Anio)
    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas, labels)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

    ##Mostrar JSON Reducido
#    retval = conversor.convertirAJson(arrayTuplas)
#    return retval




def obtener_cantidad_total_vuelos_totales_pais_en_ciudad_en_anio(PaisDestino, CiudadDestino, Anio): #OK
    """
    Dado un pais, una ciudad y un año obtiene la cantidad total de vuelos que llegan a esa ciudad durante ese año
    Dado un pais, una ciudad y un año obtiene la cantidad total de vuelos que llegan a esa ciudad durante ese año
    :param PaisDestino: Pais al que llegan los vuelos
    :type PaisDestino: str
    :param CiudadDestino: Ciudad a la que llegan los vuelos
    :type CiudadDestino: str
    :param Mes: Mes
    :type Mes: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerDatosVuelosSalientesAmadeusMensualmenteDadoPaisOrigenCiudadOrigenAnio(PaisDestino, CiudadDestino, Anio)
    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas, labels)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

    ##Mostrar JSON Reducido
#    retval = conversor.convertirAJson(arrayTuplas)
#    return retval



def obtener_cantidad_total_vuelos_totales_pais_en_mes_en_anio(PaisDestino, Mes, Anio): #OK
    """
    Dado un pais, un mes y un año obtiene la cantidad total de vuelos que llegan a ese pais durante ese año y mes
    Dado un pais, un mes y un año obtiene la cantidad total de vuelos que llegan a ese pais durante ese año y mes
    :param PaisDestino: Pais al que llegan los vuelos
    :type PaisDestino: str
    :param CiudadDestino: Ciudad a la que llegan los vuelos
    :type CiudadDestino: str
    :param Mes: Mes
    :type Mes: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerDatosVuelosEntrantesAmadeusEnUnMesEnUnAnioDadoPaisDestinoAnio(PaisDestino, Mes, Anio)
    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
#    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas, labels)
#    retval = conversor.ObtenerDataJSONExtendido(matriz)

#    return retval

    ##Mostrar JSON Reducido
    retval = conversor.convertirAJson(arrayTuplas)
    return retval




def obtener_cantidad_vuelos_ciudad_en_mes_en_rango_anios(PaisDestino, Mes, AnioInicio, AnioFin): #OK
    """
    Dado un pais, un mes y un rango de años obtiene la cantidad total de vuelos que llegan a ese pais durante ese mes y ese rango de años separando por ciudades
    Dado un pais, un mes y un rango de años obtiene la cantidad total de vuelos que llegan a ese pais durante ese mes y ese rango de años separando por ciudades
    :param PaisDestino: Pais al que llegan los vuelos
    :type PaisDestino: str
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

    cursor, labels = repository.ObtenerDatosVuelosEntrantesAmadeusEnUnMesDadoPaisDestinoAnioMinMaxSeparandoPorCiudades(PaisDestino, Mes, AnioInicio, AnioFin)
    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas, labels)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

    ##Mostrar JSON Reducido
#    retval = conversor.convertirAJson(arrayTuplas)
#    return retval




def obtener_cantidad_vuelos_ciudad_pais_en_mes_en_anio(PaisDestino, Mes, Anio): #OK
    """
    Dado un pais, un mes y un año obtiene la cantidad total de vuelos que llegan a esa ciudad durante ese mes y ese año separando por ciudades
    Dado un pais, un mes y un año obtiene la cantidad total de vuelos que llegan a esa ciudad durante ese mes y ese año separando por ciudades
    :param PaisDestino: Pais al que llegan los vuelos
    :type PaisDestino: str
    :param Mes: Mes
    :type Mes: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerDatosVuelosEntrantesAmadeusEnUnMesEnUnAnioDadoPaisDestinoAnioSeparandoPorCiudades(PaisDestino, Mes, Anio)
    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas, labels)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

    ##Mostrar JSON Reducido
#    retval = conversor.convertirAJson(arrayTuplas)
#    return retval




def obtener_cantidad_vuelos_ciudades_pais_en_anio(PaisDestino, Anio): #OK
    """
    Dado un pais y un año obtiene la cantidad de vuelos que llegan a ese pais durante ese año divividos por ciudades
    Dado un pais y un año obtiene la cantidad de vuelos que llegan a ese pais durante ese año divividos por ciudades
    :param PaisDestino: Pais al que llegan los vuelos
    :type PaisDestino: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerDatosVuelosEntrantesAmadeusEnUnAnioDadoPaisDestinoAnioSeparandoPorCiudades(PaisDestino, Anio)
    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas, labels)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

    ##Mostrar JSON Reducido
#    retval = conversor.convertirAJson(arrayTuplas)
#    return retval



def obtener_cantidad_vuelos_pais_en_anio(PaisDestino, Anio): #OK
    """
    Dado un pais y un año obtiene la cantidad de vuelos que llegan a ese pais durante ese año
    Dado un pais y un año obtiene la cantidad de vuelos que llegan a ese pais durante ese año
    :param PaisDestino: Pais al que llegan los vuelos
    :type PaisDestino: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerDatosVuelosEntrantesAmadeusTotalesEnUnAnioDadoPaisDestinoAnio(PaisDestino, Anio)
    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
#    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas, labels)
#    retval = conversor.ObtenerDataJSONExtendido(matriz)
#
#    return retval

    ##Mostrar JSON Reducido
    retval = conversor.convertirAJson(arrayTuplas)
    return retval




def obtener_cantidad_vuelos_pais_en_ciudad_en_mes_en_rango_anios(PaisDestino, CiudadDestino, Mes, AnioInicio, AnioFin): #OK
    """
    Dado un pais, una ciudad, un mes y un rango de años obtiene la cantidad total de vuelos que llegan a esa ciudad durante esos años y mes
    Dado un pais, una ciudad y un rango de años obtiene la cantidad total de vuelos que llegan a esa ciudad durante esos años separado por meses y ciudad
    :param PaisDestino: Pais al que llegan los vuelos
    :type PaisDestino: str
    :param CiudadDestino: Ciudad a la que llegan los vuelos
    :type CiudadDestino: str
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

    cursor, labels = repository.ObtenerDatosVuelosEntrantesAmadeusEnUnMesDadoPaisDestinoCiudadDestinoAnioMinMax(PaisDestino, CiudadDestino, Mes, AnioInicio, AnioFin)
    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas, labels)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

    ##Mostrar JSON Reducido
#    retval = conversor.convertirAJson(arrayTuplas)
#    return retval




def obtener_cantidad_vuelos_pais_en_ciudad_en_rango_anios(PaisDestino, CiudadDestino, AnioInicio, AnioFin): #OK
    """
    Dado un pais, una ciudad y un rango de años obtiene la cantidad total de vuelos que llegan a esa ciudad durante esos años
    Dado un pais, una ciudad y un rango de años obtiene la cantidad total de vuelos que llegan a esa ciudad durante esos años
    :param PaisDestino: Pais al que llegan los vuelos
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

    cursor, labels = repository.ObtenerDatosVuelosEntrantesAmadeusDadoPaisDestinoCiudadDestinoAnioMinMax(PaisDestino, CiudadDestino, AnioInicio, AnioFin)
    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas, labels)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

    ##Mostrar JSON Reducido
#    retval = conversor.convertirAJson(arrayTuplas)
#    return retval



def obtener_cantidad_vuelos_pais_en_ciudad_mensual_en_rango_anios(PaisDestino, CiudadDestino, AnioInicio, AnioFin): #OK
    """
    Dado un pais, una ciudad y un rango de años obtiene la cantidad total de vuelos que llegan a esa ciudad durante esos años separado por meses
    Dado un pais, una ciudad y un rango de años obtiene la cantidad total de vuelos que llegan a esa ciudad durante esos años separado por meses
    :param PaisDestino: Pais al que llegan los vuelos
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

    cursor, labels = repository.ObtenerDatosVuelosEntrantesAmadeusMensualmenteDadoPaisDestinoCiudadDestinoAnioMinMax(PaisDestino, CiudadDestino, AnioInicio, AnioFin)
    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas, labels)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

    ##Mostrar JSON Reducido
#    retval = conversor.convertirAJson(arrayTuplas)
#    return retval



def obtener_cantidad_vuelos_pais_en_mes_en_rango_anios(PaisDestino, Mes, AnioInicio, AnioFin): #OK
    """
    Dado un pais, un mes y un rango de años obtiene la cantidad total de vuelos que llegan a ese pais durante esos años
    Dado un pais, un mes y un rango de años obtiene la cantidad total de vuelos que llegan a ese pais durante esos años
    :param PaisDestino: Pais al que llegan los vuelos
    :type PaisDestino: str
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

    cursor, labels = repository.ObtenerDatosVuelosEntrantesAmadeusEnUnMesDadoPaisDestinoMesAnioMinMax(PaisDestino, Mes, AnioInicio, AnioFin)
    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas, labels)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

    ##Mostrar JSON Reducido
#    retval = conversor.convertirAJson(arrayTuplas)
#    return retval




def obtener_cantidad_vuelos_pais_en_rango_anios(PaisDestino, AnioInicio, AnioFin):#OK
    """
    Dado un pais y un rango de años obtiene la cantidad de vuelos que llegan a ese pais diviendo por años
    Dado un pais y un rango de años obtiene la cantidad de vuelos que llegan a ese pais diviendo por años
    :param PaisDestino: Pais al que llegan los vuelos
    :type PaisDestino: str
    :param AnioInicio: Anio Inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerDatosVuelosEntrantesAmadeusTotalesDadoPaisDestinoAnioMinMax(PaisDestino, AnioInicio, AnioFin)
    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas, labels)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

    ##Mostrar JSON Reducido
#    retval = conversor.convertirAJson(arrayTuplas)
#    return retval


