from django.shortcuts import render

from django.contrib.auth.models import User
from postrapp.models import Post
from userprofile.models import UserProfileModel

# Create your views here.

def profile_view(request , username) : 

    user = User.objects.get(username=username)
    all_posts = Post.objects.filter(poster=user)
    userprofile = UserProfileModel.objects.get(baseUser=user)
    return render(request , "userprofile/view_profile.html" , context={"current_user":request.user , 'user':user , "all_posts":all_posts,
                                                                        "userprofile":userprofile})