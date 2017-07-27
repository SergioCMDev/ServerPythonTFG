# coding: utf-8

from __future__ import absolute_import

from . import BaseTestCase
from six import BytesIO
from flask import json


class TestVuelosEntrantesAmadeusController(BaseTestCase):
    """ VuelosEntrantesAmadeusController integration test stubs """

    def test_obtener_cantidad_total_vuelos_pais_en_ciudad_en_mes_en_anio(self):
        """
        Test case for obtener_cantidad_total_vuelos_pais_en_ciudad_en_mes_en_anio

        Dado un pais, una ciudad, un mes y un año obtiene la cantidad total de vuelos que llegan a esa ciudad durante ese año y mes
        """
        query_string = [('CiudadDestino', 'Valencia'),
                        ('Mes', 'Enero'),
                        ('Anio', 2009)]
        response = self.client.open('/server/Amadeus/VuelosEntrantes/ObtenerCantidadTotalVuelosPaisEnCiudadEnMesEnAnio/{PaisDestino}'.format(PaisDestino='PaisDestino_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_total_vuelos_pais_en_ciudad_mensual_en_anio(self):
        """
        Test case for obtener_cantidad_total_vuelos_pais_en_ciudad_mensual_en_anio

        Dado un pais, una ciudad y un año obtiene la cantidad total de vuelos que llegan a esa ciudad durante ese año separando por meses
        """
        query_string = [('CiudadDestino', 'Valencia'),
                        ('Anio', 2009)]
        response = self.client.open('/server/Amadeus/VuelosEntrantes/ObtenerCantidadTotalVuelosPaisEnCiudadMensualEnAnio/{PaisDestino}'.format(PaisDestino='PaisDestino_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_total_vuelos_totales_pais_en_ciudad_en_anio(self):
        """
        Test case for obtener_cantidad_total_vuelos_totales_pais_en_ciudad_en_anio

        Dado un pais, una ciudad y un año obtiene la cantidad total de vuelos que llegan a esa ciudad durante ese año
        """
        query_string = [('CiudadDestino', 'Valencia'),
                        ('Mes', 'Enero'),
                        ('Anio', 2009)]
        response = self.client.open('/server/Amadeus/VuelosEntrantes/ObtenerCantidadTotalVuelosTotalesPaisEnCiudadEnAnio/{PaisDestino}'.format(PaisDestino='PaisDestino_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_total_vuelos_totales_pais_en_mes_en_anio(self):
        """
        Test case for obtener_cantidad_total_vuelos_totales_pais_en_mes_en_anio

        Dado un pais, un mes y un año obtiene la cantidad total de vuelos que llegan a ese pais durante ese año y mes
        """
        query_string = [('Mes', 'Enero'),
                        ('Anio', 2009)]
        response = self.client.open('/server/Amadeus/VuelosEntrantes/ObtenerCantidadTotalVuelosTotalesPaisEnMesEnAnio/{PaisDestino}'.format(PaisDestino='PaisDestino_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_vuelos_ciudad_en_mes_en_rango_anios(self):
        """
        Test case for obtener_cantidad_vuelos_ciudad_en_mes_en_rango_anios

        Dado un pais, un mes y un rango de años obtiene la cantidad total de vuelos que llegan a ese pais durante ese mes y ese rango de años separando por ciudades
        """
        query_string = [('Mes', 'Enero'),
                        ('AnioInicio', 2009),
                        ('AnioFin', 2015)]
        response = self.client.open('/server/Amadeus/VuelosEntrantes/ObtenerCantidadVuelosCiudadEnMesEnRangoAnios/{PaisDestino}'.format(PaisDestino='PaisDestino_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_vuelos_ciudad_pais_en_mes_en_anio(self):
        """
        Test case for obtener_cantidad_vuelos_ciudad_pais_en_mes_en_anio

        Dado un pais, un mes y un año obtiene la cantidad total de vuelos que llegan a esa ciudad durante ese mes y ese año separando por ciudades
        """
        query_string = [('Mes', 'Enero'),
                        ('Anio', 2009)]
        response = self.client.open('/server/Amadeus/VuelosEntrantes/ObtenerCantidadVuelosCiudadPaisEnMesEnAnio/{PaisDestino}'.format(PaisDestino='PaisDestino_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_vuelos_ciudades_pais_en_anio(self):
        """
        Test case for obtener_cantidad_vuelos_ciudades_pais_en_anio

        Dado un pais y un año obtiene la cantidad de vuelos que llegan a ese pais durante ese año divividos por ciudades
        """
        query_string = [('Anio', 2009)]
        response = self.client.open('/server/Amadeus/VuelosEntrantes/ObtenerCantidadVuelosCiudadesPaisEnAnio/{PaisDestino}'.format(PaisDestino='PaisDestino_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_vuelos_pais_en_anio(self):
        """
        Test case for obtener_cantidad_vuelos_pais_en_anio

        Dado un pais y un año obtiene la cantidad de vuelos que llegan a ese pais durante ese año
        """
        query_string = [('Anio', 2009)]
        response = self.client.open('/server/Amadeus/VuelosEntrantes/ObtenerCantidadVuelosPaisEnAnio/{PaisDestino}'.format(PaisDestino='PaisDestino_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_vuelos_pais_en_ciudad_en_mes_en_rango_anios(self):
        """
        Test case for obtener_cantidad_vuelos_pais_en_ciudad_en_mes_en_rango_anios

        Dado un pais, una ciudad, un mes y un rango de años obtiene la cantidad total de vuelos que llegan a esa ciudad durante esos años y mes
        """
        query_string = [('CiudadDestino', 'Valencia'),
                        ('Mes', 'Enero'),
                        ('AnioInicio', 2009),
                        ('AnioFin', 2015)]
        response = self.client.open('/server/Amadeus/VuelosEntrantes/ObtenerCantidadVuelosPaisEnCiudadEnMesEnRangoAnios/{PaisDestino}'.format(PaisDestino='PaisDestino_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_vuelos_pais_en_ciudad_en_rango_anios(self):
        """
        Test case for obtener_cantidad_vuelos_pais_en_ciudad_en_rango_anios

        Dado un pais, una ciudad y un rango de años obtiene la cantidad total de vuelos que llegan a esa ciudad durante esos años
        """
        query_string = [('CiudadDestino', 'Valencia'),
                        ('AnioInicio', 2009),
                        ('AnioFin', 2015)]
        response = self.client.open('/server/Amadeus/VuelosEntrantes/ObtenerCantidadVuelosPaisEnCiudadEnRangoAnios/{PaisDestino}'.format(PaisDestino='PaisDestino_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_vuelos_pais_en_ciudad_mensual_en_rango_anios(self):
        """
        Test case for obtener_cantidad_vuelos_pais_en_ciudad_mensual_en_rango_anios

        Dado un pais, una ciudad y un rango de años obtiene la cantidad total de vuelos que llegan a esa ciudad durante esos años separado por meses
        """
        query_string = [('CiudadDestino', 'Valencia'),
                        ('AnioInicio', 2009),
                        ('AnioFin', 2015)]
        response = self.client.open('/server/Amadeus/VuelosEntrantes/ObtenerCantidadVuelosPaisEnCiudadMensualEnRangoAnios/{PaisDestino}'.format(PaisDestino='PaisDestino_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_vuelos_pais_en_mes_en_rango_anios(self):
        """
        Test case for obtener_cantidad_vuelos_pais_en_mes_en_rango_anios

        Dado un pais, un mes y un rango de años obtiene la cantidad total de vuelos que llegan a ese pais durante esos años
        """
        query_string = [('Mes', 'Enero'),
                        ('AnioInicio', 2009),
                        ('AnioFin', 2015)]
        response = self.client.open('/server/Amadeus/VuelosEntrantes/ObtenerCantidadVuelosPaisEnMesEnRangoAnios/{PaisDestino}'.format(PaisDestino='PaisDestino_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_vuelos_pais_en_rango_anios(self):
        """
        Test case for obtener_cantidad_vuelos_pais_en_rango_anios

        Dado un pais y un rango de años obtiene la cantidad de vuelos que llegan a ese pais diviendo por años
        """
        query_string = [('AnioInicio', 2009),
                        ('AnioFin', 2015)]
        response = self.client.open('/server/Amadeus/VuelosEntrantes/ObtenerCantidadVuelosPaisEnRangoAnios/{PaisDestino}'.format(PaisDestino='PaisDestino_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
