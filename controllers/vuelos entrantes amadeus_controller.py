from ..DB.DBRepositoryAmadeus import DBRepositoryAmadeus as DBRepository
from ..Utilidades.Conversores import ConversorCursorJson as Conversor


def obtener_cantidad_total_vuelos_pais_en_ciudad_en_mes_en_anio(Pais, Ciudad, Mes, Anio):
    """
    Dado un pais, una ciudad, un mes y un año obtiene la cantidad total de vuelos que llegan a esa ciudad durante ese año y mes
    Dado un pais, una ciudad, un mes y un año obtiene la cantidad total de vuelos que llegan a esa ciudad durante ese año y mes
    :param Pais: Pais
    :type Pais: str
    :param Ciudad: Ciudad
    :type Ciudad: str
    :param Mes: Mes
    :type Mes: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.obtenercantidadtotalvuelospaisenciudadenmesenanio(Pais, Ciudad, Mes, Anio)
    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)
    retval = conversor.convertirAJson(lista)
    
    return retval



def obtener_cantidad_total_vuelos_pais_en_ciudad_mensual_en_anio(Pais, Ciudad, Anio):
    """
    Dado un pais, una ciudad y un año obtiene la cantidad total de vuelos que llegan a esa ciudad durante ese año separando por meses
    Dado un pais, una ciudad y un año obtiene la cantidad total de vuelos que llegan a esa ciudad durante ese año separando por meses
    :param Pais: Pais
    :type Pais: str
    :param Ciudad: Ciudad
    :type Ciudad: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadTotalVuelosPaisEnCiudadMensualEnAnio(Pais, Ciudad, Anio)
    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)
    retval = conversor.convertirAJson(lista)
    
    return retval



def obtener_cantidad_total_vuelos_totales_pais_en_ciudad_en_anio(Pais, Ciudad, Mes, Anio):
    """
    Dado un pais, una ciudad y un año obtiene la cantidad total de vuelos que llegan a esa ciudad durante ese año
    Dado un pais, una ciudad y un año obtiene la cantidad total de vuelos que llegan a esa ciudad durante ese año
    :param Pais: Pais
    :type Pais: str
    :param Ciudad: Ciudad
    :type Ciudad: str
    :param Mes: Mes
    :type Mes: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadTotalVuelosTotalesPaisEnCiudadEnAnio(Pais, Ciudad, Mes, Anio)
    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)
    retval = conversor.convertirAJson(lista)
    
    return retval



def obtener_cantidad_total_vuelos_totales_pais_en_mes_en_anio(Pais, Ciudad, Mes, Anio):
    """
    Dado un pais, un mes y un año obtiene la cantidad total de vuelos que llegan a ese pais durante ese año y mes
    Dado un pais, un mes y un año obtiene la cantidad total de vuelos que llegan a ese pais durante ese año y mes
    :param Pais: Pais
    :type Pais: str
    :param Ciudad: Ciudad
    :type Ciudad: str
    :param Mes: Mes
    :type Mes: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadTotalVuelosTotalesPaisEnMesEnAnio(Pais, Ciudad, Mes, Anio)
    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)
    retval = conversor.convertirAJson(lista)
    
    return retval



def obtener_cantidad_vuelos_ciudad_en_mes_en_rango_anios(Pais, Mes, AnioInicio, AnioFin):
    """
    Dado un pais, un mes y un rango de años obtiene la cantidad total de vuelos que llegan a ese pais durante ese mes y ese rango de años separando por ciudades
    Dado un pais, un mes y un rango de años obtiene la cantidad total de vuelos que llegan a ese pais durante ese mes y ese rango de años separando por ciudades
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

    cursor, labels = repository.ObtenerCantidadVuelosCiudadEnMesEnRangoAnios(Pais, Mes, AnioInicio, AnioFin)
    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)
    retval = conversor.convertirAJson(lista)
    
    return retval



def obtener_cantidad_vuelos_ciudad_pais_en_mes_en_anio(Pais, Mes, Anio):
    """
    Dado un pais, un mes y un año obtiene la cantidad total de vuelos que llegan a esa ciudad durante ese mes y ese año separando por ciudades
    Dado un pais, un mes y un año obtiene la cantidad total de vuelos que llegan a esa ciudad durante ese mes y ese año separando por ciudades
    :param Pais: Pais
    :type Pais: str
    :param Mes: Mes
    :type Mes: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerDatosVuelosEntrantesAmadeusEnUnMesEnUnAnioDadoPaisDestinoAnioSeparandoPorCiudades(Pais, Anio)
    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)
    retval = conversor.convertirAJson(lista)
    
    return retval



