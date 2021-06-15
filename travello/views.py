from django.shortcuts import render
from .models import destination



def home(request):
    
    dests=destination.objects.all()

    return render(request,'index.html',{'dests':dests})