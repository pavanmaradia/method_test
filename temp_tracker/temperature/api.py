"""
API Controller of Temperature module

__author__ = Pavan Maradia
__version__ = v1.0
"""


class TempTracker(object):
    """
    Class Temperature Tracker
    """

    def __init__(self):
        """
        initialize class object
        """
        self.payload = dict()
        self.methods = {
            'get_max': self.get_max,
            'get_mean': self.get_mean,
            'get_min': self.get_min,
            'insert': self.insert
        }
        self.flask_resp = dict()
        self.response = dict()

    def controller(self, **kwargs):
        """
        Control temperature control flow
        :return:
        """

        method = kwargs.get('method')

        if method not in self.methods:
            self.response = {
                'status': False,
                'message': 'Requested method does not supported currently.'
            }
            return self.response

        self.payload = kwargs.get('payload', {})
        self.methods.get(method)()

        if kwargs.get('response') == 'flask_resp':
            return self.flask_resp

        return self.response

    def get_max(self):
        """
        Get maximum temperature processor
        :return:
        """
        try:
            from .processor.get_max import GetMax
        except ImportError:
            self.response = {
                'status': False,
                'message': 'Failed to find GetMax module'
            }
            return

        self.flask_resp = GetMax().controller(**self.payload)
        if not self.flask_resp.get('status'):
            self.response = self.flask_resp
            return

        self.response = self.flask_resp.get('message').get('temperature')

    def get_mean(self):
        """
        Get Mean temperature processor
        :return:
        """
        try:
            from .processor.get_mean import GetMean
        except ImportError:
            self.response = {
                'status': False,
                'message': 'Failed to find GetMean module'
            }
            return

        self.flask_resp = GetMean().controller(**self.payload)

        if not self.flask_resp.get('status'):
            self.response = self.flask_resp
            return

        self.response = self.flask_resp.get('message')

    def get_min(self):
        """
        Get Minimum temperature processor
        :return:
        """
        try:
            from .processor.get_min import GetMin
        except ImportError:
            self.response = {
                'status': False,
                'message': 'Failed to find GetMin module'
            }
            return
        self.flask_resp = GetMin().controller(**self.payload)

        if not self.flask_resp.get('status'):
            self.response = self.flask_resp
            return
        self.response = self.flask_resp.get('message').get('temperature')

    def insert(self):
        """
        Get maximum temperature processor
        :return:
        """
        try:
            from .processor.insert import Insert
        except ImportError:
            self.response = {
                'status': False,
                'message': 'Failed to find Insert module'
            }
            return
        self.response = Insert().controller(**self.payload)
        self.flask_resp = self.response
