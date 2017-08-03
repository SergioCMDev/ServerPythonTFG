from ..DB.DBRepositoryAena import DBRepositoryAena as DBRepository
from ..Utilidades.Conversores import Conversores as Conversor


def obtener_cantidad_anio(PaisOrigen, Anio): #OK
    """
    Obtiene la cantidad de personas que salen de un pais en un años y devuelve la cantidad
    Obtiene la cantidad de personas que salen de un pais durante un rango de años y lo organizamos mensualmente
    :param PaisOrigen: Pais del que salen los turistas
    :type PaisOrigen: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerDatosTuristasAenaEnUnAnioDadoPaisDestinoAnio(PaisOrigen, Anio)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, Anio, Anio)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

    ##Mostrar JSON Reducido
#    retval = conversor.convertirAJson(arrayTuplas)
#    return retval


def obtener_cantidad_ciudad_destino_en_anio(PaisOrigen, CiudadOrigen, Anio): #OK
    """
    Obtiene la cantidad de personas que van hacia una ciudad durante un rango de años
    Obtiene la cantidad de personas que van hacia una ciudad durante un rango de años
    :param PaisDestino: Pais
    :type PaisDestino: str
    :param CiudadDestino: Ciudad
    :type CiudadDestino: str
    :param AnioInicio: Anio Inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int

    :rtype: None
    """

    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerDatosTuristasAenaDadoPaisDestinoCiudadDestinoAnioMinMax(PaisOrigen, CiudadOrigen, Anio, Anio )

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, Anio, Anio)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

    ##Mostrar JSON Reducido
#    retval = conversor.convertirAJson(arrayTuplas)
#    return retvaltval

def obtener_cantidad_ciudad_en_anio(PaisOrigen, CiudadOrigen, Anio): #OK
    """
    Obtiene la cantidad de personas que salen de un pais en un año y devuelve la cantidad
    Obtiene la cantidad de personas que salen de un pais durante un rango de años y lo organizamos mensualmente
    :param PaisOrigen: Pais del que salen los turistas
    :type PaisOrigen: str
    :param CiudadOrigen: Ciudad de la que salen los turistas
    :type CiudadOrigen: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """


    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerDatosTuristasAenaEnUnAnioDadoPaisDestinoCiudadDestinoAnio(PaisOrigen, CiudadOrigen, Anio)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, Anio, Anio)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

    ##Mostrar JSON Reducido
#    retval = conversor.convertirAJson(arrayTuplas)
#    return retval


def obtener_cantidad_ciudad_en_mes_en_anio(PaisOrigen, CiudadOrigen, Mes,  Anio): #OK
    """
    Obtiene la cantidad de personas que salen de una ciudad de un pais en un año durante un mismo mes y devuelve las cantidades
    Obtiene la cantidad de personas que salen de una ciudad de un pais en un año durante un mismo mes y devuelve las cantidades
    :param PaisOrigen: Pais del que salen los turistas
    :type PaisOrigen: str
    :param CiudadOrigen: Ciudad de la que salen los turistas
    :type CiudadOrigen: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerNumeroTuristasAenaDadoPaisOrigenCiudadOrigenMesAnio(PaisOrigen, CiudadOrigen,  Mes, Anio)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
#    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas, labels, Anio, Anio)
#    retval = conversor.ObtenerDataJSONExtendido(matriz)

#    return retval

    ##Mostrar JSON Reducido
    retval = conversor.convertirAJson(arrayTuplas)
    return retval





def obtener_cantidad_ciudad_en_mes_en_rango_anios(PaisOrigen, CiudadOrigen, Mes,  AnioInicio, AnioFin): #OK
    """
    Obtiene la cantidad de personas que salen de una ciudad de un pais en un rango de años durante un mismo mes y devuelve las cantidades
    Obtiene la cantidad de personas que salen de una ciudad de un pais en un rango de años durante un mismo mes y devuelve las cantidades
    :param PaisOrigen: Pais del que salen los turistas
    :type PaisOrigen: str
    :param CiudadOrigen: Ciudad de la que salen los turistas
    :type CiudadOrigen: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerDatosTuristasAenaDadoPaisCiudadMesAnioMinMax(PaisOrigen, CiudadOrigen, Mes, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

    ##Mostrar JSON Reducido
#    retval = conversor.convertirAJson(arrayTuplas)
#    return retval


def obtener_cantidad_ciudad_mensualmente_en_anio(PaisOrigen, AnioInicio, AnioFin): #OK
    """
    Obtiene la cantidad de personas que salen de un pais durante un rango de años y lo organiza mensualmente
    Obtiene la cantidad de personas que salen de un pais durante un rango de años y lo organizas mensualmente
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

    cursor, labels = repository.ObtenerDatosTuristasMensualmenteAenaDadoPaisDestinoCiudadAnio(PaisOrigen, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)
    
    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

    ##Mostrar JSON Reducido
#    retval = conversor.convertirAJson(arrayTuplas)
#    return retval

def obtener_cantidad_salientes_rango_anios(PaisOrigen, AnioInicio, AnioFin): #OK
    """
    Obtiene la cantidad de personas que salen de un pais durante un rango de años y lo organiza anualmente
    Obtiene la cantidad de personas que salen de un pais durante un rango de años y lo organizas mensualmente
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

    cursor, labels = repository.ObtenerNumeroTuristasAenaDadoPaisDestinoAnioMinMax(PaisOrigen, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)
    
    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

    ##Mostrar JSON Reducido
#    retval = conversor.convertirAJson(arrayTuplas)
#    return retval
