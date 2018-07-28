from mongoengine import *

import mlab

class Customers(Document):
    name = StringField()
    age = IntField()
    address = StringField()
    ref = StringField()
    meta = {'collection':'customers'}

mlab.connect()
ads_count = len(Customers.objects(ref__icontains = 'ads'))
wom_count = len(Customers.objects(ref__icontains ='wom'))
event_count = len(Customers.object(ref__icontains = 'events'))
