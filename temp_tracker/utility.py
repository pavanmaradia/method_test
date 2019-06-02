"""
General utility
"""


def required_field_validation(payload, require_fields):
    """
    Validate required fields exists in payload or not
    :param payload:
    :param require_fields:
    :return:
    """

    payload_fields = set(payload.keys())
    intersect = set.intersection(payload_fields, require_fields)
    if intersect == set(require_fields):
        response = {
            'status': True,
            'message': 'Required parameters are available in request.'
        }
    else:
        fields = ', '.join(require_fields)
        response = {
            'status': False,
            'message': F'Required parameters are missing. ({fields}) requires.'
        }

    return response
