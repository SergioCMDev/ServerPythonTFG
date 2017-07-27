# coding: utf-8

from __future__ import absolute_import

from . import BaseTestCase
from six import BytesIO
from flask import json


class TestVuelosEntrantesAenaController(BaseTestCase):
    """ VuelosEntrantesAenaController integration test stubs """

    def test_obtener_cantidad_anio_ciudad(self):
        """
        Test case for obtener_cantidad_anio_ciudad

        Obtener cantidades de vuelos entrantes en la ciudad del pais divididas por meses
        """
        query_string = [('CiudadDestino', 'Valencia'),
                        ('Anio', 2009)]
        response = self.client.open('/server/Aena/VuelosEntrantes/ObtenerCantidadAnioCiudad/{PaisDestino}'.format(PaisDestino='PaisDestino_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_anio_por_ciudades(self):
        """
        Test case for obtener_cantidad_anio_por_ciudades

        Obtener cantidad de vuelos entrantes en las ciudades de un pais durante un año
        """
        query_string = [('Anio', 2009)]
        response = self.client.open('/server/Aena/VuelosEntrantes/ObtenerCantidadAnioPorCiudades/{PaisDestino}'.format(PaisDestino='PaisDestino_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_anualmente(self):
        """
        Test case for obtener_cantidad_anualmente

        Obtener cantidad de vuelos entrantes anualmente dado un pais destino y un rango de años
        """
        query_string = [('AnioInicio', 2009),
                        ('AnioFin', 2015)]
        response = self.client.open('/server/Aena/VuelosEntrantes/ObtenerCantidadAnualmente/{PaisDestino}'.format(PaisDestino='PaisDestino_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_ciudad(self):
        """
        Test case for obtener_cantidad_ciudad

        Obtener cantidad de vuelos entrantes en una ciudad de un pais durante el rango de años seleccionado
        """
        query_string = [('CiudadDestino', 'Valencia'),
                        ('AnioInicio', 2009),
                        ('AnioFin', 2015)]
        response = self.client.open('/server/Aena/VuelosEntrantes/ObtenerCantidadCiudad/{PaisDestino}'.format(PaisDestino='PaisDestino_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_entrantes_por_ciudades(self):
        """
        Test case for obtener_cantidad_entrantes_por_ciudades

        Obtener cantidad de vuelos entrantes en las ciudades de un pais durante un rango de años
        """
        query_string = [('AnioInicio', 2009),
                        ('AnioFin', 2015)]
        response = self.client.open('/server/Aena/VuelosEntrantes/ObtenerCantidadPorCiudades/{PaisDestino}'.format(PaisDestino='PaisDestino_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_mensual(self):
        """
        Test case for obtener_cantidad_mensual

        Obtener cantidad de vuelos entrantes durante los meses de un año 
        """
        query_string = [('Anio', 2009)]
        response = self.client.open('/server/Aena/VuelosEntrantes/ObtenerCantidadMensual/{PaisDestino}'.format(PaisDestino='PaisDestino_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_mensualmente(self):
        """
        Test case for obtener_cantidad_mensualmente

        Obtener cantidad de vuelos entrantes de forma mensual dado un pais destino y un rango de años
        """
        query_string = [('AnioInicio', 2009),
                        ('AnioFin', 2015)]
        response = self.client.open('/server/Aena/VuelosEntrantes/ObtenerCantidadMensualmente/{PaisDestino}'.format(PaisDestino='PaisDestino_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_mes(self):
        """
        Test case for obtener_cantidad_mes

        Obtener cantidad de vuelos entrantes durante el mismo mes en un rango de años para el pais destino
        """
        query_string = [('Mes', 'Enero'),
                        ('AnioInicio', 2009),
                        ('AnioFin', 2015)]
        response = self.client.open('/server/Aena/VuelosEntrantes/ObtenerCantidadMes/{PaisDestino}'.format(PaisDestino='PaisDestino_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_mes_anio_por_ciudades(self):
        """
        Test case for obtener_cantidad_mes_anio_por_ciudades

        Obtener cantidad de vuelos entrantes en las ciudades del pais durante el mes del año seleccionado
        """
        query_string = [('Anio', 2009),
                        ('Mes', 'Enero')]
        response = self.client.open('/server/Aena/VuelosEntrantes/ObtenerCantidadMesAnioPorCiudades/{PaisDestino}'.format(PaisDestino='PaisDestino_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_mes_ciudad(self):
        """
        Test case for obtener_cantidad_mes_ciudad

        Obtener cantidad de vuelos entrantes en la ciudad del pais durante el mes del rango de años seleccionado
        """
        query_string = [('CiudadDestino', 'Valencia'),
                        ('Mes', 'Enero'),
                        ('AnioInicio', 2009),
                        ('AnioFin', 2015)]
        response = self.client.open('/server/Aena/VuelosEntrantes/ObtenerCantidadMesCiudad/{PaisDestino}'.format(PaisDestino='PaisDestino_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_mes_por_ciudades(self):
        """
        Test case for obtener_cantidad_mes_por_ciudades

        Obtener cantidad de vuelos entrantes en las ciudades de un pais durante un rango de años durante un mismo mes
        """
        query_string = [('AnioInicio', 2009),
                        ('AnioFin', 2015),
                        ('Mes', 'Enero')]
        response = self.client.open('/server/Aena/VuelosEntrantes/ObtenerCantidadMesPorCiudades/{PaisDestino}'.format(PaisDestino='PaisDestino_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
