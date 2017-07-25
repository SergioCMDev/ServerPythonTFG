from ..DB.DBRepositoryAena import DBRepositoryAena as DBRepository
from ..Utilidades.Conversores import Conversores as Conversor


def obtener_cantidad_anio(PaisOrigen, Anio):
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


    retval = conversor.convertirAJson(arrayTuplas)
    return retval


def obtener_cantidad_ciudad_en_anio(PaisOrigen, CiudadOrigen, Anio):
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


    retval = conversor.convertirAJson(arrayTuplas)
    return retval

def obtener_cantidad_ciudad_rango_anios(PaisDestino, CiudadDestino, AnioInicio, AnioFin):
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

    cursor, labels = repository.ObtenerDatosTuristasAenaDadoPaisDestinoCiudadDestinoAnioMinMax(PaisDestino, CiudadDestino, AnioInicio, AnioFin )

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)


    retval = conversor.convertirAJson(arrayTuplas)
    return retval



def obtener_cantidad_salientes_rango_anios(PaisOrigen, AnioInicio, AnioFin):
    """
    Obtiene la cantidad de personas que salen de un pais durante un rango de años y lo organizas anualmente
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


    retval = conversor.convertirAJson(arrayTuplas)
    return retval
