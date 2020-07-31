from django.urls import path
from userprofile import views

app_name = "userprofile"

urlpatterns = [
    
    path("<str:username>" , views.profile_view , name="profile_view")
]