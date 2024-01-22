from django.shortcuts import render, redirect
from .models import *
from .serial import *
from .forms import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.

def index(request):
    if request.method=='POST':
        data=blogform(request.POST)
        if data.is_valid(): #true
            data.save()
            print("Your data has been saved!")
        else:
            print(data.errors)
    return render(request, 'index.html')

def showdata(request):
    data=blog_data.objects.all()
    return render(request,'showdata.html',{'data':data})

def update(request, id):
    stid=blog_data.objects.get(id=id)
    if request.method=='POST':
        data=blogform(request.POST,instance=stid)
        if data.is_valid(): #true
            data.save()
            print("Your data has been updated!")
            return redirect('showdata')
        else:
            print(data.errors)
    return render(request, 'update.html',{'stid':stid})

def deletedata(request,id):
    stid=blog_data.objects.get(id=id)
    blog_data.delete(stid)
    return redirect('showdata')


@api_view(['GET'])
def getall(request):
    if request.method=='GET':
        stdata = blog_data.objects.all()
        serial = blog_ser(stdata, many=True)
        # print(serial.data)
        return Response(serial.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET'])
def getstud(request,id):
    try:
        stid = blog_data.objects.get(id=id)
    except blog_data.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serial = blog_ser(stid)
        return Response(serial.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE','GET'])
def deletestud(request,id):
    try:
        stid = blog_data.objects.get(id=id)
    except blog_data.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serial = blog_ser(stid)
        return Response(serial.data)
    
    if request.method=='DELETE':
        blog_data.delete(stid)
        return Response(status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)