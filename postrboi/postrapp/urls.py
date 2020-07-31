from django.urls import path
from postrapp import views

app_name = "postrapp"

urlpatterns = [
    path("" , views.IndexView.as_view(), name="index_view") , 
    path("post" , views.CreateView.as_view() , name="create_view") , 
    path("tag/<str:tag_name>/" , views.TagView.as_view() , name="tag_view")
]