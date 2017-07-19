# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 15:10:19 2017

@author: wesrok
"""
from decimal import Decimal
#import simplejson as json
import json


class ConversorCursorJson:   
    def __init__(self):
        print("Clase Conversores Cargada Correctamente ")
        
    @staticmethod
    def default(obj):
        if isinstance(obj, Decimal):
            return str(obj)
        raise TypeError
        
    @staticmethod
    def convertirAJson(self, cursor):
#        retval =  json.dumps(cursor, use_decimal = True)
        retval =  json.dumps(cursor, default=self.default)

        return retval 

class DecimalEncoder(json.JSONEncoder):
    def _iterencode(self, obj, markers=None):
         if isinstance(obj, Decimal):
            return str(obj)
         raise TypeError