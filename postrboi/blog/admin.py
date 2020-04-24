from django.contrib import admin
from blog import models

# Register your models here.
admin.site.register(models.Post)



@admin.register(models.UserProfile)
class UserProfileAdmin(admin.ModelAdmin) : 
    readonly_fields=["user_slug"]


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin) : 
    readonly_fields=["tag_slug"]