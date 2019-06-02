"""
Get minimum temperature from the database

__author__ = Pavan Maradia
__version__ = v1.0

"""

from sqlalchemy import func

from temp_tracker.db_utils import get_session
from temp_tracker.models import Temperature


class GetMin(object):
    """
    Get Minimum temperature from database
    """

    def __init__(self):
        """
        Initialize class object
        """
        self.response = dict()

    def controller(self, **kwargs):
        """
        Get Minimum number controller
        :param kwargs:
        :return:
        """
        session = get_session()
        sub_min_query = session.query(func.min(Temperature.temperature))
        row = session.query(Temperature).filter(
            Temperature.temperature == sub_min_query
        ).first()

        self.response = {
            'status': True,
            'message': {
                'id': row.id,
                'city': row.city,
                'temperature': row.temperature,
                'created_at': row.created_at
            }
        }
        return self.response
