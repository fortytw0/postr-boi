from itertools import chain

from django.shortcuts import render , redirect
from django.urls import reverse
from django.views import View
from django.http import HttpResponse

from postrapp.models import Post , Tag
from postrapp.forms import CreatePostForm , CreateTagForm
# Create your views here.


class IndexView(View) : 

    def get(self , request) : 

        all_posts = Post.objects.all()
        print(all_posts)
        current_user = request.user

        return render(request , "postrapp/index.html" , context={"all_posts" : all_posts,
                                                                "current_user" : current_user
                                                                })

class CreateView(View) : 

    def get(self, request) : 

        post_form = CreatePostForm()
        tag_form = CreateTagForm()

        tags_by_user = Tag.objects.filter(tag_creator=request.user)

        return render(request , "postrapp/create.html" , context={'post_form':post_form , 'user':request.user , 
                                                                    'tag_form':tag_form , 'current_user':request.user , 
                                                                    'tags_by_user':tags_by_user}) 

    def post(self , request) : 
        
        print("the request is : ")
        print(request.POST)

        if request.POST.get("action" , "") == 'post' : 

            post_form = CreatePostForm(request.POST)

            print(request.POST)

            if post_form.is_valid() : 

                post = post_form.save(commit=False)
                post.poster = request.user
                post.save()
                return redirect(reverse('postrapp:index_view'))

            else : 

                return HttpResponse("Whoops something went wrong...<br><br>"+post_form.errors)

        elif request.POST.get("action" , "") == 'tag' :

            tag_form = CreateTagForm(request.POST)

            print(request.POST)
            
            if tag_form.is_valid() : 

                tag = tag_form.save(commit=False)
                tag.tag_creator = request.user
                tag.save()
                return redirect(reverse('postrapp:index_view'))
            
            else : 

                return HttpResponse("Whoops something went wrong...<br><br>"+tag_form.errors)

        else : 

            return HttpResponse("What tomfuckery have you been upto?")

class TagView(View) : 

    def get(self , request , tag_name) :
        
        tag = Tag.objects.get(tag_name = tag_name.upper())

        all_posts = chain(Post.objects.filter(tag_1 = tag),Post.objects.filter(tag_2 = tag) , \
                    Post.objects.filter(tag_3 = tag) , Post.objects.filter(tag_4 = tag))

        context = {"all_posts" : all_posts , "tag" : tag, "current_user":request.user}

        return render(request , "postrapp/view_tag.html" , context=context)






