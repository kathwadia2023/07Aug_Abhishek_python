from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')


def gogreen(request):
    return render(request, 'go_green.html')

def contact(request):
    return render(request, 'contact.html')

def event(request):
    return render(request, 'event.html')

def com_member(request):
    return render(request, 'com_member.html')