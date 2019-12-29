import json
from persistqueue import PDict

qStore = PDict('data', 'qStore')


def wall(uri, handler):
    bypass_endpoints = ['reload']
    if uri.split('?')[0] in bypass_endpoints:
        return False, None

    _autocomplete_live = 'autocomplete_is_live' in qStore and qStore['autocomplete_is_live']
    _classifier_live = 'classifier_is_live' in qStore and qStore['classifier_is_live']

    if not _autocomplete_live or not _classifier_live:
        return True, json.dumps([])
    return False, None
