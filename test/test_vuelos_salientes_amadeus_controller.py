# coding: utf-8

from __future__ import absolute_import

from . import BaseTestCase
from six import BytesIO
from flask import json


class TestVuelosSalientesAmadeusController(BaseTestCase):
    """ VuelosSalientesAmadeusController integration test stubs """

    def test_obtener_cantidad_anual(self):
        """
        Test case for obtener_cantidad_anual

        Dado un pais origen obtiene la cantidad de vuelos que salen de dicho pais durante un rango de años
        """
        query_string = [('AnioInicio', 789),
                        ('AnioFin', 789)]
        response = self.client.open('/server/Amadeus/VuelosSalientes/ObtenerCantidadAnual/{Pais}'.format(Pais='Pais_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_ciudad_mensual_rango_anios(self):
        """
        Test case for obtener_cantidad_ciudad_mensual_rango_anios

        Dado un pais origen y una ciudad origen obtiene la cantidad de vuelos que salen de dicha ciudad durante un rango de años organzido mensualmente
        """
        query_string = [('Ciudad', 'Ciudad_example'),
                        ('AnioInicio', 789),
                        ('AnioFin', 789)]
        response = self.client.open('/server/Amadeus/VuelosSalientes/ObtenerCantidadCiudadMensualRangoAnios/{Pais}'.format(Pais='Pais_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_ciudad_mes_rango_anios(self):
        """
        Test case for obtener_cantidad_ciudad_mes_rango_anios

        Dado un pais origen y una ciudad origen obtiene la cantidad de vuelos que salen de dicha ciudad durante un rango de años durante un mes
        """
        query_string = [('Ciudad', 'Ciudad_example'),
                        ('Mes', 'Mes_example'),
                        ('AnioInicio', 789),
                        ('AnioFin', 789)]
        response = self.client.open('/server/Amadeus/VuelosSalientes/ObtenerCantidadCiudadMesRangoAnios/{Pais}'.format(Pais='Pais_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_ciudades_mensual_rango_anios(self):
        """
        Test case for obtener_cantidad_ciudades_mensual_rango_anios

        Dado un pais origen obtiene la cantidad de vuelos que salen de dicho pais y las ciudades hacia las que se dirigen durante un rango de años diviendo por meses
        """
        query_string = [('AnioInicio', 789),
                        ('AnioFin', 789)]
        response = self.client.open('/server/Amadeus/VuelosSalientes/ObtenerCantidadCiudadesMensualRangoAnios/{Pais}'.format(Pais='Pais_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_ciudades_rango_anios(self):
        """
        Test case for obtener_cantidad_ciudades_rango_anios

        Dado un pais origen obtiene la cantidad de vuelos que salen de dicho pais y las ciudades hacia las que se dirigen durante un rango de años
        """
        query_string = [('AnioInicio', 789),
                        ('AnioFin', 789)]
        response = self.client.open('/server/Amadeus/VuelosSalientes/ObtenerCantidadCiudadesRangoAnios/{Pais}'.format(Pais='Pais_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_mensualmente_en_anio(self):
        """
        Test case for obtener_cantidad_mensualmente_en_anio

        Dado un pais origen y un anio obtiene la cantidad de vuelos que salen de dicho pais durante ese año de forma mensual
        """
        query_string = [('Anio', 789)]
        response = self.client.open('/server/Amadeus/VuelosSalientes/ObtenerCantidadMensualmenteEnAnio/{Pais}'.format(Pais='Pais_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_mes_en_anios(self):
        """
        Test case for obtener_cantidad_mes_en_anios

        Dado un pais origen, un mes y un rango de años obtiene la cantidad de vuelos salientes durante ese rango de años en ese mes
        """
        query_string = [('Mes', 'Mes_example'),
                        ('AnioInicio', 789),
                        ('AnioFin', 789)]
        response = self.client.open('/server/Amadeus/VuelosSalientes/ObtenerCantidadMesEnAnios/{Pais}'.format(Pais='Pais_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_vuelos_salienes_ciudades_en_anio(self):
        """
        Test case for obtener_cantidad_vuelos_salienes_ciudades_en_anio

        Dado un pais origen y un anio obtiene la cantidad de vuelos que salen de dicho pais durante ese año dividiendo por ciudades
        """
        query_string = [('Anio', 789)]
        response = self.client.open('/server/Amadeus/VuelosSalientes/ObtenerCantidadVuelosSalienesCiudadesEnAnio/{Pais}'.format(Pais='Pais_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_vuelos_salientes_ciudad_rango_anios(self):
        """
        Test case for obtener_cantidad_vuelos_salientes_ciudad_rango_anios

        Dado un pais origen y una ciudad origen obtiene la cantidad de vuelos que salen de dicha ciudad durante un rango de años
        """
        query_string = [('Ciudad', 'Ciudad_example'),
                        ('AnioInicio', 789),
                        ('AnioFin', 789)]
        response = self.client.open('/server/Amadeus/VuelosSalientes/ObtenerCantidadVuelosSalientesCiudadRangoAnios/{Pais}'.format(Pais='Pais_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
