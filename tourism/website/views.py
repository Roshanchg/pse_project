from django.shortcuts import render
from django.shortcuts import redirect
from website.models import Users,Destinations,Packages,Bookings
from django.contrib.sessions.models import Session
from django.http import Http404
import datetime
# Create your views here.
def index(request):  
    context={'session':get_session_context(request=request),
             'top_packages':get_top_packages(request=request,Type=None,all_packages=False),
             'pop_packages':get_popular_packages(request=request)}  
    return render(request=request,template_name="index.html",context=context)

def update_section(request):
    all_packages=request.GET.get('all',False)
    mytype=request.GET.get("type",None) 
    context={'session':get_session_context(request=request),
             'top_packages':get_top_packages(request=request,Type=mytype,all_packages=all_packages),
        }
    return render(request, "package_section.html", context=context)

def loginform(request):
    if request.method=="POST":
        email=request.POST["email"]
        password=request.POST["password"]
        context={'alert':'Email is not registered'}
        if email_exists(email=email):
            if(authenticate(email=email,password=password)):
                time=0
                if 'remember' in request.POST:
                    time=2592000
                store_session(request=request,email=email,password=password,time=time)
                return redirect("website:index")
            
            else:
                context={'alert':'Incorrect email or password'}
                return render(request=request,template_name="loginform.html",context=context)
        return render(request=request,template_name="loginform.html",context=context)
    else:
        context=get_session_context(request=request)
        if context :
            return render(request=request,template_name="index.html",context=context) 
        return render(request=request,template_name="loginform.html")

def regform(request):
    if request.method=="POST":
        fullname=request.POST["fullname"]
        regemail=request.POST["reg-email"]
        regpassword=request.POST["reg-password"]
        context={'alert':"This Email Already Exists"}
        if email_exists(email=regemail):
            return render(request=request,template_name="regform.html",context=context)
        else:
            if (add_new_user(name=fullname,email=regemail,password=regpassword)):
                store_session(request=request,email=regemail,password=regpassword)
                return redirect(to="website:index")
            else:
                context={'alert':"Internal Server Error"}                
                return render(request=request,template_name="regform.html",context=context)
    return render(request=request,template_name="regform.html")

def account(request):
    details=get_user_details(request=request)
    if not details:
        return redirect(to="website:login")
    return render(request=request,template_name="account.html",context=details)

def accountedit(request):
    details=get_user_details(request=request)
    if request.method=="POST":
        uid=details['uid']
        name=request.POST['edit-name']
        email=request.POST['edit-email']
        try :
            gender=request.POST['edit-gender']
        except:    
            gender=None    
        country=request.POST['edit-country']        
        nickname=request.POST['edit-nickname']        
        edit_user_details(id=uid,name=name,email=email,gender=gender,nickname=nickname,country=country)
        details=get_user_details(request=request)
        return render(request=request,template_name="accountedit.html",context=details)
    if not details:
        return redirect(to="website:login")
    return render(request=request,template_name="accountedit.html",context=details)

def logout(request):
    clear_session(request=request)
    return redirect(to='website:login')

def email_exists(email):
    return Users.objects.filter(email=email).exists()

def make_bookings(request):
    pid=request.GET.get('id',None)
    date=request.GET.get('date',None)
    if not pid:
        return redirect("website:index")
    uid=request.session.get['uid']
    if not uid > 1:
         return redirect("website:login")
    else: 
        place_booking(request=request,uid=uid,pid=pid)
        return redirect("website:index")
def place_booking(request,uid=None,pid=None,dtb=datetime.date.today()):
    if uid or pid is None:
        print("SERVER ERROR")
        return redirect("website:index")
    booking=Bookings(dateToBoook=dtb,package_id=pid,user_id=uid,approved=False)
    booking.save()
    return 
    
def delete_account(request):
    uid=request.session['uid']
    user=Users.objects.filter(id=uid).first()
    user.delete()
    clear_session(request=request)
    return redirect("website:index")

# POST to DATABASE "Users"
def add_new_user(name,email,password):
    try:
        newuser=Users(name=name,email=email,password=password)
        newuser.save()
        print(f" Added User of Name: {name},Email: {email} and Password: {password} ")
        return True
    except Exception as e:
        print(e,"\n")
        return False
def edit_user_details(id,name,email,gender,nickname,country):
    user=Users.objects.filter(id=id).first()
    user.email=email
    user.gender=gender
    user.nickname= nickname if nickname!='' or not nickname else "None"
    user.country=country
    user.name=name
    user.save()
def authenticate(email,password):
    try:
        user=Users.objects.all().get(email=email)
        if user.password==password:        
            return True
        else:
            return False
    except:
        return False
    
def get_uid(email):
    return Users.objects.filter(email=email).first().id

def store_session(request,email,password,time=0):
    request.session['email']=email
    request.session['password']=email
    request.session['uid']=get_uid(email=email)
    request.session.set_expiry(time)

def get_session_context(request):
    uid=request.session.get('uid')
    email=request.session.get('email')
    password=request.session.get('password')
    context={'uid':uid,'email':email,'password':password}
    if not uid or not email or not password:
        return None
    return context 

def get_user_details(request):
    try:
        uid=request.session.get('uid')
        user=Users.objects.filter(id=uid).first()
        email=user.email
        name=user.name
        nickname=user.nickname
        country=user.country
        gender=user.gender
        profile=user.profile
        doj=user.date
        details={'uid':uid,'email':email,
                 'name':name,
                 'nickname':nickname,'country':country,
                 'gender':gender,'profile':profile,
                 'doj':doj}
        return details
    except:
        return 

    

def clear_session(request):
    session_key = request.session.session_key

    if session_key:
        try:
            Session.objects.get(session_key=session_key).delete()
        except Session.DoesNotExist:
            pass  
    request.session.flush()  


def get_top_packages(request,Type=None,all_packages=False):
    if not Type:
        all_data = Packages.objects.select_related('destination').order_by('bookingcount')
    else:
        all_data = Packages.objects.select_related('destination').filter(ptype__icontains=Type).order_by('bookingcount')
    if all_packages!=False:
        return all_data
    else:
        return all_data[:3]
    
def get_popular_packages(request):
    all_data = Packages.objects.select_related('destination').filter(destination__in=[1,2,12])[:4]
    return all_data