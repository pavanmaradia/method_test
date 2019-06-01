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
        if isinstance(requested_list, list):
            self.response = {
                'status': True,
                'message': self.flat_list(requested_list)
            }
        else:
            self.response = {
                'status': False,
                'message': 'Requested collection is not List'
            }
        return self.response

    def flat_list(self, sub_list):
        """
        Flat sub list
        :param sub_list: list
        :return:
        """
        _list = list()
        for element in sub_list:
            if isinstance(element, list):
                _list += self.flat_list(element)
            else:
                _list.append(element)

        return _list
