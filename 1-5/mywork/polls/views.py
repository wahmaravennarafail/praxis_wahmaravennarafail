from django.shortcuts import render, redirect
from . import models

# Create your views here.
def index(request):
    if request.POST:
        input = request.POST["nama"]
        models.project.objects.create(nama=input)

    data = models.project.objects.all()
    return render(request, 'index.html', {
        "datahtml": data
    })

def hapus(request, id):
    models.project.objects.filter(id=id).delete()
    return redirect('/')

def detail(request, id):
    data = models.project.objects.filter(id = id).first()
    print(data)
    return render(request, "detail.html", {
        "detailData": data,
    })

def edit(request, id):
    if request.POST:
        input = request.POST["nama"]
        print(input)
        models.project.objects.filter(id=id).update(nama=input)
        return redirect('/')



        #input data ke database
        # models.project.objects.create(nama = request.POST['fname'])
        #nampilin data
    data2 = models.project.objects.filter(id = id).first()
    return render(request, 'edit.html', {
        "detailData" : data2
    })
    
def about(request):
    return  ("Halaman about")