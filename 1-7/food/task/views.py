from django.shortcuts import redirect,render
from . import models

# Create your views here.

def makanan(request):
    if request.POST:
        jenis = request.POST["jenis"]
        nama = request.POST["nama"] 
        harga = request.POST["harga"]
        models.makanan.objects.create(jenis=jenis, nama=nama, harga=harga)
        return redirect('/')
    makan = models.makanan.objects.all()
    return render (request, "indexmakanan.html", {
        'makan' : makan
        })


def minuman(request):
    if request.POST:
        jenis = request.POST['jenis']
        nama = request.POST['nama']
        harga = request.POST['harga']
        models.minuman.objects.create(jenis=jenis, nama=nama, harga=harga)
        return redirect('/')
    minum = models.minuman.objects.all()
    return render (request, "indexminuman.html", {
        'minum' :minum
        })



def index(request):
    if request.POST: 
        get_makanan= request.POST["makanan"]
        get_minuman= request.POST["minuman"]
        get_jml_makanan= request.POST["jml_makanan"]
        get_jml_minuman = request.POST["jml_minuman"]

        input_makanan=models.makanan.objects.filter(id=get_makanan).first()
        input_minuman=models.minuman.objects.filter(id=get_minuman).first()

        models.pesanan.objects.create(makanan=input_makanan, minuman=input_minuman, jml_makanan=get_jml_makanan, jml_minuman=get_jml_minuman)
    makan=models.makanan.objects.all()
    minum=models.minuman.objects.all()
    pesanan=models.pesanan.objects.all()
    return render (request,"indexpesanan.html", {
        'makan':makan,
        'minum':minum,
        'pesanan' : pesanan,
    })

def detailmakanan(request, id):
    models.makanan.objects.filter(id=id).first()
    return redirect('/')

def detailminuman(request, id):
    models.minuman.objects.filter(id=id).first()
    return redirect('/')

def editmakanan(request, id):
    if request.POST:
        input=request.POST["nama"]
        print (input)
    models.makanan.objects.filter(id=id).update(nama=input)
    return redirect('/')

def editminuman(request, id):
    if request.POST:
        input=request.POST["nama"]
        print (input)
    models.minuman.objects.filter(id=id).update(nama=input)
    return redirect('/')

def deletemakanan(request, id):
    models.makanan.objects.filter(id=id).delete()
    return redirect('/makan')

def deleteminuman(request, id):
    models.minuman.objects.filter(id=id).delete()
    return redirect('/minum')

