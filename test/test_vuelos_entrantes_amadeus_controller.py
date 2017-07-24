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
        query_string = [('Ciudad', 'Ciudad_example'),
                        ('Mes', 'Mes_example'),
                        ('Anio', 789)]
        response = self.client.open('/server/Amadeus/VuelosEntrantes/ObtenerCantidadTotalVuelosPaisEnCiudadEnMesEnAnio/{Pais}'.format(Pais='Pais_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_total_vuelos_pais_en_ciudad_mensual_en_anio(self):
        """
        Test case for obtener_cantidad_total_vuelos_pais_en_ciudad_mensual_en_anio

        Dado un pais, una ciudad y un año obtiene la cantidad total de vuelos que llegan a esa ciudad durante ese año separando por meses
        """
        query_string = [('Ciudad', 'Ciudad_example'),
                        ('Anio', 789)]
        response = self.client.open('/server/Amadeus/VuelosEntrantes/ObtenerCantidadTotalVuelosPaisEnCiudadMensualEnAnio/{Pais}'.format(Pais='Pais_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_total_vuelos_totales_pais_en_ciudad_en_anio(self):
        """
        Test case for obtener_cantidad_total_vuelos_totales_pais_en_ciudad_en_anio

        Dado un pais, una ciudad y un año obtiene la cantidad total de vuelos que llegan a esa ciudad durante ese año
        """
        query_string = [('Ciudad', 'Ciudad_example'),
                        ('Mes', 'Mes_example'),
                        ('Anio', 789)]
        response = self.client.open('/server/Amadeus/VuelosEntrantes/ObtenerCantidadTotalVuelosTotalesPaisEnCiudadEnAnio/{Pais}'.format(Pais='Pais_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_total_vuelos_totales_pais_en_mes_en_anio(self):
        """
        Test case for obtener_cantidad_total_vuelos_totales_pais_en_mes_en_anio

        Dado un pais, un mes y un año obtiene la cantidad total de vuelos que llegan a ese pais durante ese año y mes
        """
        query_string = [('Ciudad', 'Ciudad_example'),
                        ('Mes', 'Mes_example'),
                        ('Anio', 789)]
        response = self.client.open('/server/Amadeus/VuelosEntrantes/ObtenerCantidadTotalVuelosTotalesPaisEnMesEnAnio/{Pais}'.format(Pais='Pais_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_vuelos_ciudad_en_mes_en_rango_anios(self):
        """
        Test case for obtener_cantidad_vuelos_ciudad_en_mes_en_rango_anios

        Dado un pais, un mes y un rango de años obtiene la cantidad total de vuelos que llegan a ese pais durante ese mes y ese rango de años separando por ciudades
        """
        query_string = [('Mes', 'Mes_example'),
                        ('AnioInicio', 789),
                        ('AnioFin', 789)]
        response = self.client.open('/server/Amadeus/VuelosEntrantes/ObtenerCantidadVuelosCiudadEnMesEnRangoAnios/{Pais}'.format(Pais='Pais_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_vuelos_ciudad_pais_en_mes_en_anio(self):
        """
        Test case for obtener_cantidad_vuelos_ciudad_pais_en_mes_en_anio

        Dado un pais, un mes y un año obtiene la cantidad total de vuelos que llegan a esa ciudad durante ese mes y ese año separando por ciudades
        """
        query_string = [('Mes', 'Mes_example'),
                        ('Anio', 789)]
        response = self.client.open('/server/Amadeus/VuelosEntrantes/ObtenerCantidadVuelosCiudadPaisEnMesEnAnio/{Pais}'.format(Pais='Pais_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_vuelos_ciudades_pais_en_anio(self):
        """
        Test case for obtener_cantidad_vuelos_ciudades_pais_en_anio

        Dado un pais y un año obtiene la cantidad de vuelos que llegan a ese pais durante ese año divividos por ciudades
        """
        query_string = [('Anio', 789)]
        response = self.client.open('/server/Amadeus/VuelosEntrantes/ObtenerCantidadVuelosCiudadesPaisEnAnio/{Pais}'.format(Pais='Pais_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_vuelos_pais_en_anio(self):
        """
        Test case for obtener_cantidad_vuelos_pais_en_anio

        Dado un pais y un año obtiene la cantidad de vuelos que llegan a ese pais durante ese año
        """
        query_string = [('Anio', 789)]
        response = self.client.open('/server/Amadeus/VuelosEntrantes/ObtenerCantidadVuelosPaisEnAnio/{Pais}'.format(Pais='Pais_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_vuelos_pais_en_ciudad_en_mes_en_rango_anios(self):
        """
        Test case for obtener_cantidad_vuelos_pais_en_ciudad_en_mes_en_rango_anios

        Dado un pais, una ciudad, un mes y un rango de años obtiene la cantidad total de vuelos que llegan a esa ciudad durante esos años y mes
        """
        query_string = [('Ciudad', 'Ciudad_example'),
                        ('Mes', 'Mes_example'),
                        ('AnioInicio', 789),
                        ('AnioFin', 789)]
        response = self.client.open('/server/Amadeus/VuelosEntrantes/ObtenerCantidadVuelosPaisEnCiudadEnMesEnRangoAnios/{Pais}'.format(Pais='Pais_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_vuelos_pais_en_ciudad_en_rango_anios(self):
        """
        Test case for obtener_cantidad_vuelos_pais_en_ciudad_en_rango_anios

        Dado un pais, una ciudad y un rango de años obtiene la cantidad total de vuelos que llegan a esa ciudad durante esos años
        """
        query_string = [('Ciudad', 'Ciudad_example'),
                        ('AnioInicio', 789),
                        ('AnioFin', 789)]
        response = self.client.open('/server/Amadeus/VuelosEntrantes/ObtenerCantidadVuelosPaisEnCiudadEnRangoAnios/{Pais}'.format(Pais='Pais_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_vuelos_pais_en_ciudad_mensual_en_rango_anios(self):
        """
        Test case for obtener_cantidad_vuelos_pais_en_ciudad_mensual_en_rango_anios

        Dado un pais, una ciudad y un rango de años obtiene la cantidad total de vuelos que llegan a esa ciudad durante esos años separado por meses
        """
        query_string = [('Ciudad', 'Ciudad_example'),
                        ('AnioInicio', 789),
                        ('AnioFin', 789)]
        response = self.client.open('/server/Amadeus/VuelosEntrantes/ObtenerCantidadVuelosPaisEnCiudadMensualEnRangoAnios/{Pais}'.format(Pais='Pais_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_vuelos_pais_en_mes_en_rango_anios(self):
        """
        Test case for obtener_cantidad_vuelos_pais_en_mes_en_rango_anios

        Dado un pais, un mes y un rango de años obtiene la cantidad total de vuelos que llegan a ese pais durante esos años
        """
        query_string = [('Mes', 'Mes_example'),
                        ('AnioInicio', 789),
                        ('AnioFin', 789)]
        response = self.client.open('/server/Amadeus/VuelosEntrantes/ObtenerCantidadVuelosPaisEnMesEnRangoAnios/{Pais}'.format(Pais='Pais_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_vuelos_pais_en_rango_anios(self):
        """
        Test case for obtener_cantidad_vuelos_pais_en_rango_anios

        Dado un pais y un rango de años obtiene la cantidad de vuelos que llegan a ese pais diviendo por años
        """
        query_string = [('AnioInicio', 789),
                        ('AnioFin', 789)]
        response = self.client.open('/server/Amadeus/VuelosEntrantes/ObtenerCantidadVuelosPaisEnRangoAnios/{Pais}'.format(Pais='Pais_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
