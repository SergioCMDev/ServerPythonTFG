from ..DB.DBRepositoryAmadeus import DBRepositoryAmadeus as DBRepository
from ..Utilidades.Conversores import Conversores as Conversor

def obtener_cantidad_turistas_en_ciudades_mensual_en_rango_anios(PaisDestino, AnioInicio, AnioFin): #OK
    """
    Dado un pais y un rango de años obtiene la cantidad total de personas que llegan a ese pais separando por ciudades, meses y años
    Dado un pais y un rango de años obtiene la cantidad total de personas que llegan a ese pais separando por ciudades, meses y años
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

    cursor, labels = repository.ObtenerPaisOrigenYNumeroTuristasAmadeusAnualmenteDadoPaisDestinoAnioMinMaxSeparadoPorCiudadesYMeses(PaisDestino, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
#    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels)
#    retval = conversor.ObtenerDataJSONExtendido(matriz)
#
#    return retval

    ##Mostrar JSON Reducido
    retval = conversor.convertirAJson(arrayTuplas)
    return retval


def obtener_cantidad_turistas_en_pais_en_rango_anios(PaisDestino, AnioInicio, AnioFin): #OK
    """
    Dado un pais y un rango de años obtiene la cantidad total de personas que llegan a ese pais separando por años
    Dado un pais y un rango de años obtiene la cantidad total de personas que llegan a ese pais separando por años
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

    cursor, labels = repository.ObtenerNumeroTuristasAmadeusAnualmenteDadoPaisDestinoAnioMinMax(PaisDestino, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)


    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

    ##Mostrar JSON Reducido
#    retval = conversor.convertirAJson(arrayTuplas)
#    return retval


def obtener_cantidad_turistas_y_ciudades_origen_en_ciudad_en_mes_en_rango_anios(PaisDestino, CiudadDestino, Mes, AnioInicio, AnioFin): #OK
    """
    Dado un pais, una ciudad, un mes y un rango de años obtiene la cantidad total de personas que llegan a esa ciudad separando por años,paises y ciudades de origen
    Dado un pais, una ciudad, un mes y un rango de años obtiene la cantidad total de personas que llegan a esa ciudad separando por años,paises y ciudades de origen
    :param PaisDestino: Pais al que llegan los turistas
    :type PaisDestino: str
    :param CiudadDestino: Ciudad a la que llegan los turistas
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

    cursor, labels = repository.ObtenerPaisOrigenYNumeroTuristasAmadeusAnualmenteDadoPaisDestinoCiudadDestinoMesAnioMinMax(PaisDestino, CiudadDestino, Mes, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)


    ##Mostrar JSON Extendido
#    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels)
#    retval = conversor.ObtenerDataJSONExtendido(matriz)

#    return retval

    ##Mostrar JSON Reducido
    retval = conversor.convertirAJson(arrayTuplas)
    return retval



def obtener_cantidad_turistas_y_ciudades_origen_en_ciudad_en_rango_anios(PaisDestino, AnioInicio, AnioFin): #OK
    """
    Dado un pais y un rango de años obtiene la cantidad total de personas que llegan a esa ciudad separando por años, paises y ciudades de origen
    Dado un pais, una ciudad, un mes y un rango de años obtiene la cantidad total de personas que llegan a esa ciudad separando por años,paises y ciudades de origen
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

    cursor, labels = repository.ObtenerPaisOrigenYNumeroTuristasAmadeusSeparadoPorCiudadesAnualmenteDadoPaisDestinoAnioMinMax(PaisDestino, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)


    ##Mostrar JSON Extendido
#    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels)
#    retval = conversor.ObtenerDataJSONExtendido(matriz)
#
#    return retval

    ##Mostrar JSON Reducido
    retval = conversor.convertirAJson(arrayTuplas)
    return retval


