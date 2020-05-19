from django.shortcuts import render , redirect
from django.urls import reverse
from django.http import HttpResponse

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

import datetime
from blog.forms import PostForm , TagForm
from blog.models import Post , Tag , User

# Create your views here.

@login_required
def index(request) : 

    all_posts = Post.objects.all()

    if len(all_posts) > 25 : 
        all_posts = all_posts[:25]

    current_user = request.user

    return render(request, "blog/base.html" , context={'all_posts' : all_posts , 'current_user' : current_user})


@login_required
def logout_view(request) : 

    print(request.user)
    logout(request)
    return redirect(reverse('login:login'))

@login_required
def create_view(request) : 

    if request.method == 'POST' : 

        if request.POST['action'] == 'post' : 

            post_form = PostForm(request.POST)
            
            if post_form.is_valid() :        
                
                post = post_form.save(commit=False)
                post.poster = request.user
                post.save()

                return redirect(reverse('blog:index_view'))

            else : 
                print('Looks like post was not valid.')
                print(post_form.errors)

        if request.POST['action'] == 'tag' : 

            tag_form = TagForm(request.POST)

            if tag_form.is_valid() : 

                tag_creator = request.user
                print(tag_creator)
                return redirect(reverse('blog:index_view'))

            else : 
                return(HttpResponse('<h1>LOOKS LIKE TAG WAS INCOMPLETE.</h1>'))

    else : 

        post_form = PostForm()
        tag_form = TagForm()

        return render(request , 'blog/create.html' , context={'post_form':post_form , 'tag_form':tag_form})



