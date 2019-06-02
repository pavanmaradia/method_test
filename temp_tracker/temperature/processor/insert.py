"""
Insert temperature in database

__author__ = Pavan Maradia
__version__ = v1.0

"""

from time import time

from temp_tracker.db_utils import get_session
from temp_tracker.models import Temperature
from temp_tracker.utility import required_field_validation


class Insert(object):
    """
    Insert temperature in database
    """

    def __init__(self):
        """
        Initialize class object
        """
        self.response = dict()
        self.payload = dict()

    def controller(self, **kwargs):
        """
        Insert Temperature controller
        :param kwargs:
        :return:
        """
        self.payload = kwargs

        validation_response = Validation().controller(**self.payload)
        if validation_response.get('status') is False:
            return validation_response

        self.insert_in_database()

        return self.response

    def insert_in_database(self):
        """
        Insert in database
        :return:
        """
        self.payload.update({
            'created_at': time()
        })
        self.payload['temperature'] = int(self.payload['temperature'])
        session = get_session()
        temperature = Temperature(**self.payload)
        session.add(temperature)
        session.commit()

        self.response = {
            'status': True,
            'message': 'Temperature has been inserted'
        }


class Validation(object):

    def __init__(self):
        """
        initialize validation object
        """
        self.payload = dict()
        self.response = dict()
        self.methods = {
            'temperature_range': self.temperature_range,
            'required_keys': self.required_field,
        }

    def controller(self, **kwargs):
        """
        Validation controller
        :param kwargs:
        :return:
        """

        self.payload = kwargs

        if not self.payload:
            self.response = {
                'status': False,
                'message': 'Payload is missing'
            }

        for method, _func in self.methods.items():
            _func()
            if self.response.get('status', False) is False:
                return self.response

        return self.response

    def temperature_range(self):
        """
        Validate if temperature is in range or not
        :return:
        """
        try:
            temperature = int(self.payload.get('temperature', -1))
        except:
            self.response = {
                'status': False,
                'message': 'Temperature is not integer'
            }
            return

        if 0 < temperature < 110:
            self.response = {
                'status': True,
            }

        else:
            self.response = {
                'status': False,
                'message': 'Temperature is missing or out of the range '
                           '(0 to 113)'
            }

    def required_field(self):
        """
        Validate if require fields are present in payload or not
        :return:
        """

        self.response = required_field_validation(
            payload=self.payload,
            require_fields=['temperature', 'city']
        )
