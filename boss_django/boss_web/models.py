from django.db import models
from mongoengine import *
# Create your models here.
from mongoengine import connect
connect('Boss',host='localhost',port=27017)
# ORM
class CareerInfo(Document):
    location = StringField()
    title = StringField()
    education = StringField()
    img = StringField()
    company = ListField(StringField())
    salary = StringField()
    experience = StringField()
    type = StringField()
    meta = { 'collection': 'details2'}

