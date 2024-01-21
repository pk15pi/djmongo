from rest_framework import serializers
from .models import *



class TSSerialiser(serializers.ModelSerializer):
    _id = serializers.CharField(read_only=True)
    class Meta:
        model = TimeSeriesData
        fields = '__all__'

