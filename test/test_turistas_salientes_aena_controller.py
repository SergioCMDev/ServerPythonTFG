# coding: utf-8

from __future__ import absolute_import

from . import BaseTestCase
from six import BytesIO
from flask import json


class TestTuristasSalientesAenaController(BaseTestCase):
    """ TuristasSalientesAenaController integration test stubs """

    def test_obtener_cantidad_anio(self):
        """
        Test case for obtener_cantidad_anio

        Obtiene la cantidad de personas que salen de un pais en un años y devuelve la cantidad
        """
        query_string = [('Anio', 789)]
        response = self.client.open('/server/Aena/TuristasSalientes/ObtenerCantidadAnio/{Pais}'.format(Pais='Pais_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_ciudad_en_anio(self):
        """
        Test case for obtener_cantidad_ciudad_en_anio

        Obtiene la cantidad de personas que salen de un pais en un años y devuelve la cantidad
        """
        query_string = [('Ciudad', 'Ciudad_example'),
                        ('Anio', 789)]
        response = self.client.open('/server/Aena/TuristasSalientes/ObtenerCantidadCiudadEnAnio/{Pais}'.format(Pais='Pais_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_ciudad_rango_anios(self):
        """
        Test case for obtener_cantidad_ciudad_rango_anios

        Obtiene la cantidad de personas que van hacia una ciudad durante un rango de años
        """
        query_string = [('Ciudad', 'Ciudad_example'),
                        ('AnioInicio', 789),
                        ('AnioFin', 789)]
        response = self.client.open('/server/Aena/TuristasSalientes/ObtenerCantidadCiudadRangoAnios/{Pais}'.format(Pais='Pais_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_salientes_rango_anios(self):
        """
        Test case for obtener_cantidad_salientes_rango_anios

        Obtiene la cantidad de personas que salen de un pais durante un rango de años y lo organizas anualmente
        """
        query_string = [('AnioInicio', 789),
                        ('AnioFin', 789)]
        response = self.client.open('/server/Aena/TuristasSalientes/ObtenerCantidadSalientesRangoAnios/{Pais}'.format(Pais='Pais_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
