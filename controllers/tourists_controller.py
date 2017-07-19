import connexion
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def find_by_country_origin(countryOrigin):
    """
    Finds Tourists by Country Origin
    Fin number Of Tourist given a country of origin
    :param countryOrigin: Status values that need to be considered for filter
    :type countryOrigin: str

    :rtype: int
    """
    return 121
