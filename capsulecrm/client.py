import requests
import requests.auth
import pprint
import json


class Client(object):
    BASE_URL = 'https://api.capsulecrm.com/api/'
    _VALID_VERSIONS = ['v2', ]

    def __init__(self, token, version=None):
        self.token = token
        if version not in self._VALID_VERSIONS:
            self.version = self._VALID_VERSIONS[0]

    def _post(self, endpoint, data=None):
        return self._request('post', endpoint, data=data)

    def _get(self, endpoint, data=None):
        return self._request('get', endpoint, data=data)

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
        """Returns the created tag.
        Args:
            entity: String [parties, opportunities, kases]
            name: String requerid
            description: String
            datatag: Boolean
        Returns:
            A dict.
        """
        data = {
            "tag": {
                "name": name,
                "description": description,
                "dataTag": datatag
            }
        }
        return self._post('{}/tags'.format(entity), data=data)

    def list_tag(self, entity, page=1, perpage=50):
        """Returns all created tags.
        Args:
            entity: String [parties, opportunities, kases]
            page: Integer
            perpage: Integer
        Returns:
            A dict.
        """
        data = {
            'page': page,
            'perPage': perpage
        }
        return self._get('{}/tags'.format(entity), data=data)

    def create_person(self, embed):
        """Returns the created person.
        Args:
            embed: Dict { 'firstName': String required, 'lastName': String required, 'title': String,
                          'jobTitle': String (Mr, Master, Mrs, Miss, Ms, Dr, Prof), 'organisation': String,
                          'about': String,
                          'addresses': dict { 'type': String (Home, Postal, Office),
                                              'street': String,
                                              'city': String,
                                              'state': String,
                                              'country': String,
                                              'zip': String },
                          'phoneNumbers': dict { 'type': String (Home, Work, Mobile, Fax, Direct),
                                                 'number': String required },
                          'websites': dict { 'service': String required (URL, SKYPE, TWITTER, LINKED_IN, FLICKR, GITHUB,
                                                                         YOUTUBE, INSTAGRAM, PINTEREST),
                                             'address': String required,
                                             'type': String (Home, Work),
                                             'url': String required },
                          'emailAddresses': dict { 'type': String (Home, Work),
                                                   'address': String required },
                          'tags': dict { 'id': Long,
                                         'name': String required,
                                         'description': String },
                          'fields': dict { 'id': Long,
                                           'value': Multiple requerid,
                                           'definition': dict requerid { 'id': Long,
                                                                         'name': String } }
        Returns:
            A dict.
        """
        data = {
            'party': {
                'type': 'person',
            }
        }
        data['party'].update(embed)
        return self._post('/parties', data=data)

    def create_organisation(self, embed):
        """Returns the created organisation.
        Args:
            embed: Dict { 'name': String required, 'about': String,
                          'addresses': dict { 'type': String (Home, Postal, Office),
                                              'street': String,
                                              'city': String,
                                              'state': String,
                                              'country': String,
                                              'zip': String },
                          'phoneNumbers': dict { 'type': String (Home, Work, Mobile, Fax, Direct),
                                                 'number': String required },
                          'websites': dict { 'service': String required (URL, SKYPE, TWITTER, LINKED_IN, FLICKR, GITHUB,
                                                                         YOUTUBE, INSTAGRAM, PINTEREST),
                                             'address': String required,
                                             'type': String (Home, Work),
                                             'url': String required },
                          'emailAddresses': dict { 'type': String (Home, Work),
                                                   'address': String required },
                          'tags': dict { 'id': Long,
                                         'name': String required,
                                         'description': String },
                          'fields': dict { 'id': Long,
                                           'value': Multiple requerid,
                                           'definition': dict requerid { 'id': Long,
                                                                         'name': String } }
        Returns:
            A dict.
        """
        data = {
            'party': {
                'type': 'organisation',
            }
        }
        data['party'].update(embed)
        return self._post('/parties', data=data)

    def list_parties(self, since=None, page=1, perpage=50, embed={}):
        """Returns the all parties.
        Args:
            since: Date
            page: Integer
            perpage: Integer
            embed: dict
        Returns:
            A dict.
        """
        data = {
            'since': since,
            'page': page,
            'perPage': perpage,
            'embed': embed
        }
        return self._get('/parties', data=data)

    def create_milestone(self, name, description, probability, complete=False):
        """Returns the create milestone.
        Args:
            name: String required
            description: String
            probability: Integer
            complete: Boolean
        Returns:
            A dict.
        """
        data = {
            'milestone': {
                'name': name,
                'description': description,
                'probability': probability,
                'complete': complete
            }
        }
        return self._post('/milestones', data=data)

    def list_milestone(self, page=1, perpage=50):
        """Returns the all milestones.
        Args:
            page: Integer
            perpage: Integer
        Returns:
            A dict.
        """
        data = {
            'page': page,
            'perPage': perpage
        }
        return self._get('/milestones', data=data)

    def create_oppotunity(self, embed):
        """Returns the created oppotunity.
        Args:
            embed: Dict { 'party': dict { 'id': Long required },
                          'name': String required, 'description': String,
                          'milestone': dict { 'id': Long required },
                          'value': dict { 'amount': Double required, 'currency': String },
                          'probability': Long
                        }
        Returns:
            A dict.
        """
        data = {
            'opportunity': {}
        }
        data['opportunity'].update(embed)
        return self._post('/opportunities', data=data)

    def list_opportunities(self, since=None, page=1, perpage=50, embed={}):
        """Returns the all parties.
        Args:
            since: Date
            page: Integer
            perpage: Integer
            embed: dict
        Returns:
            A dict.
        """
        data = {
            'since': since,
            'page': page,
            'perPage': perpage,
            'embed': embed
        }
        return self._get('/opportunities', data=data)