def obtener_cantidad_vuelos_ciudades_pais_en_anio(Pais, Anio):
    """
    Dado un pais y un año obtiene la cantidad de vuelos que llegan a ese pais durante ese año divividos por ciudades
    Dado un pais y un año obtiene la cantidad de vuelos que llegan a ese pais durante ese año divividos por ciudades
    :param Pais: Pais
    :type Pais: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadVuelosCiudadesPaisEnAnio(Pais, Anio)
    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)
    retval = conversor.convertirAJson(lista)
    
    return retval



def obtener_cantidad_vuelos_pais_en_anio(Pais, Anio):
    """
    Dado un pais y un año obtiene la cantidad de vuelos que llegan a ese pais durante ese año
    Dado un pais y un año obtiene la cantidad de vuelos que llegan a ese pais durante ese año
    :param Pais: Pais
    :type Pais: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadVuelosPaisEnAnio(Pais, Anio)
    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)
    retval = conversor.convertirAJson(lista)
    
    return retval



def obtener_cantidad_vuelos_pais_en_ciudad_en_mes_en_rango_anios(Pais, Ciudad, Mes, AnioInicio, AnioFin):
    """
    Dado un pais, una ciudad, un mes y un rango de años obtiene la cantidad total de vuelos que llegan a esa ciudad durante esos años y mes
    Dado un pais, una ciudad y un rango de años obtiene la cantidad total de vuelos que llegan a esa ciudad durante esos años separado por meses y mes
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

    cursor, labels = repository.ObtenerCantidadVuelosPaisEnCiudadEnMesEnRangoAnios(Pais, Ciudad, Mes, AnioInicio, AnioFin)
    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)
    retval = conversor.convertirAJson(lista)
    
    return retval



def obtener_cantidad_vuelos_pais_en_ciudad_en_rango_anios(Pais, Ciudad, AnioInicio, AnioFin):
    """
    Dado un pais, una ciudad y un rango de años obtiene la cantidad total de vuelos que llegan a esa ciudad durante esos años
    Dado un pais, una ciudad y un rango de años obtiene la cantidad total de vuelos que llegan a esa ciudad durante esos años
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

    cursor, labels = repository.ObtenerDatosVuelosEntrantesAmadeusDadoPaisDestinoCiudadDestinoAnioMinMax(Pais, Ciudad, AnioInicio, AnioFin)
    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)
    retval = conversor.convertirAJson(lista)
    
    return retval



def obtener_cantidad_vuelos_pais_en_ciudad_mensual_en_rango_anios(Pais, Ciudad, AnioInicio, AnioFin):
    """
    Dado un pais, una ciudad y un rango de años obtiene la cantidad total de vuelos que llegan a esa ciudad durante esos años separado por meses
    Dado un pais, una ciudad y un rango de años obtiene la cantidad total de vuelos que llegan a esa ciudad durante esos años separado por meses
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

    cursor, labels = repository.ObtenerCantidadVuelosPaisEnCiudadMensualEnRangoAnios(Pais, Ciudad, AnioInicio, AnioFin)
    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)
    retval = conversor.convertirAJson(lista)
    
    return retval



def obtener_cantidad_vuelos_pais_en_mes_en_rango_anios(Pais, Mes, AnioInicio, AnioFin):
    """
    Dado un pais, un mes y un rango de años obtiene la cantidad total de vuelos que llegan a ese pais durante esos años
    Dado un pais, un mes y un rango de años obtiene la cantidad total de vuelos que llegan a ese pais durante esos años
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

    cursor, labels = repository.ObtenerCantidadVuelosPaisEnMesEnRangoAnios(Pais, Mes, AnioInicio, AnioFin)
    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)
    retval = conversor.convertirAJson(lista)
    
    return retval



def obtener_cantidad_vuelos_pais_en_rango_anios(Pais, AnioInicio, AnioFin):
    """
    Dado un pais y un rango de años obtiene la cantidad de vuelos que llegan a ese pais diviendo por años
    Dado un pais y un rango de años obtiene la cantidad de vuelos que llegan a ese pais diviendo por años
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

    cursor, labels = repository.ObtenerCantidadVuelosPaisEnRangoAnios(Pais, AnioInicio, AnioFin)
    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)
    retval = conversor.convertirAJson(lista)
    
    return retval

