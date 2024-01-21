# from django.db import models
from mongoengine import *
from djongo import models
from bson.objectid import ObjectId


class TimeSeriesData(models.Model):

    _id = models.ObjectIdField(primary_key=True, editable=False)
    # create a field that will auto insert current date time.
    updatedAt = models.DateTimeField()
    # string fields.
    temperature = models.TextField()



    # this is required to return the _id field
    objects = models.DjongoManager()

    def __str__(self):
        return self._id

