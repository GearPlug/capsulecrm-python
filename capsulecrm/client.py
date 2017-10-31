import requests
import requests.auth
import pprint
import webbrowser

class Client(object):
    BASE_URL = 'https://api.capsulecrm.com/api/'
    _VALID_VERSIONS = ['v2', ]

    def __init__(self, token, version=None):
        self.token = token,
        if version not in self._VALID_VERSIONS:
            self.version = self._VALID_VERSIONS[0]


    def _get(self, endpoint, params=None):
        return self._request('GET', endpoint, params)

    def _post(self, endpoint, params=None):
        return self._request('POST', endpoint, params)

    def _request(self, method, endpoint, params=None, data=None):
        url = '{0}{1}/{2}'.format(self.BASE_URL, self.version, endpoint)
        response = requests.request(method, url, params=params, json=data)
        r = response.json()
        return r

    def create_tag(self, entity):
        params = {'token': self.token}
        return self._post('{0}/tags'.format(entity), params=params)

f = Client('PNbfNbIj38uoddcH6huxi9OgVyImNul3oofS38ZbzmugVvb4RtSWqDLfNCHNE9kH')
pprint.pprint(f)
tag = f.create_tag('parties')
pprint.pprint(tag)