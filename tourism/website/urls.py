from django.urls import include,path
from website import views
app_name="website"
urlpatterns = [
    path('',views.index,name="index"),
    path('home/',views.index,name="home"),
    path('login/',views.loginform,name='login'),
    path('register/',views.regform,name='register'),
    path('my/',views.account,name='account'),
    path('myEdit/',views.accountedit,name='accountedit'),
    path('logout/',views.logout,name='logout'),
]
