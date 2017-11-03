# capsulecrm-python
Capsule CRM API wrapper written in python.

## Installing
```
pip install git+git://github.com/GearPlug/capsulecrm-python.git
```

## Requirements
- requests

## Usage
```
from capsulecrm.client import Client
client = Client('TOKEN')
```

Create Tag
```
client.create_tag('ENTITY, NAME, DESCRIPTION, DATATAG')
```

List Tags
```
client.list_tag('ENTITY, PAGE, PERPAGE')
```

Create Person
```
client.create_person('EMBED')
```

Create Organisation
```
client.create_organisation('EMBED')
```

List Parties
```
client.list_parties('SINCE, PAGE, PERPAGE, EMBED')
```

Create Milestone
```
client.create_milestone('NAME, DESCRIPTION, PROBABILITY, COMPLETE')
```

List Milestone
```
client.list_milestone('NAME, DESCRIPTION, PROBABILITY, COMPLETE')
```

Create Opportunity
```
client.create_oppotunity('EMBED')
```

List Opportunities
```
client.list_opportunities('EMBED')
```

## TODO
- show_party
- show_multiple_parties
- update_party
- delete_party
- list_employees
- list_deleted_parties
- search_parties
- list_opportunities_by_party
- show_opportunity
- show_multiple_opportunities
- update_opportunity
- delete_opportunity
- list_deleted_opportunities
- search_opportunities
- list_additional_parties
- add_additional_party
- remove_additional_party
- delete tag
- show_tag
- update_tag
- delete_milestone
- show_milestone
- update_milestone
