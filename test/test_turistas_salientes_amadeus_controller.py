# coding: utf-8

from __future__ import absolute_import

from . import BaseTestCase
from six import BytesIO
from flask import json


class TestTuristasSalientesAmadeusController(BaseTestCase):
    """ TuristasSalientesAmadeusController integration test stubs """

    def test_obtener_cantidad_ciudad_durante_mes_en_rango_anios(self):
        """
        Test case for obtener_cantidad_ciudad_durante_mes_en_rango_anios

        Dado un pais origen, una ciudad, un mes y un rango de años obtiene la cantidad de turistas salientes de ese pais diviendo por meses y años
        """
        query_string = [('Mes', 'Enero'),
                        ('CiudadOrigen', 'Valencia'),
                        ('AnioInicio', 2009),
                        ('AnioFin', 2015)]
        response = self.client.open('/server/Amadeus/TuristasSalientes/ObtenerCantidadCiudadDuranteMesEnRangoAnios/{PaisOrigen}'.format(PaisOrigen='PaisOrigen_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_en_ciudad_en_rango_anios(self):
        """
        Test case for obtener_cantidad_en_ciudad_en_rango_anios

        Dado un pais origen, una ciudad y un rango de años obtiene la cantidad de turistas que salen de ese pais durante ese rango de años de esa ciudad
        """
        query_string = [('CiudadOrigen', 'Valencia'),
                        ('AnioInicio', 2009),
                        ('AnioFin', 2015)]
        response = self.client.open('/server/Amadeus/TuristasSalientes/ObtenerCantidadEnCiudadEnRangoAnios/{PaisOrigen}'.format(PaisOrigen='PaisOrigen_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_en_ciudades_mensualmente_en_anio(self):
        """
        Test case for obtener_cantidad_en_ciudades_mensualmente_en_anio

        Dado un pais origen y un rango de años obtiene la cantidad de turistas salientes de ese pais durante esos años divididos por ciudad y mes
        """
        query_string = [('AnioInicio', 2009),
                        ('AnioFin', 2015)]
        response = self.client.open('/server/Amadeus/TuristasSalientes/ObtenerCantidadEnCiudadesMensualmenteEnAnio/{PaisOrigen}'.format(PaisOrigen='PaisOrigen_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_en_pais_en_anio(self):
        """
        Test case for obtener_cantidad_en_pais_en_anio

        Dado un pais origen y un anio obtiene la cantidad de turistas que salen de dicho pais durante ese año
        """
        query_string = [('Anio', 2009)]
        response = self.client.open('/server/Amadeus/TuristasSalientes/ObtenerCantidadEnPaisEnAnio/{PaisOrigen}'.format(PaisOrigen='PaisOrigen_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_en_pais_en_anio_mensualmente(self):
        """
        Test case for obtener_cantidad_en_pais_en_anio_mensualmente

        Dado un pais origen y un año obtiene la cantidad de turistas salientes de ese pais durante ese año dividido por meses
        """
        query_string = [('Anio', 2009)]
        response = self.client.open('/server/Amadeus/TuristasSalientes/ObtenerCantidadEnPaisEnAnioMensualmente/{PaisOrigen}'.format(PaisOrigen='PaisOrigen_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_en_pais_en_ciudades_en_anio(self):
        """
        Test case for obtener_cantidad_en_pais_en_ciudades_en_anio

        Dado un pais origen y un año obtiene la cantidad de turistas salientes de ese pais durante ese año dividido por ciudades origen
        """
        query_string = [('Anio', 2009)]
        response = self.client.open('/server/Amadeus/TuristasSalientes/ObtenerCantidadEnPaisEnCiudadesEnAnio/{PaisOrigen}'.format(PaisOrigen='PaisOrigen_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_en_pais_en_mes_en_rango_anios(self):
        """
        Test case for obtener_cantidad_en_pais_en_mes_en_rango_anios

        Dado un pais origen, un mes y un rango de años obtiene la cantidad de turistas salientes de ese pais durante esos años y ese mes
        """
        query_string = [('Mes', 'Enero'),
                        ('AnioInicio', 2009),
                        ('AnioFin', 2015)]
        response = self.client.open('/server/Amadeus/TuristasSalientes/ObtenerCantidadEnPaisEnMesEnRangoAnios/{PaisOrigen}'.format(PaisOrigen='PaisOrigen_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_en_pais_en_rango_anios(self):
        """
        Test case for obtener_cantidad_en_pais_en_rango_anios

        Dado un pais origen y un rango de años obtiene la cantidad de turistas salientes de ese pais durante esos años
        """
        query_string = [('AnioInicio', 2009),
                        ('AnioFin', 2015)]
        response = self.client.open('/server/Amadeus/TuristasSalientes/ObtenerCantidadEnPaisEnRangoAnios/{PaisOrigen}'.format(PaisOrigen='PaisOrigen_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
