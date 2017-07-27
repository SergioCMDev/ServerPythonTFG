# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.body import Body
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestCalculosController(BaseTestCase):
    """ CalculosController integration test stubs """

    def test_obtener_progresion_lineal(self):
        """
        Test case for obtener_progresion_lineal

        Obtener la prediccion para un año dado el año a predecir y los datos de varios años anteriores
        """
        body = [Body()]
        query_string = [('AnioPrediccion', '2009')]
        response = self.client.open('/server/Calculos/ObtenerProgresionLineal/',
                                    method='POST',
                                    data=json.dumps(body),
                                    content_type='application/json',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
