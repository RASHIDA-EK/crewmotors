from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth,User
from django.contrib.auth import logout
from .models import *
from django.db.models.query_utils import Q

from django.http.response import JsonResponse

def index(request):
    x = cars.objects.all()
    if 'fi' in request.COOKIES:
        q = request.COOKIES['fi']
        print(q)
    return render(request, 'index.html', {'a': x})

def views(request):
    y = request.GET['cat']
    z = cars.objects.filter(id=y)
    print(z)
    return render(request, 'booking.html', {'m':z})



def views2(request):
    a = request.GET['car']
    z = cars.objects.filter(id=a)
    print(a,'g')
    return render(request, 'booking.html', {'m':z}) 

   

def list(request):
    x = cars.objects.all()
    return render(request, 'car.html', {'a': x})

    

def part(request):
    a = parts.objects.all()
    print(a)
    return render(request, 'p_parts.html', {'b':a})


def login(request):
    if request.method=="POST":
        x = request.POST['first']
        y = request.POST['ps']
        print(x,y)
        if x != '' and y != '':
            valid = auth.authenticate(username=x,password=y)
            if valid is not None:
                auth.login(request,valid)
                firstname = User.objects.get(username=request.user)
                a =  redirect('/')
                a.set_cookie('fi',firstname.username)
                a.set_cookie('valid', True)
                return a
               
            
            else:
                a = "invalid username"
                return render(request, 'login.html',{'ms':a})
        else:
              a = "required field empty"
              return render(request, 'login.html',{'ms':a})

    else:
        return render(request, 'login.html')
    
def logout(request):
    auth.logout(request)
    r =redirect('index')
    r.delete_cookie('fi') 
    r.delete_cookie('valid') 
    return r

def register(request):
    if request.method == "POST":
        x = request.POST['first']
        y = request.POST['second']
        z = request.POST['user']
        a = request.POST['email']
        b = request.POST['pass']
        c = request.POST['repass']
        print(x,y,z,a,b,c)
        if z != '' and a != '' and b !='':

            if User.objects.filter(username=z).exists() or User.objects.filter(email=a).exists():

                a = "username or email already exists"
                return render(request, 'register.html',{'ms':a})
            elif b!=c:
                a = "incorrect password"
                return render(request, 'register.html',{'ms':a})    
            
            else:
                us = User.objects.create_user(first_name = x, last_name = y, username = z, email = a, password = b)
                us.save()
                auth.login(request,us)
                return redirect('/') 
                
        else:
              a = "required field empty"
              return render(request, 'register.html',{'ms':a})

        
    else:
        return render(request, 'register.html')
    
#about

def about(request):
    return render(request, 'about.html')   


#search

def search(request):

    if 'term' in request.GET:
        s = request.GET['term']

        t = cars.objects.filter(Q(cars_name__istartswith=s))
        a = []
      
        for i in t:
            a.append(i.cars_name)
        return JsonResponse(a,safe=False)
    return redirect('/')


def search2(request):
    x = request.POST['s']
    z = cars.objects.filter(cars_name=x)

    return render(request, 'booking.html', {'m':z}) 

    
    


# parts deatils

def parts_view(request):
    a1 = request.GET['cats']
    print(a1,"sam")
    b1 = detail.objects.filter(part=a1)
    print(b1,"partview")
    return render(request, 'parts_list.html',{'z':b1})



def part_details(request):
    b = request.GET['pv']
    print(b,"id")
    c = detail.objects.get(id=b)
    print("j",c)
    return render(request, 'partsview.html',{'m':c})

#services


def service(request):
    s = s_services.objects.all()
    print(s)
    return render(request, 's_service.html', {'z':s})


def s_details(request):
    v = request.GET['sp']
    w = s_services.objects.get(id=v)
    return render(request,'s_detail.html', {'x':w})


    
  