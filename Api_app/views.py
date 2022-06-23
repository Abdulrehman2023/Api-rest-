import json
from telnetlib import STATUS
from urllib import request
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from django.http import HttpResponse,JsonResponse
# Create your views here.
from rest_framework.parsers import JSONParser
from .serializer import AddressSerial
from .models import *
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


class article(APIView):

   def get(self, request, format=None):
        snippets = APi_default.objects.all()
        serializer = AddressSerial(snippets, many=True)
        return Response(serializer.data)

   def post(self, request, format=None):
        serializer = AddressSerial(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




















@api_view(['GET', 'POST'])
def new1(request):
    
    if request.method=="GET":
        QuerySet = APi_default.objects.all()
        serializer = AddressSerial(QuerySet,many=True)
        print(serializer)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = AddressSerial(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'PUT', 'DELETE','PATCH'])
def new_details(request,pk):
    try:
        data_get = APi_default.objects.get(pk=pk)
    
    except data.DoesNotExist:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    if request.method== "GET":
        serializer = AddressSerial(data_get)
        return Response(serializer.data)

    elif request.method== "PUT":
        serializer = AddressSerial(data_get, data=request.data, partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    elif request.method == "DELETE":
        print("i am in delete response")
        data_get.delete()
        return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PATCH":

        testmodel_object = APi_default.objects.get(pk=pk)
        serializer = AddressSerial(testmodel_object, data=request.data, partial=True) # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
