import requests
import requests.auth
import pprint
import json


class Client(object):
    BASE_URL = 'https://api.capsulecrm.com/api/'
    _VALID_VERSIONS = ['v2', ]

    def __init__(self, name, token, version=None):
        self.name = name
        self.token = token
        if version not in self._VALID_VERSIONS:
            self.version = self._VALID_VERSIONS[0]

    def _post(self, endpoint, data=None):
        return self._request('post', endpoint, data=data)

    def _get(self, endpoint, params=None):
        return self._request('get', endpoint)

    def _request(self, method, endpoint, data=None, headers={}):
        headers = {
            'Accept': 'application/json',
            'Authorization': 'Bearer {0}'.format(self.token),
            'Content-Type': 'application/json'
        }
        url = '{0}{1}/{2}'.format(self.BASE_URL, self.version, endpoint)
        result = requests.request(method, url, headers=headers, data=json.dumps(data))
        return result.text

    def create_tag(self, entity, name, description, datatag):
        data = {
            "tag": {
                "name": name,
                "description": description,
                "dataTag": datatag
            }
        }
        return self._post('{}/tags'.format(entity), data=data)


f = Client('GearPlug', 'PNbfNbIj38uoddcH6huxiy0FBBP/XfMwMaeb9jVwGcsSu66BsFakMZQKfTlBcdPh')
tag = f.create_tag('parties')