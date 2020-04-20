from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

import random
import string

# Create your models here.






class Tag(models.Model) : 

    tag_name = models.CharField(max_length=8 , unique=True) 
    tag_creator = models.ForeignKey(User , on_delete=models.CASCADE)
    tag_slug = models.SlugField(max_length=50 , default="" , null=True)

    seen_count = models.IntegerField(default=0)
    click_count = models.IntegerField(default=0)
    reccomended_count = models.IntegerField(default=0)

    def __str__(self):
        return self.tag_name

    def save(self, *args, **kwargs):

        self.tag_slug = slugify(self.tag_name)
        self.tag_name = self.tag_name.upper()


        if (self.pk is False) : 
            Tag.objects.create(tag_name=self.tag_name , tag_slug=self.tag_slug , tag_creator=self.tag_creator)

        return super(Tag , self).save(*args, **kwargs)

        

    
                
class Post(models.Model) : 

    poster = models.ForeignKey(User , on_delete = models.CASCADE)
    content = models.CharField(max_length=256)
    hyperlink = models.URLField(max_length=256 , null=True , blank=True , unique=True)
    feature_image = models.ImageField(verbose_name="Background Image" , blank=True , null=True)
    
    tag_1 = models.ForeignKey(Tag , on_delete=models.CASCADE , related_name="high_prio_tag" , blank=True , null=True)
    tag_2 = models.ForeignKey(Tag , on_delete=models.CASCADE , related_name="moderate_prio_tag", blank=True , null=True)
    tag_3 = models.ForeignKey(Tag , on_delete=models.CASCADE , related_name="low_prio_tag", blank=True , null=True)
    tag_4 = models.ForeignKey(Tag , on_delete=models.CASCADE , related_name="least_prio_tag", blank=True , null=True)
    
    seen_count = models.IntegerField(default=0)
    click_count = models.IntegerField(default=0)
    read_count = models.IntegerField(default=0)

    def save(self, if_new_profile=False, *args , **kwargs):

        self.hyperlink = self.hyperlink.replace("http://","")
        self.hyperlink = self.hyperlink.replace("www.", "") 
        self.hyperlink = self.hyperlink.replace("https://","")
        
        # if (self.pk is False) : 
        #     new_user_profile = UserProfile.objects.create(user=self.user , user_slug=self.user_slug)
        #     new_user_profile.posts_clicked.add(self.posts_clicked)


        return super(Post, self).save(*args, **kwargs)


    def __str__(self):
        return self.content


class UserProfile(models.Model) : 

    user = models.OneToOneField(User , on_delete=models.CASCADE)

    user_slug = models.SlugField(max_length=50 , default = "")

    posts_clicked = models.ManyToManyField(Post , related_name="this_user_has_clicked_posts" , blank=True)
    posts_reccommended = models.ManyToManyField(Post , blank=True)

    tags_clicked = models.ManyToManyField(Tag , related_name="this_user_has_clicked_tags"  , blank=True)
    tags_recommended = models.ManyToManyField(Tag  , blank=True)

    invited_by = models.ForeignKey(User , on_delete = models.CASCADE , related_name="inviter"  , blank=True , null = True)
    invitations_held = models.IntegerField(default=0)

    number_of_tags_invented = models.IntegerField(default=0)

    


    def save(self, if_new_profile=False, *args , **kwargs):
        self.user_slug = slugify(self.user.username)


        if (self.pk is False) : 
            new_user_profile = UserProfile.objects.create(user=self.user , user_slug=self.user_slug)
            new_user_profile.posts_clicked.add(self.posts_clicked)


        return super(UserProfile, self).save(*args, **kwargs)



        
    
        

    def __str__(self) :
        return self.user.username