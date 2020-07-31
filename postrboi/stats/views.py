from django.shortcuts import render
from django.views.generic import View

from django.contrib.auth.models import User

# Create your views here.
class SiteView(View) : 

    def get(self , request) :
        current_user = request.user
        return render(request , "stats/site_stats.html" , context={"current_user":current_user})

class UserView(View) : 

    def get(self , request , username) : 
        
        user = User.objects.get(username=username)
        current_user = request.user

        return render(request , "stats/user_stats.html" , context={"user":user , "current_user" : current_user})