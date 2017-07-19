# coding: utf-8

from __future__ import absolute_import

from . import BaseTestCase
from six import BytesIO
from flask import json


class TestTouristsController(BaseTestCase):
    """ TouristsController integration test stubs """

    def test_find_by_country_origin(self):
        """
        Test case for find_by_country_origin

        Finds Tourists by Country Origin
        """
        response = self.client.open('/v2/Tourists/findByCountryOrigin/{countryOrigin}'.format(countryOrigin='countryOrigin_example'),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
