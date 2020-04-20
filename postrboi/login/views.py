from django.shortcuts import render
from django.contrib.auth.models import User
from login.forms import UserForm

# Create your views here.

def register(request) : 


    registered = False 

    if request.method == 'POST' : 

        print('posting !!!! .....')

        user_form = UserForm(request.POST)
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

    else : 

        user_form = UserForm()

    return render(request , 'login/base.html' , context={'user_form':user_form , 'registered':registered})

