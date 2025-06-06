# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class DustAverage(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, average_pm25: float=None, average_pm10: float=None, average_aqi: float=None):  # noqa: E501
        """DustAverage - a model defined in Swagger

        :param average_pm25: The average_pm25 of this DustAverage.  # noqa: E501
        :type average_pm25: float
        :param average_pm10: The average_pm10 of this DustAverage.  # noqa: E501
        :type average_pm10: float
        :param average_aqi: The average_aqi of this DustAverage.  # noqa: E501
        :type average_aqi: float
        """
        self.swagger_types = {
            'average_pm25': float,
            'average_pm10': float,
            'average_aqi': float
        }

        self.attribute_map = {
            'average_pm25': 'average_pm25',
            'average_pm10': 'average_pm10',
            'average_aqi': 'average_aqi'
        }
        self._average_pm25 = average_pm25
        self._average_pm10 = average_pm10
        self._average_aqi = average_aqi

    @classmethod
    def from_dict(cls, dikt) -> 'DustAverage':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DustAverage of this DustAverage.  # noqa: E501
        :rtype: DustAverage
        """
        return util.deserialize_model(dikt, cls)

    @property
    def average_pm25(self) -> float:
        """Gets the average_pm25 of this DustAverage.


        :return: The average_pm25 of this DustAverage.
        :rtype: float
        """
        return self._average_pm25

    @average_pm25.setter
    def average_pm25(self, average_pm25: float):
        """Sets the average_pm25 of this DustAverage.


        :param average_pm25: The average_pm25 of this DustAverage.
        :type average_pm25: float
        """

        self._average_pm25 = average_pm25

    @property
    def average_pm10(self) -> float:
        """Gets the average_pm10 of this DustAverage.


        :return: The average_pm10 of this DustAverage.
        :rtype: float
        """
        return self._average_pm10

    @average_pm10.setter
    def average_pm10(self, average_pm10: float):
        """Sets the average_pm10 of this DustAverage.


        :param average_pm10: The average_pm10 of this DustAverage.
        :type average_pm10: float
        """

        self._average_pm10 = average_pm10

    @property
    def average_aqi(self) -> float:
        """Gets the average_aqi of this DustAverage.


        :return: The average_aqi of this DustAverage.
        :rtype: float
        """
        return self._average_aqi

    @average_aqi.setter
    def average_aqi(self, average_aqi: float):
        """Sets the average_aqi of this DustAverage.


        :param average_aqi: The average_aqi of this DustAverage.
        :type average_aqi: float
        """

        self._average_aqi = average_aqi
