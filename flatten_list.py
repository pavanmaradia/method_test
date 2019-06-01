"""
Flatten List from nested list

__author__ = Pavan Maradia
__version__ = v1.0

"""


class ListFlatten(object):
    """
    Flat Nested list in single list
    """

    def __init__(self):
        """
        Initialize class object
        """
        self.resp_list = list()
        self.response = dict()

    def controller(self, requested_list):
        """
        Control the flow of flatten list
        :param requested_list: original nested list
        :return:
        """
