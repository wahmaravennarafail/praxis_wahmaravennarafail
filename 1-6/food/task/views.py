from django.shortcuts import redirect, render
from . import models

    # Create your views here.
def makanan(request):
    if request.POST:
        input_jenis = request.POST["jenis"]
        input_nama = request.POST["nama"]
        input_harga = request.POST["harga"]
        models.makanan.objects.create(jenis = input_jenis, nama = input_nama, harga = input_harga)
    data = models.makanan.objects.all()
    return render(request, "makanan/index.html",{
            "data": data,
        })

def minuman(request):
    if request.POST:
        input_jenis = request.POST["jenis"]
        input_nama = request.POST["nama"]
        input_harga = request.POST["harga"]
        models.minuman.objects.create(jenis = input_jenis, nama = input_nama, harga = input_harga)
    data = models.minuman.objects.all()
    return render(request, "minuman/index.html",{
        "data": data
    })

def pesanan(request):
    if request.POST:
        get_makanan = request.POST["makanan"]
        get_minuman = request.POST["minuman"]
        get_jumlah_makanan = request.POST["jumlah_makanan"]
        get_jumlah_minuman = request.POST["jumlah_minuman"]
        print(get_minuman)

        input_makanan = models.makanan.objects.filter(id=get_makanan).first()
        input_minuman = models.minuman.objects.filter(id=get_minuman).first()
        
        models.pesanan.objects.create(jenis=input_makanan, minuman=input_minuman, Jumlah_makanan=get_jumlah_makanan, jumlah_minuman = get_jumlah_minuman)
    dataMakanan = models.makanan.objects.all()
    dataMinuman = models.minuman.objects.all()
    data = models.pesanan.objects.all()
    return render(request, "pesanan/index.html",{
        "dataMakanan": dataMakanan,
        "dataMinuman": dataMinuman,
        "data":data,
    })
def hapus(request,id):
    models.makanan.objects.filter(pk=id).delete()
    return redirect('/')

def detail(request, id):
    data = models.makanan.objects.filter(id = id).first()
    print(data)
    return render(request, "detail.html", {
        "detailData": data,
    })

def edit(request, id):
    if request.POST:
        input = request.POST["nama"]
        print(input)
        models.makanan.objects.filter(id=id).update(nama=input)
        return redirect('/')



        #input data ke database
        # models.Makanan.objects.create(nama = request.POST['fname'])
        #nampilin data
    data2 = models.pesanan.objects.filter(id = id).first()
    return render(request, 'edit.html', {
        "detailData" : data2
    })
def index(request):
    return redirect("pesanan/")
def about(request):
    return  ("Halaman about")