from ..DB.DBRepositoryAmadeus import DBRepositoryAmadeus as DBRepository
from ..Utilidades.Conversores import ConversorCursorJson as Conversor

def obtener_cantidad_turistas_en_ciudades_mensual_en_rango_anios(Pais, AnioInicio, AnioFin):
    """
    Dado un pais y un rango de años obtiene la cantidad total de personas que llegan a ese pais separando por ciudades, meses y años
    Dado un pais y un rango de años obtiene la cantidad total de personas que llegan a ese pais separando por ciudades, meses y años
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

    cursor, labels = repository.ObtenerPaisOrigenYNumeroTuristasAmadeusAnualmenteDadoPaisDestinoAnioMinMaxSeparadoPorCiudadesYMeses(Pais, AnioInicio, AnioFin)

    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)

    retval = conversor.convertirAJson(lista)
    return retval


def obtener_cantidad_turistas_en_pais_en_rango_anios(Pais, AnioInicio, AnioFin):
    """
    Dado un pais y un rango de años obtiene la cantidad total de personas que llegan a ese pais separando por años
    Dado un pais y un rango de años obtiene la cantidad total de personas que llegan a ese pais separando por años
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

    cursor, labels = repository.ObtenerNumeroTuristasAmadeusAnualmenteDadoPaisDestinoAnioMinMax(Pais, AnioInicio, AnioFin)

    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)

    retval = conversor.convertirAJson(lista)
    return retval


def obtener_cantidad_turistas_y_ciudades_origen_en_ciudad_en_mes_en_rango_anios(Pais, Ciudad, Mes, AnioInicio, AnioFin):
    """
    Dado un pais, una ciudad, un mes y un rango de años obtiene la cantidad total de personas que llegan a esa ciudad separando por años,paises y ciudades de origen
    Dado un pais, una ciudad, un mes y un rango de años obtiene la cantidad total de personas que llegan a esa ciudad separando por años,paises y ciudades de origen
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

    cursor, labels = repository.ObtenerPaisOrigenYNumeroTuristasAmadeusAnualmenteDadoPaisDestinoCiudadDestinoMesAnioMinMax(Pais, Ciudad, Mes, AnioInicio, AnioFin)

    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)

    retval = conversor.convertirAJson(lista)
    return retval



def obtener_cantidad_turistas_y_ciudades_origen_en_ciudad_en_rango_anios(Pais, AnioInicio, AnioFin):
    """
    Dado un pais y un rango de años obtiene la cantidad total de personas que llegan a esa ciudad separando por años, paises y ciudades de origen
    Dado un pais, una ciudad, un mes y un rango de años obtiene la cantidad total de personas que llegan a esa ciudad separando por años,paises y ciudades de origen
    :param Pais: Pais
    :type Pais: str
    :param AnioInicio: Anio Inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int
ObtenerPaisOrigenYNumeroTuristasAmadeusSeparadoPorCiudadesAnualmenteDadoPaisDestinoAnioMinMax
    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerPaisOrigenYNumeroTuristasAmadeusSeparadoPorCiudadesAnualmenteDadoPaisDestinoAnioMinMax(Pais, AnioInicio, AnioFin)

    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)

    retval = conversor.convertirAJson(lista)
    return retval


def obtener_cantidad_turistas_y_ciudades_origen_en_pais_en_rango_anios(Pais, Ciudad, AnioInicio, AnioFin):
    """
    Dado un pais, una ciudad y un rango de años obtiene la cantidad total de personas que llegan a esa ciudad separando por años,paises y ciudades de origen
    Dado un pais y un rango de años obtiene la cantidad total de personas que llegan a ese pais separando por años
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

    cursor, labels = repository.ObtenerPaisOrigenYNumeroTuristasAmadeusAnualmenteDadoPaisDestinoCiudadDestinoAnioMinMax(Pais, Ciudad, AnioInicio, AnioFin)

    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)

    retval = conversor.convertirAJson(lista)
    return retval




def obtener_cantidad_turistas_y_pais_origen_en_ciudad_en_mes_en_anio(Pais, Ciudad, Mes, Anio):
    """
    Dado un pais, una ciudad destino, un mes y un año obtiene la cantidad total de personas que llegan a esa ciudad separando por pais de origen
    Dado un pais, una ciudad destino, un mes y un año obtiene la cantidad total de personas que llegan a esa ciudad separando por pais de origen
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

    cursor, labels = repository.ObtenerPaisOrigenYNumeroTuristasAmadeusTotalesEnUnAnioDadoPaisDestinoCiudadDestinoMesAnio(Pais, Ciudad, Mes, Anio)

    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)

    retval = conversor.convertirAJson(lista)
    return retval



def obtener_cantidad_turistas_y_paises_enpais_en_anio(Pais, Mes):
    """
    Dado un pais y un año obtiene la cantidad total de personas que llegan a ese pais en ese año
    Dado un pais, una ciudad destino y un año obtiene la cantidad total de personas que llegan a esa ciudad separando por meses
    :param Pais: Pais
    :type Pais: str
    :param Mes: Anio
    :type Mes: str

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerPaisOrigenYNumeroTuristasAmadeusMensualmenteEnUnAnioTotalesDadoPaisDestinoAnio(Pais, Mes)

    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)

    retval = conversor.convertirAJson(lista)
    return retval


def obtener_cantidad_turistas_y_paises_mensual_en_pais_en_anio(Pais, Mes): ##curl -X GET "http://127.0.0.1:8080/server/Amadeus/TuristasEntrantes/ObtenerCantidadTuristasYPaisesEnPaisEnAnio/Belgium?Mes=Enero" -H "accept: application/xml"
    """
    Dado un pais y un año obtiene la cantidad total de personas que llegan a ese pais en ese año separadas por meses
    Dado un pais, una ciudad destino y un año obtiene la cantidad total de personas que llegan a esa ciudad separando por meses
    :param Pais: Pais
    :type Pais: str
    :param Mes: Mes
    :type Mes: str

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadTuristasYPaisesMensualEnpaisEnAnio(Pais, Mes)

    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)

    retval = conversor.convertirAJson(lista)
    return retval
