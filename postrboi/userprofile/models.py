from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileModel(models.Model) : 

    baseUser = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=128, blank=True, default="Hey, welcome to my profile!")

    def __str__(self) : 
        return self.baseUser