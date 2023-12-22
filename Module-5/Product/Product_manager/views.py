from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):
    if request.method == 'POST':
        pro_n=request.POST['product_name']
        pro_m=request.POST['product_model_name']
        pro_c=request.POST['product_colour']
        pro_p=request.POST['product_price']
        
        product_data.objects.create(product_name=pro_n,product_model_name=pro_m, product_colour=pro_c,product_price=pro_p)
        print("Record inserted")
    else:
        print("Error")
    return render(request,'index.html')

def show_data(request):
    data = product_data.objects.all()
    return render(request, 'show_data.html',{'data':data})

def update_data(request,id):
    stid = product_data.objects.get(id=id)
    if request.method == 'POST':
        pro_n=request.POST['product_name']
        pro_m=request.POST['product_model_name']
        pro_c=request.POST['product_colour']
        pro_p=request.POST['product_price']
        
        product_data.objects.filter(id=id).update(product_name=pro_n,product_model_name=pro_m, product_colour=pro_c,product_price=pro_p        )
        print("Success")
        return redirect('show_data')
    else:
        print("error")

    return render(request, 'update_data.html', {'stid':stid})

def delete_data(request,id):
    stid = product_data.objects.get(id=id)
    product_data.delete(stid)
    return redirect('show_data')