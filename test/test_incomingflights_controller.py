# coding: utf-8

from __future__ import absolute_import

from . import BaseTestCase
from six import BytesIO
from flask import json


class TestIncomingflightsController(BaseTestCase):
    """ IncomingflightsController integration test stubs """

    def test_find_quantity_by_country_origin(self):
        """
        Test case for find_quantity_by_country_origin

        Finds Incomingflights by Country Origin
        """
        query_string = [('StartingYear', 789),
                        ('FinalYear', 789)]
        response = self.client.open('/v2/Incomingflights/findQuantityByCountryOriginBetweenYears/{countryOrigin}'.format(countryOrigin=789),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
