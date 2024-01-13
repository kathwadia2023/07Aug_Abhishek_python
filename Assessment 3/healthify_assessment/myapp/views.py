from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth import logout
from django.core.mail import send_mail
# from Healthify_assessment import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password,check_password
from healthify_assessment import settings
import requests
import random

# Create your views here.

def index(request):
    msg=""
    if request.method=='POST':
        newuser=signupForm(request.POST)
        if newuser.is_valid():
            email_user=newuser.cleaned_data.get('email')
            try:
                usersignup.objects.get(email=email_user)
                print("Email user is already exists!")
                msg="Email user is already exists!"
            except usersignup.DoesNotExist:
                
               
                print("Signup Successfully!")
                msg="Signup Successfully!"
                global fotp
                fotp = random.randint(1000,9999)
                
                subject = 'Your OTP Verfication'
                message = f"Hi your OTP is {fotp}, thank you for choosing us"
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [ request.POST['email'], ]
                send_mail( subject, message, email_from, recipient_list )
                global temp
               
                temp= {
                "name":request.POST["firstname"],
                "email":request.POST["email"],
                "password":request.POST["password"],
               
                }
                newuser.save()
                return render(request,'otp_verify.html')
            else:
                print(newuser.errors)

        elif request.POST.get('login')=='login':
            email_u = request.POST['email']
            pswd = request.POST['password']
            r =request.POST['role']

            user=usersignup.objects.filter( email = email_u, password=pswd,role=r)           
            c_id = usersignup.objects.get(email = email_u)
            print("Current ID:",c_id.id)
            c_role=c_id.role
            print("Current Role:",c_role)

            if user:
               
                print("login Success")
                # msg = "login Success"
                status = True
                request.session['user']= email_u
                request.session['c_role']= c_role
                return redirect("appointment")
            else:
                print("Login fail ,plz try again!!!")

    
        else:
            print(newuser.errors)
            msg="Something went wrong...Try again!"
    return render(request,'index.html',{'msg':msg})





def otp(request):
    global fotp
    global msg
    if request.method=="POST":

        if request.POST['otp'] == str(fotp):
           
            return render(request,'index.html')
        else:
            return render(request,'otp_verify.html',{'msg':'OTP not match'})
    else :
        return render(request,'register.html')

def about(request):
    return render(request,'about.html')




def contact(request):
    if request.method == "POST":
        newfeedback = Feedback_form(request.POST)
        if newfeedback.is_valid():
            newfeedback.save()
            print("Feedback saved")
            ran_otp = random.randint(11111,99999)
        # send mail
            sub="Thank you"
            message = f"Hello {request.POST['name']}! \n\nWe have Received Your feedback.\nWe will contact you shortly...\nIf any Queries, plz feel free to contact us...\nRegards \nHealthify Company PVT. LTD.\n Mo: +91 95866 32371"
            frm_mail = settings.EMAIL_HOST_USER
            to_mail=['djangotestingpython@gmail.com', request.POST['email']]
            send_mail(subject=sub, message=message, from_email=frm_mail, recipient_list=to_mail)
        
        
        
        else:
            print(newfeedback.errors)
    return render(request,'contact.html') 

def profile(request):
    return render(request,'profile.html')


def resetpass(request):
    msg = ""
    status = False
    if request.method == "POST":
        email_f = request.POST['email']
        mob_f = request.POST['mobile']
        try:
            user = usersignup.objects.get(email=email_f, mobile=mob_f)
            uid = user.id
            print("User id:", uid)
            request.session['uid']=uid
            status=True
            print("Email and Mobile number found...")
            msg = 'Email and Mobile number found...'
            return redirect('newpass')
        except:
            print("Error! Not Found...")
            msg = "Sorry! not found plz try again"
    return render(request, 'resetpass.html', {'msg':msg, 'status':status})


def newpass(request):
    uid = request.session.get('uid')
    cuid = usersignup.objects.get(id = uid)
    if request.method == 'POST':
        new_pass = update_form(request.POST)
        if new_pass.is_valid():
            new_pass = update_form(request.POST, instance=cuid)
            new_pass.save()
            print("Password is updated")
            return redirect('/')
        else:
            print("Error!!!!")
    return render(request, 'newpass.html')


def appointment_req(request):
    # global status
    user = request.session.get('user')
    c_role = request.session.get('c_role')
    data=appointment.objects.all()
     
    # c_email = request.session.get('email')

    if request.method == "POST":
        pat_app = appointment_form(request.POST, request.FILES)
        if pat_app.is_valid():
            pat_app.save()
            print("Appointment saved")
           
            
        # send mail
            sub="Thank you"
            message = f"Hello {request.POST['name']}! \n\nYour appointment is booked.\n\nIf any Queries, plz feel free to contact us...\nRegards \nHealthify Company PVT. LTD.\n Mo: +91 95866 32371"
            frm_mail = settings.EMAIL_HOST_USER
            to_mail=['djangotestingpython@gmail.com', request.POST['email']]
            send_mail(subject=sub, message=message, from_email=frm_mail, recipient_list=to_mail)
        else:
            print(pat_app.errors)
            print("Sorry Try again")
    return render(request,'appointment.html', {'c_role':c_role, 'user':user, 'data':data, 'id':id})

def grantappointment(request):
    
    # user_id = appointment.objects.get(id= id)
    # # user_email = user_id.email
    # print("the email of patient is :", user_id)
    
    user = request.session.get('user')

    if request.method == "POST":
        app_g = app_g_form(request.POST)
        print("Patient app name: ", app_g)
        if app_g.is_valid():
            app_g.save()
            print("Doctor scheduled the appointment")
            # p_id = appointment.objects.get(id=id)
            # p_name = p_id.patient_name
            # p_mail = p_id.email
            # print("Email of patient :", p_mail)
            # print("Name of patient :", p_name)
            
            
            # send mail
            sub="Doctor's Appointment "
          
            message = f"Hello Patient {request.POST['p_name']} ! \n\nYour Appoitnment is booked\nThe Date: {request.POST['date']}\nTimings: {request.POST['time']}  \nIf any Queries, plz feel free to contact us...\nRegards \nHealthify Company PVT. LTD.\nMo: +91 95866 32371"
            frm_mail = settings.EMAIL_HOST_USER
            to_mail=['djangotestingpython@gmail.com', request.POST['email']]
            send_mail(subject=sub, message=message, from_email=frm_mail, recipient_list=to_mail)
            return redirect('appointment')
        else:
            print(app_g.errors)
            print("Error!")
    return render(request,'grantappointment.html')




def user_logout(request):
    logout(request)
    return redirect('/')
