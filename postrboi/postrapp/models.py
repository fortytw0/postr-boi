from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
import urllib.request as urllib2

# Create your models here.

class Tag(models.Model) : 

    tag_creator = models.ForeignKey(User , on_delete=models.CASCADE)
    tag_name = models.CharField(unique=True, blank=True, max_length=8 , default="")
    tag_slug = models.SlugField(unique=True , max_length=50)
    tag_description = models.CharField(blank=True , max_length=128, default="")

    seen_count = models.IntegerField(default=0)
    clicked_count = models.IntegerField(default=0)
    reco_count = models.IntegerField(default=0)

    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tag_name

    def save(self, *args, **kwargs):

        self.tag_name = self.tag_name.upper()

        if (self.tag_name == "") or (self.tag_name == "NO-TAG") : 
            self.tag_slug = "no-tag"
        else : 
            self.tag_slug = slugify(self.tag_name)

        if (self.pk is False) : 
            Tag.objects.create(tag_name=self.tag_name , tag_slug=self.tag_slug , tag_creator=self.tag_creator)

        return super(Tag , self).save(*args, **kwargs)

class Post(models.Model) : 

    poster = models.ForeignKey(User , on_delete=models.CASCADE)
    content = models.TextField(blank=False, null=False, max_length=150 , unique=True)
    article_hyperlink = models.URLField(unique=True)

    tag_1 = models.ForeignKey(Tag , on_delete=models.CASCADE , related_name="high_prio_tag" , blank=True , null=True)
    tag_2 = models.ForeignKey(Tag , on_delete=models.CASCADE , related_name="moderate_prio_tag", blank=True , null=True)
    tag_3 = models.ForeignKey(Tag , on_delete=models.CASCADE , related_name="low_prio_tag", blank=True , null=True)
    tag_4 = models.ForeignKey(Tag , on_delete=models.CASCADE , related_name="least_prio_tag", blank=True , null=True)
    
    seen_count = models.IntegerField(default=0)
    click_count = models.IntegerField(default=0)
    reco_count = models.IntegerField(default=0)

    created_date = models.DateTimeField(auto_now_add=True)

    def save(self, if_new_profile=False, *args , **kwargs):

        request = urllib2.urlopen(self.article_hyperlink)
        self.article_hyperlink = request.geturl() #checking for redirects

        return super(Post, self).save(*args, **kwargs)


    def __str__(self):
        return self.content
