"""
Get Mean temperature from the database

__author__ = Pavan Maradia
__version__ = v1.0

"""

from statistics import mean

from temp_tracker.db_utils import get_session
from temp_tracker.models import Temperature


class GetMean(object):
    """
    Get Mean temperature from database
    """

    def __init__(self):
        """
        Initialize class object
        """
        self.response = dict()

    def controller(self, **kwargs):
        """
        Get mean temperature controller
        :param kwargs:
        :return:
        """
        session = get_session()
        data = [i[0] for i in session.query(Temperature.temperature).all()]
        self.response = {
            'status': True,
            'message': mean(data)
        }
        return self.response
