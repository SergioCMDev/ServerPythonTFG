from ..DB.DBRepositoryAmadeus import DBRepositoryAmadeus as DBRepository
from ..Utilidades.Conversores import Conversores as Conversor



def obtener_cantidad_anual(PaisOrigen, AnioInicio, AnioFin): #OK
    """
    Dado un pais origen obtiene la cantidad de vuelos que salen de dicho pais durante un rango de años
    Dado un pais origen obtiene la cantidad de vuelos que salen de dicho pais durante un rango de años
    :param PaisOrigen: Pais del que salen los vuelos
    :type PaisOrigen: str
    :param AnioInicio: Anio Inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerDatosVuelosSalientesAmadeusAnualmenteDadoPaisOrigenAnioMinMax(PaisOrigen, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)


    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas, labels)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

    ##Mostrar JSON Reducido
#    retval = conversor.convertirAJson(arrayTuplas)
#    return retval



def obtener_cantidad_ciudad_mensual_rango_anios(PaisOrigen, CiudadOrigen, AnioInicio, AnioFin): #OK
    """
    Dado un pais origen y una ciudad origen obtiene la cantidad de vuelos que salen de dicha ciudad durante un rango de años organizado mensualmente
    Dado un pais origen y una ciudad origen obtiene la cantidad de vuelos que salen de dicha ciudad durante un rango de años organizado mensualmente
    :param PaisOrigen: Pais del que salen los vuelos
    :type PaisOrigen: str
    :param CiudadOrigen: Ciudad de la que salen los vuelos
    :type CiudadOrigen: str
    :param AnioInicio: Anio Inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerDatosVuelosSalientesAmadeusMensualmenteDadoPaisOrigenCiudadOrigenAnioMinMax(PaisOrigen, CiudadOrigen, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

#    print(arrayTuplas)
    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas, labels)
#    print(arrayTuplas)

    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

    ##Mostrar JSON Reducido
#    retval = conversor.convertirAJson(arrayTuplas)
#    return retval



def obtener_cantidad_ciudad_mes_rango_anios(PaisOrigen, CiudadOrigen, Mes, AnioInicio, AnioFin): #OK
    """
    Dado un pais origen y una ciudad origen obtiene la cantidad de vuelos que salen de dicha ciudad durante un rango de años durante un mes
    Dado un pais origen y una ciudad origen obtiene la cantidad de vuelos que salen de dicha ciudad durante un rango de años durante un mes
    :param PaisOrigen: Pais del que salen los vuelos
    :type PaisOrigen: str
    :param CiudadOrigen: Ciudad de la que salen los vuelos
    :type CiudadOrigen: str
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

    cursor, labels = repository.ObtenerDatosVuelosSalientesAmadeusEnUnMesDadoPaisOrigenCiudadOrigenMesAnioMinMax(PaisOrigen, CiudadOrigen, Mes, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)


    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas, labels)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

    ##Mostrar JSON Reducido
#    retval = conversor.convertirAJson(arrayTuplas)
#    return retval



def obtener_cantidad_ciudades_mensual_rango_anios(PaisOrigen, AnioInicio, AnioFin): #OK
    """
    Dado un pais origen obtiene la cantidad de vuelos que salen de dicho pais y las ciudades hacia las que se dirigen durante un rango de años diviendo por meses
    Dado un pais origen obtiene la cantidad de vuelos que salen de dicho pais y las ciudades hacia las que se dirigen durante un rango de años diviendo por meses
    :param PaisOrigen: Pais del que salen los vuelos
    :type PaisOrigen: str
    :param AnioInicio: Anio Inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerDatosVuelosSalientesAmadeusDadoPaisOrigenAnioMinMaxSeparadoPorCiudadesMensualmente(PaisOrigen, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)


    ##Mostrar JSON Extendido
#    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas, labels)
#    retval = conversor.ObtenerDataJSONExtendido(matriz)
#
#    return retval

    ##Mostrar JSON Reducido
    retval = conversor.convertirAJson(arrayTuplas)
    return retval



