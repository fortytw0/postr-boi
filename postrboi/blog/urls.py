from django.urls import path
from blog import views
from django.contrib.auth.decorators import login_required

app_name = 'blog'

urlpatterns = [
    path("" , views.index , name="index_view"),
    path("logout/" , views.logout_view , name="logout_view"),
    path("post/" , views.create_view , name="create_view")
]