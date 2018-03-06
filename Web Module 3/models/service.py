from mongoengine import Document, StringField, IntField, BooleanField, ImageField
#create collection
class Service(Document):
    name = StringField()
    yob = IntField()
    gender = IntField() #0: Female, 1: male
    height = IntField()
    phone = StringField()
    address = StringField()
    status = BooleanField()
    description = StringField()
    photo = StringField()
    measurement = StringField()
