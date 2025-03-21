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
    path('update_content/',views.update_section,name='update_content'),
    path('booking/',views.booking,name='booking'),
    path('delete_account',views.delete_account,name="delete_account"),
    path('insta/',views.insta,name="instagram"),
    path('booking/makepayment/',views.make_payment,name="payment"),
]
