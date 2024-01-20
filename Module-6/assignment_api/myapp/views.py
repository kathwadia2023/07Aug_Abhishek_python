from django.shortcuts import render
from .models import *
from .serial import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.

@api_view(['GET'])
def getall(request):
    if request.method=='GET':
        stdata = studinfo.objects.all()
        serial = stud_ser(stdata, many=True)
        # print(serial.data)
        return Response(serial.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET'])
def getstud(request,id):
    try:
        stid = studinfo.objects.get(id=id)
    except studinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serial = stud_ser(stid)
        return Response(serial.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE','GET'])
def deletestud(request,id):
    try:
        stid = studinfo.objects.get(id=id)
    except studinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serial = stud_ser(stid)
        return Response(serial.data)
    
    if request.method=='DELETE':
        studinfo.delete(stid)
        return Response(status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)