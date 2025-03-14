from django.contrib import admin
from website.models import Users
from website.models import Packages
from website.models import Bookings
from website.models import Destinations,Payment_Info
from django.contrib.sessions.models import Session
# Register your models here.
admin.site.register(Users)
admin.site.register(Packages)
admin.site.register(Bookings)
admin.site.register(Destinations)
admin.site.register(Session)
admin.site.register(Payment_Info)