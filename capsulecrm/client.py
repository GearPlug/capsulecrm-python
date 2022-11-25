from urllib.parse import urlencode

import requests

from capsulecrm import exceptions
import json


class Client(object):
    AUTHORITY_URL = 'https://api.capsulecrm.com/'
    AUTH_ENDPOINT = 'oauth/authorise?'
    TOKEN_ENDPOINT = 'oauth/token'

    RESOURCE = 'https://api.capsulecrm.com/api/'
    _VALID_VERSIONS = ['v2', ]

    def __init__(self, client_id, client_secret, api_version=None):
        self.client_id = client_id
        self.client_secret = client_secret
        self.token = None
        if api_version not in self._VALID_VERSIONS:
            self.api_version = self._VALID_VERSIONS[0]
        self.base_url = self.RESOURCE + self.api_version + '/'

    def authorization_url(self, redirect_uri, scope=None, state=None):
        params = {
            'client_id': self.client_id,
            'redirect_uri': redirect_uri,
            'response_type': 'code',
        }
        if scope:
            params['scope'] = ' '.join(scope),
        if state:
            params['state'] = state
        return self.AUTHORITY_URL + self.AUTH_ENDPOINT + urlencode(params)

    def exchange_code(self, code):
        data = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'code': code,
            'grant_type': 'authorization_code',
        }
        return self._parse(requests.post(self.AUTHORITY_URL + self.TOKEN_ENDPOINT, data=data))

    def refresh_token(self, refresh_token):
        data = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'refresh_token': refresh_token,
            'grant_type': 'refresh_token',
        }
        return self._parse(requests.post(self.AUTHORITY_URL + self.TOKEN_ENDPOINT, data=data))

    def set_token(self, token):
        self.token = token

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
        return self._post('{}/tags'.format(entity), **data)

    def list_tag(self, entity, page=None, perpage=None):
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
        return self._get('{}/tags'.format(entity), params=data)

    def create_person(self, embed):
        """Returns the created person.
        Args:
            embed: Dict { 'firstName': String required, 
                          'lastName': String required, 
                          'title': String (Mr, Master, Mrs, Miss, Ms, Dr, Prof),
                          'jobTitle': String, 
                          'organisation': String,
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
        return self._post('/parties', **data)

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
        return self._post('/parties', **data)

    def list_parties(self, since=None, page=None, perpage=None, embed=None):
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
        return self._get('/parties', params=data)

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
        return self._post('/milestones', **data)

    def list_milestone(self, page=None, perpage=None):
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
        return self._get('/milestones', params=data)

    def create_oppotunity(self, embed):
        """Returns the created oppotunity.
        Args:
            embed: Dict { 'description' : String
                          'party': dict { 'id': Long required },
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
        return self._post('/opportunities', **data)

    def list_opportunities(self, since=None, page=None, perpage=None, embed=None):
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
        return self._get('/opportunities', params=data)

    def get_current_user(self):
        return self._get('/users/current')

    def list_users(self):
        return self._get('/users')

    def list_tasks(self, page=None, perpage=None, embed=None, since=None):
        """Returns the all tasks.
        Args:
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
        return self._get('/tasks', params=data)

    def create_task(self, embed):
        """Returns the created task.
        One of Party, Opportunity or Kase must be included
        Args:
            embed: Dict { 
                          'detail': String required,
                          'category': category ID.
                          'description': String,
                          'dueOn': String,
                          'dueTime': dict { 'amount': Double required, 'currency': String },
                          'oportunity': dict { 'id': Long required },
                          'party': dict { 'id': Long required },
                          'kase': dict { 'id': Long required },
                          'owner': dict { 'id': Long required },
                          'completedAt': String,
                        }
        Returns:
            A dict.
        """
        return self._post('/tasks', **{'task': embed})
    
    def list_projects(self, page=None, perpage=None, embed=None, since=None):
        """Returns the all tasks.
        Args:
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
        return self._get('/kases', params=data)
    
    def filter_order_data(self, entity, conditions=None, order_by=None, page=None, per_page=None, embed=None):
        """
        Perform structured searches on parties, projects and opportunities
        Args:
            entity: (str) parties, projects, opportunities
            conditions: array of (dict)
                field: entity field reference
                operator: some options are "is", "contains", "is greater than"
                value: variable used to filter depending on operator.
            order_by: array of (dict)
                field: entity field reference
                direction: "ascending" or "descending"
            page: (int)
            perpage: (int)
            embed: (str) separated by commas, supported values depending on entity
        """
        params = {
            'page': page,
            'perPage': per_page,
            'embed': embed
        }
        data = {
            "filter": {}
        }
        if conditions:
            data["filter"].update(conditions=conditions)
        if order_by:
            data["filter"].update(orderBy=order_by)
        return self._post(f'{entity}/filters/results', params=params, **data)
    
    def get_custom_fields(self, entity, page=None, per_page=None):
        """
        Returns custom fields for specific entity
        Entity options: parties, opportunities or kases
        """
        params = {
            'page': page,
            'perPage': per_page
        }
        return self._get(f'{entity}/fields/definitions', params=params)
    
    def list_countries(self):
        return self._get('/countries')

    def list_currencies(self):
        return self._get('/currencies')

    def list_categories(self):
        return self._get('/categories')

    def _get(self, url, **kwargs):
        return self._request('GET', url, **kwargs)

    def _post(self, url, **kwargs):
        return self._request('POST', url, **kwargs)

    def _put(self, url, **kwargs):
        return self._request('PUT', url, **kwargs)

    def _patch(self, url, **kwargs):
        return self._request('PATCH', url, **kwargs)

    def _delete(self, url, **kwargs):
        return self._request('DELETE', url, **kwargs)

    def _request(self, method, endpoint, headers=None, params=None, **kwargs):
        _headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + self.token['access_token']
        }
        if headers:
            _headers.update(headers)
        return self._parse(requests.request(method, 
                                            self.base_url + endpoint, 
                                            headers=_headers, 
                                            data=json.dumps(kwargs),
                                            params=params))

    def _parse(self, response):
        status_code = response.status_code
        if 'application/json' in response.headers['Content-Type']:
            r = response.json()
        else:
            r = response.text
        if status_code in (200, 201, 202):
            return r
        elif status_code == 204:
            return None
        elif status_code == 400:
            raise exceptions.BadRequestError(r)
        elif status_code == 401:
            raise exceptions.AuthenticationFailedError(r)
        elif status_code == 403:
            raise exceptions.ForbiddenError(r)
        elif status_code == 422:
            raise exceptions.ValidationFailedError(r)
        else:
            raise exceptions.UnknownError(r)
