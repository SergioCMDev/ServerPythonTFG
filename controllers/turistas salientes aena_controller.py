from ..DB.DBRepositoryAmadeus import DBRepositoryAmadeus as DBRepository
from ..Utilidades.Conversores import ConversorCursorJson as Conversor


def obtener_cantidad_anio(Pais, Anio):
    """
    Obtiene la cantidad de personas que salen de un pais en un años y devuelve la cantidad
    Obtiene la cantidad de personas que salen de un pais durante un rango de años y lo organizamos mensualmente
    :param Pais: Pais
    :type Pais: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerDatosTuristasAenaEnUnAnioDadoPaisDestinoAnio(Pais, Anio)

    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)

    retval = conversor.convertirAJson(lista)
    return retval


def obtener_cantidad_ciudad_en_anio(Pais, Ciudad, Anio):
    """
    Obtiene la cantidad de personas que salen de un pais en un años y devuelve la cantidad
    Obtiene la cantidad de personas que salen de un pais durante un rango de años y lo organizamos mensualmente
    :param Pais: Pais
    :type Pais: str
    :param Ciudad: Ciudad
    :type Ciudad: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    return 'do some magic!'



    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerDatosTuristasAenaEnUnAnioDadoPaisDestinoCiudadDestinoAnio(Pais, Ciudad, Anio)

    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)

    retval = conversor.convertirAJson(lista)
    return retval

def obtener_cantidad_ciudad_rango_anios(Pais, Ciudad, AnioInicio, AnioFin):
    """
    Obtiene la cantidad de personas que van hacia una ciudad durante un rango de años
    Obtiene la cantidad de personas que van hacia una ciudad durante un rango de años
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

    cursor, labels = repository.ObtenerDatosTuristasAenaDadoPaisDestinoCiudadDestinoAnioMinMax(Pais, Ciudad, AnioInicio, AnioFin )

    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)

    retval = conversor.convertirAJson(lista)
    return retval


def obtener_cantidad_salientes_rango_anios(Pais, AnioInicio, AnioFin):
    """
    Obtiene la cantidad de personas que salen de un pais durante un rango de años y lo organizas anualmente
    Obtiene la cantidad de personas que salen de un pais durante un rango de años y lo organizas anualmente
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

    cursor, labels = repository.ObtenerNumeroTuristasAenaDadoPaisDestinoAnioMinMax(Pais, AnioInicio, AnioFin)

    lista =  conversor.ConvertirCursorToTuplas(cursor, labels)

    retval = conversor.convertirAJson(lista)
    return retval
