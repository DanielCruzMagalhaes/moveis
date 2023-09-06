from django.shortcuts import render
from .models import *
# Create your views here.



def index(request):
    banner = Banner.objects.get(id=1)
    main = Main.objects.all()
    main2 = Main2.objects.all()
    return render(request,'index.html',{"banner":banner,"main":main,"main2":main2,})