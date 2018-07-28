from mongoengine import *

import mlab

class Customer(Document):
    name = StringField()
    age = IntField()
    address = StringField()
    ref = StringField()
    meta = {'collection':'customers'}

mlab.connect()
ads_count = len(Customer.objects(ref__icontains = 'ads'))
wom_count = len(Customer.objects(ref__icontains ='wom'))
event_count = len(Customer.object(ref__icontains = 'events'))
