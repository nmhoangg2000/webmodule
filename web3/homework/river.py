from mongoengine import Document, StringField, IntField

class River(Document):
    name = StringField()
    length = StringField()
    continent = IntField()