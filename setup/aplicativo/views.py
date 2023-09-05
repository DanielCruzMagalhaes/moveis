from django.shortcuts import render
from .models import *
# Create your views here.



def index(request):
    banner = Banner.objects.get(id=1)
    main = Main.objects.all()
    return render(request,'index.html',{"banner":banner,"main":main})