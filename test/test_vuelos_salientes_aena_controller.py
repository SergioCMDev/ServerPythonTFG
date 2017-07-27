# coding: utf-8

from __future__ import absolute_import

from . import BaseTestCase
from six import BytesIO
from flask import json


class TestVuelosSalientesAenaController(BaseTestCase):
    """ VuelosSalientesAenaController integration test stubs """

    def test_obtener_cantidad_ciudad_anualmente_mensualmente(self):
        """
        Test case for obtener_cantidad_ciudad_anualmente_mensualmente

        Obtiene la cantidad de vuelos salientes en una ciudad de un pais durante un año de forma mensual
        """
        query_string = [('CiudadOrigen', 'Valencia'),
                        ('Anio', 2009)]
        response = self.client.open('/server/Aena/VuelosSalientes/ObtenerCantidadCiudadAnualmenteMensualmente/{PaisOrigen}'.format(PaisOrigen='PaisOrigen_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_ciudad_mensualmente(self):
        """
        Test case for obtener_cantidad_ciudad_mensualmente

        Obtiene la cantidad de vuelos salientes de desde un pais hacia una ciudad destino durante un rango de años y lo organizamos mensualmente
        """
        query_string = [('PaisDestino', 'Belgium'),
                        ('CiudadDestino', 'Amberes'),
                        ('AnioInicio', 2009),
                        ('AnioFin', 2015)]
        response = self.client.open('/server/Aena/VuelosSalientes/ObtenerCantidadCiudadMensualmente/{PaisOrigen}'.format(PaisOrigen='PaisOrigen_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_ciudades_durante_un_mes_en_rango_anios(self):
        """
        Test case for obtener_cantidad_ciudades_durante_un_mes_en_rango_anios

        Obtiene la cantidad de vuelos salientes en todas las ciudades de un pais durante un mes en un rango de años
        """
        query_string = [('Mes', 'Enero'),
                        ('AnioInicio', 2009),
                        ('AnioFin', 2015)]
        response = self.client.open('/server/Aena/VuelosSalientes/ObtenerCantidadCiudadesDuranteUnMesEnRangoAnios/{PaisOrigen}'.format(PaisOrigen='PaisOrigen_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_ciudades_en_anio(self):
        """
        Test case for obtener_cantidad_ciudades_en_anio

        Obtiene la cantidad de vuelos salientes en todas las ciudades de un pais durante un anio
        """
        query_string = [('Anio', 2009)]
        response = self.client.open('/server/Aena/VuelosSalientes/ObtenerCantidadCiudadesEnAnio/{PaisOrigen}'.format(PaisOrigen='PaisOrigen_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_por_ciudades_mensualmente(self):
        """
        Test case for obtener_cantidad_por_ciudades_mensualmente

        Obtener cantidad de vuelos salientes por ciudades de un pais de forma mensual
        """
        response = self.client.open('/server/Aena/VuelosSalientes/ObtenerCantidadPorCiudadesMensualmente/{PaisOrigen}'.format(PaisOrigen='PaisOrigen_example'),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_por_ciudades_mensualmentey_anualmente(self):
        """
        Test case for obtener_cantidad_por_ciudades_mensualmentey_anualmente

        Obtener cantidad de vuelos salientes totales en todas las ciudad de un pais durante un rango de años separando por meses
        """
        query_string = [('AnioInicio', 2009),
                        ('AnioFin', 2015)]
        response = self.client.open('/server/Aena/VuelosSalientes/ObtenerCantidadPorCiudadesMensualmenteyAnualmente/{PaisOrigen}'.format(PaisOrigen='PaisOrigen_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

 def test_obtener_cantidad_entrantes_ciudad(self):
        """
        Test case for obtener_cantidad_entrantes_ciudad

        Obtener cantidad de vuelos salientes hacia una ciudad desde un pais durante un año
        """
        query_string = [('CiudaDestino', 'Valencia'),
                        ('Anio', 2009)]
        response = self.client.open('/server/Aena/VuelosSalientes/ObtenerCantidadEntrantesCiudad/{PaisOrigen}'.format(PaisOrigen='Belgium'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
