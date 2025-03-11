from django.contrib import admin
from django.urls import path,include
from django.conf.urls import handler404, handler500, handler403

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('website.urls'))
]
