import connexion
import six

from swagger_server.models.dust import Dust  # noqa: E501
from swagger_server.models.dust_average import DustAverage  # noqa: E501
from swagger_server.models.project import Project  # noqa: E501
from swagger_server import util


def controller_get_dust_average():  # noqa: E501
    """Returns average PM2.5, PM10, and AQI over all recorded entries.

     # noqa: E501


    :rtype: DustAverage
    """
    return 'do some magic!'


def controller_get_dust_data():  # noqa: E501
    """Returns all dust data entries.

     # noqa: E501


    :rtype: List[Dust]
    """
    return 'do some magic!'


def controller_get_dust_entry(dust_id):  # noqa: E501
    """Returns details of a specific dust entry.

     # noqa: E501

    :param dust_id: 
    :type dust_id: int

    :rtype: Dust
    """
    return 'do some magic!'


def controller_get_project_details(project_id):  # noqa: E501
    """Returns details of the specified project.

     # noqa: E501

    :param project_id: 
    :type project_id: int

    :rtype: Project
    """
    return 'do some magic!'


def controller_get_projects():  # noqa: E501
    """Returns a list of projects.

     # noqa: E501


    :rtype: List[Project]
    """
    return 'do some magic!'
