from mongoengine import *

class New_bike(Document):
    model = StringField()
    daily_fee = IntField()
    image = StringField()
    year = IntField()