# coding: utf-8

"""
    Golf v2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Injury(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'injury_id': 'int',
        'player_id': 'int',
        'name': 'str',
        'active': 'bool',
        'start_date': 'str',
        'status': 'str',
        'body_part': 'str',
        'expected_return': 'str'
    }

    attribute_map = {
        'injury_id': 'InjuryID',
        'player_id': 'PlayerID',
        'name': 'Name',
        'active': 'Active',
        'start_date': 'StartDate',
        'status': 'Status',
        'body_part': 'BodyPart',
        'expected_return': 'ExpectedReturn'
    }

    def __init__(self, injury_id=None, player_id=None, name=None, active=None, start_date=None, status=None, body_part=None, expected_return=None):  # noqa: E501
        """Injury - a model defined in Swagger"""  # noqa: E501

        self._injury_id = None
        self._player_id = None
        self._name = None
        self._active = None
        self._start_date = None
        self._status = None
        self._body_part = None
        self._expected_return = None
        self.discriminator = None

        if injury_id is not None:
            self.injury_id = injury_id
        if player_id is not None:
            self.player_id = player_id
        if name is not None:
            self.name = name
        if active is not None:
            self.active = active
        if start_date is not None:
            self.start_date = start_date
        if status is not None:
            self.status = status
        if body_part is not None:
            self.body_part = body_part
        if expected_return is not None:
            self.expected_return = expected_return

    @property
    def injury_id(self):
        """Gets the injury_id of this Injury.  # noqa: E501


        :return: The injury_id of this Injury.  # noqa: E501
        :rtype: int
        """
        return self._injury_id

    @injury_id.setter
    def injury_id(self, injury_id):
        """Sets the injury_id of this Injury.


        :param injury_id: The injury_id of this Injury.  # noqa: E501
        :type: int
        """

        self._injury_id = injury_id

    @property
    def player_id(self):
        """Gets the player_id of this Injury.  # noqa: E501


        :return: The player_id of this Injury.  # noqa: E501
        :rtype: int
        """
        return self._player_id

    @player_id.setter
    def player_id(self, player_id):
        """Sets the player_id of this Injury.


        :param player_id: The player_id of this Injury.  # noqa: E501
        :type: int
        """

        self._player_id = player_id

    @property
    def name(self):
        """Gets the name of this Injury.  # noqa: E501


        :return: The name of this Injury.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Injury.


        :param name: The name of this Injury.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def active(self):
        """Gets the active of this Injury.  # noqa: E501


        :return: The active of this Injury.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this Injury.


        :param active: The active of this Injury.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def start_date(self):
        """Gets the start_date of this Injury.  # noqa: E501


        :return: The start_date of this Injury.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this Injury.


        :param start_date: The start_date of this Injury.  # noqa: E501
        :type: str
        """

        self._start_date = start_date

    @property
    def status(self):
        """Gets the status of this Injury.  # noqa: E501


        :return: The status of this Injury.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Injury.


        :param status: The status of this Injury.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def body_part(self):
        """Gets the body_part of this Injury.  # noqa: E501


        :return: The body_part of this Injury.  # noqa: E501
        :rtype: str
        """
        return self._body_part

    @body_part.setter
    def body_part(self, body_part):
        """Sets the body_part of this Injury.


        :param body_part: The body_part of this Injury.  # noqa: E501
        :type: str
        """

        self._body_part = body_part

    @property
    def expected_return(self):
        """Gets the expected_return of this Injury.  # noqa: E501


        :return: The expected_return of this Injury.  # noqa: E501
        :rtype: str
        """
        return self._expected_return

    @expected_return.setter
    def expected_return(self, expected_return):
        """Sets the expected_return of this Injury.


        :param expected_return: The expected_return of this Injury.  # noqa: E501
        :type: str
        """

        self._expected_return = expected_return

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Injury, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Injury):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other