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
        query_string = [('Anio', 2009)]
        response = self.client.open('/server/Aena/TuristasSalientes/ObtenerCantidadAnio/{PaisOrigen}'.format(PaisOrigen='PaisOrigen_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_ciudad_en_anio(self):
        """
        Test case for obtener_cantidad_ciudad_en_anio

        Obtiene la cantidad de personas que salen de un pais en un año y devuelve la cantidad
        """
        query_string = [('CiudadOrigen', 'Valencia'),
                        ('Anio', 2009)]
        response = self.client.open('/server/Aena/TuristasSalientes/ObtenerCantidadCiudadEnAnio/{PaisOrigen}'.format(PaisOrigen='PaisOrigen_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_salientes_rango_anios(self):
        """
        Test case for obtener_cantidad_salientes_rango_anios

        Obtiene la cantidad de personas que salen de un pais durante un rango de años y lo organizas anualmente
        """
        query_string = [('AnioInicio', 2009),
                        ('AnioFin', 2015)]
        response = self.client.open('/server/Aena/TuristasSalientes/ObtenerCantidadSalientesRangoAnios/{PaisOrigen}'.format(PaisOrigen='PaisOrigen_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

     def test_obtener_cantidad_ciudad_destino_rango_anios(self):
        """
        Test case for obtener_cantidad_ciudad_destino_rango_anios

        Obtiene la cantidad de personas que salen de un pais en un año y devuelve la cantidad
        """
        query_string = [('CiudadOrigen', 'Valencia'),
                        ('Anio', 2009)]
        response = self.client.open('/server/Aena/TuristasSalientes/ObtenerCantidadCiudadDestinoRangoAnios/{PaisOrigen}'.format(PaisOrigen='PaisOrigen_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))
if __name__ == '__main__':
    import unittest
    unittest.main()
