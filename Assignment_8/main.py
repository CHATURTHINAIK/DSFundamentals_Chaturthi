import json
import pymongo

data = {}
with open("data.json") as file:
    data = json.load(file)

city_country = {
    'new_york':'usa',
    'dallas':'usa',
    'beijing':'china',
    'colombo':'sri_lanka',
    'hong_kong':'china',
    'kandy':'sri_lanka',
    'wuhan':'china',
    'chicago':'usa'
}

print(data['visa_rates'][city_country['beijing']])

myclient = pymongo.MongoClient('')

db = myclient['passenger_management_system']
collection = db['tickets']

print('='*50)
print('TICKETS')
print('='*50)

for t in db['tickets'].find({}):
    total = data['visa_rates'][city_country[t['visa_stamped_location'][-1]]] + int(t['ticket_price'])

    print(f"\nTicket ID: {t['tiket_id']}")
    print(f"\nPassenger Name: {t['passenger_name']}")
    print(f"\nVisa Stamped Locations: {','.join(t['visa_stamped_locations'])}")
    print(f"\nTicket Price: Rs.{t['tiket_price']}")
    print(f"\nDestination: Rs.{t['destination']}")
    print(f"\nTotal Price: Rs.{t['total']}")
    print('='*50)