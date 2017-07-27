# coding: utf-8

from __future__ import absolute_import

from . import BaseTestCase
from six import BytesIO
from flask import json


class TestTuristasEntrantesAmadeusController(BaseTestCase):
    """ TuristasEntrantesAmadeusController integration test stubs """

    def test_obtener_cantidad_turistas_en_ciudades_mensual_en_rango_anios(self):
        """
        Test case for obtener_cantidad_turistas_en_ciudades_mensual_en_rango_anios

        Dado un pais y un rango de años obtiene la cantidad total de personas que llegan a ese pais separando por ciudades, meses y años
        """
        query_string = [('AnioInicio', 2009),
                        ('AnioFin', 2015)]
        response = self.client.open('/server/Amadeus/TuristasEntrantes/ObtenerCantidadTuristasEnCiudadesMensualEnRangoAnios/{PaisDestino}'.format(PaisDestino='PaisDestino_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_turistas_en_pais_en_rango_anios(self):
        """
        Test case for obtener_cantidad_turistas_en_pais_en_rango_anios

        Dado un pais y un rango de años obtiene la cantidad total de personas que llegan a ese pais separando por años
        """
        query_string = [('AnioInicio', 2009),
                        ('AnioFin', 2015)]
        response = self.client.open('/server/Amadeus/TuristasEntrantes/ObtenerCantidadTuristasEnPaisEnRangoAnios/{PaisDestino}'.format(PaisDestino='PaisDestino_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_turistas_y_ciudades_origen_en_ciudad_en_mes_en_rango_anios(self):
        """
        Test case for obtener_cantidad_turistas_y_ciudades_origen_en_ciudad_en_mes_en_rango_anios

        Dado un pais, una ciudad, un mes y un rango de años obtiene la cantidad total de personas que llegan a esa ciudad separando por años,paises y ciudades de origen
        """
        query_string = [('CiudadDestino', 'Amberes'),
                        ('Mes', 'Enero'),
                        ('AnioInicio', 2009),
                        ('AnioFin', 2015)]
        response = self.client.open('/server/Amadeus/TuristasEntrantes/ObtenerCantidadTuristasYCiudadesOrigenEnCiudadEnMesEnRangoAnios/{PaisDestino}'.format(PaisDestino='PaisDestino_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_turistas_y_ciudades_origen_en_ciudad_en_rango_anios(self):
        """
        Test case for obtener_cantidad_turistas_y_ciudades_origen_en_ciudad_en_rango_anios

        Dado un pais y un rango de años obtiene la cantidad total de personas que llegan a esa ciudad separando por años, paises y ciudades de origen
        """
        query_string = [('AnioInicio', 2009),
                        ('AnioFin', 2015)]
        response = self.client.open('/server/Amadeus/TuristasEntrantes/ObtenerCantidadTuristasYCiudadesOrigenEnCiudadEnRangoAnios/{PaisDestino}'.format(PaisDestino='PaisDestino_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_turistas_y_ciudades_origen_en_pais_en_rango_anios(self):
        """
        Test case for obtener_cantidad_turistas_y_ciudades_origen_en_pais_en_rango_anios

        Dado un pais, una ciudad y un rango de años obtiene la cantidad total de personas que llegan a esa ciudad separando por años,paises y ciudades de origen
        """
        query_string = [('CiudadDestino', 'Amberes'),
                        ('AnioInicio', 2009),
                        ('AnioFin', 2015)]
        response = self.client.open('/server/Amadeus/TuristasEntrantes/ObtenerCantidadTuristasYCiudadesOrigenEnPaisEnRangoAnios/{PaisDestino}'.format(PaisDestino='PaisDestino_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_turistas_y_pais_origen_en_ciudad_en_mes_en_anio(self):
        """
        Test case for obtener_cantidad_turistas_y_pais_origen_en_ciudad_en_mes_en_anio

        Dado un pais, una ciudad destino, un mes y un año obtiene la cantidad total de personas que llegan a esa ciudad separando por pais de origen
        """
        query_string = [('CiudadDestino', 'Amberes'),
                        ('Mes', 'Enero'),
                        ('Anio', 2009)]
        response = self.client.open('/server/Amadeus/TuristasEntrantes/ObtenerCantidadTuristasYPaisOrigenEnCiudadEnMesEnAnio/{PaisDestino}'.format(PaisDestino='PaisDestino_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_turistas_y_paises_en_pais_en_anio(self):
        """
        Test case for obtener_cantidad_turistas_y_paises_en_pais_en_anio

        Dado un pais y un año obtiene la cantidad total de personas que llegan a ese pais en ese año
        """
        query_string = [('Anio', 2009)]
        response = self.client.open('/server/Amadeus/TuristasEntrantes/ObtenerCantidadTuristasYPaisesEnPaisEnAnio/{PaisDestino}'.format(PaisDestino='PaisDestino_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_turistas_y_paises_mensual_en_pais_en_anio(self):
        """
        Test case for obtener_cantidad_turistas_y_paises_mensual_en_pais_en_anio

        Dado un pais y un año obtiene la cantidad total de personas que llegan a ese pais en ese año separadas por meses
        """
        query_string = [('Anio', 2009)]
        response = self.client.open('/server/Amadeus/TuristasEntrantes/ObtenerCantidadTuristasYPaisesMensualEnPaisEnAnio/{PaisDestino}'.format(PaisDestino='PaisDestino_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
