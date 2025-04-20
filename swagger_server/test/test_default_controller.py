# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.dust import Dust  # noqa: E501
from swagger_server.models.dust_average import DustAverage  # noqa: E501
from swagger_server.models.project import Project  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_controller_get_dust_average(self):
        """Test case for controller_get_dust_average

        Returns average PM2.5, PM10, and AQI over all recorded entries.
        """
        response = self.client.open(
            '/air-quality-api/v1/dust/average',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_dust_data(self):
        """Test case for controller_get_dust_data

        Returns all dust data entries.
        """
        response = self.client.open(
            '/air-quality-api/v1/dust',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_dust_entry(self):
        """Test case for controller_get_dust_entry

        Returns details of a specific dust entry.
        """
        response = self.client.open(
            '/air-quality-api/v1/dust/{dustId}'.format(dust_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_project_details(self):
        """Test case for controller_get_project_details

        Returns details of the specified project.
        """
        response = self.client.open(
            '/air-quality-api/v1/projects/{projectId}'.format(project_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_projects(self):
        """Test case for controller_get_projects

        Returns a list of projects.
        """
        response = self.client.open(
            '/air-quality-api/v1/projects',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
