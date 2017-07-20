#import connexion
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
from ..DB.DBRepository import DBRepository as DBRepository
from ..Utilidades.Conversores import ConversorCursorJson as Conversor
import mysql.connector



def find_quantity_by_country_origin(countryOrigin, StartingYear, FinalYear):
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerDatosVuelosEntrantesAenaDadoPaisDestinoAnioMinMax(countryOrigin, StartingYear, FinalYear)

    lista =  conversor.ConvertirCursorToTuplasAnioCantidad(cursor)

    retval = conversor.convertirAJson(lista)
    """
    Finds Incomingflights by Country Origin
    Fin number Of Tourist given a country of origin
    :param countryOrigin: Status values that need to be considered for filter
    :type countryOrigin: int
    :param StartingYear: Starting Year
    :type StartingYear: int
    :param FinalYear: Final Year
    :type FinalYear: int

    :rtype: Dict[str, int]
    """
#    return retval
    return retval
