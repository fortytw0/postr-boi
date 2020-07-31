from django.urls import path 
from stats.views import SiteView, UserView

app_name = "stats"

urlpatterns = [
    path("site" , SiteView.as_view() , name="site_stats_view") , 
    path("<str:username>" , UserView.as_view() , name="user_stats_view")
]
