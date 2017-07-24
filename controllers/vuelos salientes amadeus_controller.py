from ..DB.DBRepositoryAmadeus import DBRepositoryAmadeus as DBRepository
from ..Utilidades.Conversores import ConversorCursorJson as Conversor


def obtener_cantidad_anual(Pais, AnioInicio, AnioFin): ##eee
    """
    Dado un pais origen obtiene la cantidad de vuelos que salen de dicho pais durante un rango de años
    Dado un pais origen obtiene la cantidad de vuelos que salen de dicho pais durante un rango de años
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

    cursor, labels = repository.ObtenerDatosVuelosSalientesAmadeusAnualmenteDadoPaisOrigenAnioMinMax(Pais, AnioInicio, AnioFin)

    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)

    retval = conversor.convertirAJson(lista)
    return retval


def obtener_cantidad_ciudad_mensual_rango_anios(Pais, Ciudad, AnioInicio, AnioFin): ##€ee
    """
    Dado un pais origen y una ciudad origen obtiene la cantidad de vuelos que salen de dicha ciudad durante un rango de años organzido mensualmente
    Dado un pais origen y una ciudad origen obtiene la cantidad de vuelos que salen de dicha ciudad durante un rango de años organzido mensualmente
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

    cursor, labels = repository.ObtenerCantidadCiudadMensualRangoAnios(Pais, Ciudad, AnioInicio, AnioFin)

    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)

    retval = conversor.convertirAJson(lista)
    return retval


def obtener_cantidad_ciudad_mes_rango_anios(Pais, Ciudad, Mes, AnioInicio, AnioFin): ##ee
    """
    Dado un pais origen y una ciudad origen obtiene la cantidad de vuelos que salen de dicha ciudad durante un rango de años durante un mes
    Dado un pais origen y una ciudad origen obtiene la cantidad de vuelos que salen de dicha ciudad durante un rango de años durante un mes
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

    cursor, labels = repository.ObtenerCantidadCiudadMesRangoAnios(Pais, Ciudad, Mes, AnioInicio, AnioFin)

    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)

    retval = conversor.convertirAJson(lista)
    return retval


def obtener_cantidad_ciudades_mensual_rango_anios(Pais, AnioInicio, AnioFin): ##ee
    """
    Dado un pais origen obtiene la cantidad de vuelos que salen de dicho pais y las ciudades hacia las que se dirigen durante un rango de años diviendo por meses
    Dado un pais origen obtiene la cantidad de vuelos que salen de dicho pais y las ciudades hacia las que se dirigen durante un rango de años diviendo por meses
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

    cursor, labels = repository.ObtenerDatosVuelosSalientesAmadeusDadoPaisOrigenAnioMinMaxSeparadoPorCiudadesMensualmente(Pais, AnioInicio, AnioFin)

    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)

    retval = conversor.convertirAJson(lista)
    return retval


def obtener_cantidad_ciudades_rango_anios(Pais, AnioInicio, AnioFin): ##eee
    """
    Dado un pais origen obtiene la cantidad de vuelos que salen de dicho pais y las ciudades hacia las que se dirigen durante un rango de años
    Dado un pais origen obtiene la cantidad de vuelos que salen de dicho pais y las ciudades hacia las que se dirigen durante un rango de años
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

    cursor, labels = repository.ObtenerDatosVuelosSalientesAmadeusDadoPaisOrigenAnioMinMaxSeparadoPorCiudades(Pais, AnioInicio, AnioFin)

    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)

    retval = conversor.convertirAJson(lista)
    return retval

def obtener_cantidad_mensualmente_en_anio(Pais, Anio): ##eee
    """
    Dado un pais origen y un anio obtiene la cantidad de vuelos que salen de dicho pais durante ese año de forma mensual
    Dado un pais origen y un anio obtiene la cantidad de vuelos que salen de dicho pais durante ese año de forma mensual
    :param Pais: Pais
    :type Pais: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerDatosVuelosSalientesAmadeusEnUnAnioDadoPaisOrigenAnioMensualmente(Pais, Anio)

    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)

    retval = conversor.convertirAJson(lista)
    return retval

def obtener_cantidad_mes_en_anios(Pais, Mes, AnioInicio, AnioFin): ##eee
    """
    Dado un pais origen, un mes y un rango de años obtiene la cantidad de vuelos salientes durante ese rango de años en ese mes
    Dado un pais origen, un mes y un rango de años obtiene la cantidad de vuelos salientes durante ese rango de años en ese mes
    :param Pais: Pais
    :type Pais: str
    :param Mes: Mes
    :type Mes: str
    :param Anio_Inicio: AnioInicio
    :type Anio_Inicio: int
    :param AnioFin: AnioFin
    :type AnioFin: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerDatosVuelosSalientesAmadeusAnualmenteEnUnMesDadoPaisOrigenMesAnioMinMax(Pais, Mes, AnioInicio, AnioFin)

    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)

    retval = conversor.convertirAJson(lista)
    return retval


def obtener_cantidad_vuelos_salienes_ciudades_en_anio(Pais, Anio): ##ee
    """
    Dado un pais origen y un anio obtiene la cantidad de vuelos que salen de dicho pais durante ese año dividiendo por ciudades
    Dado un pais origen y un anio obtiene la cantidad de vuelos que salen de dicho pais durante ese año dividiendo por ciudades
    :param Pais: Pais
    :type Pais: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerDatosVuelosSalientesAmadeusEnUnAnioDadoPaisOrigenAnioSeparandoPorCiudades(Pais, Anio)

    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)

    retval = conversor.convertirAJson(lista)
    return retval


def obtener_cantidad_vuelos_salientes_ciudad_rango_anios(Pais, Ciudad, AnioInicio, AnioFin):
    """
    Dado un pais origen y una ciudad origen obtiene la cantidad de vuelos que salen de dicha ciudad durante un rango de años
    Dado un pais origen y una ciudad origen obtiene la cantidad de vuelos que salen de dicha ciudad durante un rango de años
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

    cursor, labels = repository.ObtenerDatosVuelosSalientesAmadeusDadoPaisOrigenCiudadOrigenAnioMinMax(Pais, Ciudad, AnioInicio, AnioFin)

    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)

    retval = conversor.convertirAJson(lista)
    return retval
