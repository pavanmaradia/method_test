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

        return self.response

    def get_max(self):
        """
        Get maximum temperature processor
        :return:
        """

    def get_mean(self):
        """
        Get Mean temperature processor
        :return:
        """

    def get_min(self):
        """
        Get Minimum temperature processor
        :return:
        """

    def insert(self):
        """
        Get maximum temperature processor
        :return:
        """
