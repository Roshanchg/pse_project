from django.urls import include,path
from website import views
appname="website"
urlpatterns = [
    path('',views.index,name="index"),
]
