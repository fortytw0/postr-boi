from django.urls import path
from login import views


app_name = 'login'

urlpatterns = [
    path("" , views.signin , name="login"),
    path("signup" , views.register , name="register")
]