def obtener_cantidad_ciudades_rango_anios(PaisOrigen, AnioInicio, AnioFin): #OK
    """
    Dado un pais origen obtiene la cantidad de vuelos que salen de dicho pais y las ciudades hacia las que se dirigen durante un rango de años
    Dado un pais origen obtiene la cantidad de vuelos que salen de dicho pais y las ciudades hacia las que se dirigen durante un rango de años
    :param PaisOrigen: Pais del que salen los vuelos
    :type PaisOrigen: str
    :param AnioInicio: Anio Inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerDatosVuelosSalientesAmadeusDadoPaisOrigenAnioMinMaxSeparadoPorCiudades(PaisOrigen, AnioInicio, AnioFin)
    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
#    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas, labels)
#    retval = conversor.ObtenerDataJSONExtendido(matriz)
#
#    return retval

    ##Mostrar JSON Reducido
    retval = conversor.convertirAJson(arrayTuplas)
    return retval


def obtener_cantidad_mensualmente_en_anio(PaisOrigen, Anio): #OK
    """
    Dado un pais origen y un anio obtiene la cantidad de vuelos que salen de dicho pais durante ese año de forma mensual
    Dado un pais origen y un anio obtiene la cantidad de vuelos que salen de dicho pais durante ese año de forma mensual
    :param PaisOrigen: Pais del que salen los vuelos
    :type PaisOrigen: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerDatosVuelosSalientesAmadeusEnUnAnioDadoPaisOrigenAnioMensualmente(PaisOrigen, Anio)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)


    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas, labels)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

    ##Mostrar JSON Reducido
#    retval = conversor.convertirAJson(arrayTuplas)
#    return retval


def obtener_cantidad_mes_en_rango_anios(PaisOrigen, Mes, AnioInicio, AnioFin): #OK
    """
    Dado un pais origen, un mes y un rango de años obtiene la cantidad de vuelos salientes durante ese rango de años en ese mes
    Dado un pais origen, un mes y un rango de años obtiene la cantidad de vuelos salientes durante ese rango de años en ese mes
    :param PaisOrigen: Pais del que salen los vuelos
    :type PaisOrigen: str
    :param Mes: Mes
    :type Mes: str
    :param AnioInicio: Anio Inicio
    :type AnioInicio: int
    :param AnioFin: AnioFin
    :type AnioFin: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerDatosVuelosSalientesAmadeusAnualmenteEnUnMesDadoPaisOrigenMesAnioMinMax(PaisOrigen, Mes, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)


    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas, labels)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

    ##Mostrar JSON Reducido
#    retval = conversor.convertirAJson(arrayTuplas)
#    return retval



def obtener_cantidad_vuelos_salientes_ciudades_en_anio(PaisOrigen, Anio): #OK
    """
    Dado un pais origen y un anio obtiene la cantidad de vuelos que salen de dicho pais durante ese año dividiendo por ciudades
    Dado un pais origen y un anio obtiene la cantidad de vuelos que salen de dicho pais durante ese año dividiendo por ciudades
    :param PaisOrigen: Pais del que salen los vuelos
    :type PaisOrigen: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerDatosVuelosSalientesAmadeusEnUnAnioDadoPaisOrigenAnioSeparandoPorCiudades(PaisOrigen, Anio)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)


    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas, labels)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

    ##Mostrar JSON Reducido
#    retval = conversor.convertirAJson(arrayTuplas)
#    return retval



def obtener_cantidad_vuelos_salientes_ciudad_rango_anios(PaisOrigen, CiudadOrigen, AnioInicio, AnioFin): #OK
    """
    Dado un pais origen y una ciudad origen obtiene la cantidad de vuelos que salen de dicha ciudad durante un rango de años
    Dado un pais origen y una ciudad origen obtiene la cantidad de vuelos que salen de dicha ciudad durante un rango de años
    :param PaisOrigen: Pais del que salen los vuelos
    :type PaisOrigen: str
    :param CiudadOrigen: Ciudad de la que salen los vuelos
    :type CiudadOrigen: str
    :param AnioInicio: Anio Inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerDatosVuelosSalientesAmadeusDadoPaisOrigenCiudadOrigenAnioMinMax(PaisOrigen, CiudadOrigen, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)


    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas, labels)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

    ##Mostrar JSON Reducido
#    retval = conversor.convertirAJson(arrayTuplas)
#    return retval

