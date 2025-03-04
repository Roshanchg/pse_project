from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.
def index(request):
    return render(request=request,template_name="regform.html",context=None)