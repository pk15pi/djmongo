from django.shortcuts import render
# from rest_framework import exceptions, viewsets
from rest_framework_mongoengine import viewsets
from .models import *
from .serializers import *
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

class TimeSeriesView(viewsets.ModelViewSet):
    queryset = TimeSeriesData.objects.all()
    serializer_class = TSSerialiser


    def get_queryset(self, **kwargs):
        qs = super().get_queryset()

        # this is how you can add custom filters
        # accept resorce params from request body and filter all the docs having source as received source value
        source = self.request.query_params.get('source')
        p_key = self.request.query_params.get('p_key')

        # in sql : select * from TimeSeriesData where source='source' 
        if source:
            return qs.filter(source=source)

        # get record by id
        if p_key:
            print(p_key)
            return TimeSeriesData.objects.get(pk=p_key)


        # in sql : select * from TimeSeriesData 
        return qs



@api_view(['DELETE'])
def delRecords(request):
    obj = request.GET.get('obj')
    id = request.GET.get('_id')
    # res = TimeSeriesData.objects.filter(_id=id)
    res = TimeSeriesData.objects.get(_id=ObjectId(id))
    print(res._id)
    res.delete()
    return Response("Deleted Successfully")


@api_view(['UPDATE','PATCH','PUT'])
def updateRecords(request):
    id = request.GET.get('_id')
    # res = TimeSeriesData.objects.filter(_id=id)
    res = TimeSeriesData.objects.get(_id=ObjectId(id))
    res.temperature = request.data['temperature']
    res.updatedAt = request.data['updatedAt']
    res.save()
    return Response("Updated Successfully")
