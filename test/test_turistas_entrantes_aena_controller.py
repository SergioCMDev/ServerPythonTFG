# coding: utf-8

from __future__ import absolute_import

from . import BaseTestCase
from six import BytesIO
from flask import json


class TestTuristasEntrantesAenaController(BaseTestCase):
    """ TuristasEntrantesAenaController integration test stubs """

    def test_obtener_cantidad_entrantes_rango_anios(self):
        """
        Test case for obtener_cantidad_entrantes_rango_anios

        Dado un pais destino obtiene la cantidad de personas que viajan hacia el organizado por años
        """
        query_string = [('AnioInicio', 789),
                        ('AnioFin', 789)]
        response = self.client.open('/server/Aena/TuristasEntrantes/ObtenerCantidadEntrantesRangoAnios/{Pais}'.format(Pais='Pais_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_origen_rango_anios(self):
        """
        Test case for obtener_cantidad_origen_rango_anios

        Dado un pais destino obtiene la cantidad de personas que viajan hacia el y sus localizaciones organizado por años
        """
        query_string = [('AnioInicio', 789),
                        ('AnioFin', 789)]
        response = self.client.open('/server/Aena/TuristasEntrantes/ObtenerCantidadOrigenRangoAnios/{Pais}'.format(Pais='Pais_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_origen_rango_anios_meses(self):
        """
        Test case for obtener_cantidad_origen_rango_anios_meses

        Dado un pais destino obtiene la cantidad de personas que viajan hacia el y sus localizaciones organizado por años y meses
        """
        query_string = [('AnioInicio', 789),
                        ('AnioFin', 789)]
        response = self.client.open('/server/Aena/TuristasEntrantes/ObtenerCantidadOrigenRangoAniosMeses/{Pais}'.format(Pais='Pais_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_rango_anios_meses(self):
        """
        Test case for obtener_cantidad_rango_anios_meses

        Dado un pais destino obtiene la cantidad de personas que viajan hacia el organizado por años
        """
        query_string = [('AnioInicio', 789),
                        ('AnioFin', 789)]
        response = self.client.open('/server/Aena/TuristasEntrantes/ObtenerCantidadRangoAniosMeses/{Pais}'.format(Pais='Pais_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