def obtener_cantidad_turistas_mensualmente_en_ciudad_en_rango_anios(PaisDestino, CiudadDestino, AnioInicio, AnioFin):
    """
    Dado un pais, una ciudad y un rango de años obtiene la cantidad total de personas que llegan a esa ciudad separando por años y meses
    Dado un pais y un rango de años obtiene la cantidad total de personas que llegan a ese pais separando por años y en esos años por meses
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

    cursor, labels = repository.ObtenerNumeroTuristasEntrantesAnualmenteEnMesesAmadeusDadoPaisDestinoCiudadDestinoAnioMinMax(PaisDestino, CiudadDestino, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels)
#    print(matriz)
    retval = conversor.ObtenerDataJSONExtendido(matriz)
#
    return retval

    ##Mostrar JSON Reducido
#    retval = conversor.convertirAJson(arrayTuplas)
#    return retval


def obtener_cantidad_turistas_y_ciudades_origen_en_pais_en_rango_anios(PaisDestino, CiudadDestino, AnioInicio, AnioFin): #OK
    """
    Dado un pais, una ciudad y un rango de años obtiene la cantidad total de personas que llegan a esa ciudad separando por años,paises y ciudades de origen
    Dado un pais y un rango de años obtiene la cantidad total de personas que llegan a ese pais separando por años
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

    cursor, labels = repository.ObtenerPaisOrigenYNumeroTuristasAmadeusAnualmenteDadoPaisDestinoCiudadDestinoAnioMinMax(PaisDestino, CiudadDestino, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)


    ##Mostrar JSON Extendido
#    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels)
#    retval = conversor.ObtenerDataJSONExtendido(matriz)
#
#    return retval

    ##Mostrar JSON Reducido
    retval = conversor.convertirAJson(arrayTuplas)
    return retval




def obtener_cantidad_turistas_y_pais_origen_en_ciudad_en_mes_en_anio(PaisDestino, CiudadDestino, Mes, Anio): #OK
    """
    Dado un pais, una ciudad destino, un mes y un año obtiene la cantidad total de personas que llegan a esa ciudad separando por pais de origen
    Dado un pais, una ciudad destino, un mes y un año obtiene la cantidad total de personas que llegan a esa ciudad separando por pais de origen
    :param PaisDestino: Pais al que llegan los turistas
    :type PaisDestino: str
    :param CiudadDestino: Ciudad a la que llegan los turistas
    :type CiudadDestino: str
    :param Mes: Mes
    :type Mes: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerPaisOrigenYNumeroTuristasAmadeusTotalesEnUnAnioDadoPaisDestinoCiudadDestinoMesAnio(PaisDestino, CiudadDestino, Mes, Anio)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)


    ##Mostrar JSON Extendido
#    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, Anio, Anio)
#    retval = conversor.ObtenerDataJSONExtendido(matriz)
#
#    return retval

    ##Mostrar JSON Reducido
    retval = conversor.convertirAJson(arrayTuplas)
    return retval


def obtener_cantidad_turistas_y_paises_en_pais_en_anio(PaisDestino, Anio): #OK
    """
    Dado un pais y un año obtiene la cantidad total de personas que llegan a ese pais en ese año
    Dado un pais, una ciudad destino y un año obtiene la cantidad total de personas que llegan a esa ciudad separando por meses
    :param PaisDestino: Pais al que llegan los turistas
    :type PaisDestino: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerPaisOrigenYNumeroTuristasAmadeusMensualmenteEnUnAnioTotalesDadoPaisDestinoAnio(PaisDestino, Anio)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)


    ##Mostrar JSON Extendido
#    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, Anio, Anio)
#    retval = conversor.ObtenerDataJSONExtendido(matriz)
#
#    return retval

    ##Mostrar JSON Reducido
    retval = conversor.convertirAJson(arrayTuplas)
    return retval


def obtener_cantidad_turistas_y_paises_mensual_en_pais_en_anio(PaisDestino, Anio): #OK
    """
    Dado un pais y un año obtiene la cantidad total de personas que llegan a ese pais en ese año separadas por meses
    Dado un pais, una ciudad destino y un año obtiene la cantidad total de personas que llegan a esa ciudad separando por meses
    :param PaisDestino: Pais al que llegan los turistas
    :type PaisDestino: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerPaisOrigenYNumeroTuristasAmadeusMensualmenteEnUnAnioDadoPaisDestinoAnio(PaisDestino, Anio)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)


    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, Anio, Anio)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

    ##Mostrar JSON Reducido
#    retval = conversor.convertirAJson(arrayTuplas)
#    return retval
