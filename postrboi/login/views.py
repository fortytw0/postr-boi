from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login
from login.forms import UserForm
from django.urls import reverse
from django.shortcuts import redirect
from django.http import HttpResponse
import datetime

# Create your views here.

def register(request) : 


    registered = False 
    

    if request.method == 'POST' : 

        print('posting !!!! .....')

        user_form = UserForm(request.POST)
        print('user_form')
        print(user_form)
        print('request.POST')
        print(request.POST)

        if user_form.is_valid() : 

            user = user_form.save()

            user.set_password(user.password)
            user.save()

            print('User model has been saved....')
            print('USER : ' , user)

            registered = True

        else : 

            print(user_form.errors)
            return render(request , 'login/base.html' , context={'user_form':user_form , 'registered':registered , 'signup':True})

    else : 

        user_form = UserForm()

    return render(request , 'login/base.html' , context={'user_form':user_form , 'registered':registered , 'signup':True})


def signin(request) : 

    login_successful = False
    
    print('setting session test cookie...')
    request.session.set_test_cookie()

    print("Has the test cookie worked?")
    print(request.session.test_cookie_worked())

    if request.session.test_cookie_worked() : 
        request.session['cookies_accepted'] = True
        request.session.delete_test_cookie()
        


    
    if request.method == 'POST' : 

        print('authenticating...')

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username , password=password)

        if user : 

            if user.is_active :

                login(request , user)
                now = datetime.datetime.now()
                # request.session['last_signin'] = now.strftime("%d %m %Y , %H:%M:%S")
                return redirect(reverse('blog:index_view'))

            else :

                return HttpResponse('<h1>USER IS NOT ACTIVE!</h1>')

        else : 
            
            return HttpResponse('<h1>login credentials invalid!</h1>')

        
    else: 

        return render(request , 'login/base.html' , context={'login':True})


                





