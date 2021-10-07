from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from . import models

def index(request):
    if request.POST:
        #input data ke database
        models.project.objects.create(nama = request.POST['fname'])
        #nampilin data
    data2 =models.project.objects.all()
    print(data2)

    return render(request,'index.html', {'isi': data2})

def about(request):
    return HttpResponse("Halaman about")