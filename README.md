# capsulecrm-python
Capsule CRM API wrapper written in python.

## Installing
```
pip install capsulecrm-python
```

## Requirements
- requests

## Usage
```
from capsulecrm.client import Client
client = Client(client_id, client_secret)
```

### Advanced filtering for parties, organisations and projects
```
# Example:
order_by= [{"field": "addedOn", "direction":"descending"}]
conditions= [{"field":"email", "operator": "is", "value": "juan@mail.com"}]
parties = client.filter_order_data('parties',conditions=conditions, order_by=order_by, page=1, per_page=1)
```

### Create Person or Organisation
```
client.create_person('embed')
client.create_organisation('embed')
```

### List Parties
```
client.list_parties('since, page, perpage, embed')
```

### Create and list Milestone
```
client.create_milestone('name, description, probability, complete')
client.list_milestone('page, perpage')
```

### Create and List Opportunities
```
client.create_oppotunity('embed')
client.list_opportunities('since, page, perpage, embed')
```

### Create and list tasks
```
client.create_task('embed')
client.list_tasks('since, page, perpage, embed')
```

### Create and list tags
```
client.create_tag('entity, name, description, datatag')
client.list_tag('entity, page, perpage')
```

### List projects, users, countries, currencies and categories
```
client.list_projects('since, page, perpage, embed')
client.list_users()
client.list_countries()
client.list_currencies()
client.list_categories()
```

### Get custom Fields by entity (parties, organisations or projects):
```
client.get_custom_fields('entity, page, perpage')
```
## TODO
- show_party
- show_multiple_parties
- update_party
- delete_party
- list_deleted_parties
- list_opportunities_by_party
- show_opportunity
- show_multiple_opportunities
- update_opportunity
- delete_opportunity
- list_deleted_opportunities
- list_additional_parties
- add_additional_party
- remove_additional_party
- delete tag
- show_tag
- update_tag
- delete_milestone
- show_milestone
- update_milestone
