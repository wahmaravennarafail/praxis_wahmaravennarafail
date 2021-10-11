from django.shortcuts import render
from task import models

    # Create your views here.
def readMakanan(request):
    if request.POST:
        input_jenis = request.POST["jenis"]
        input_nama = request.POST['nama']
        input_harga = request.POST['harga']
        models.makanan.objects.create(jenis = input_jenis, nama = input_nama, harga = input_harga)
    data = models.makanan.objects.all()
    return render(request, "makanan/index.html",{
            "data": data,
        })

def readMinuman(request):
    if request.POST:
        input_jenis = request.POST["jenis"]
        input_nama = request.POST["nama"]
        input_harga = request.POST["harga"]
        models.minuman.objects.create(jenis = input_jenis, nama = input_nama, harga = input_harga)
    data = models.minuman.objects.all()
    return render(request, "minuman/index.html".{
        "data": data
    })

def readPesanan(request):
    if request.POST:
        get_makanan = request.POST["makanan"]
        get_minuman = request.POST["minuman"]
        get_jumlah_makanan = request.POST["jumlah_makanan"]
        get_jumlah_minuman = request.POST["jumlah_minuman"]

        input makanan = models.makanan.objects.filter(id=get_makanan).first()
        input minuman = models.minuman.objects.filter(id=get_minuman).first()
        models.pesanan.objects.create(makanan = input_makanan, minuman = input_minuman, jumlah_makanan = get_jumlah_makanan, jumlah_minuman = get_jumlah_minuman)
    dataMakanan = models.makanan.objects.all()
    dataMinuman = models.minuman.objects.all()
    data = models.pesanan.objects.all()
    return render(request, "pesanan/index.html"
        "dataMakanan": dataMakanan,
        "dataMinuman": dataMinuman,
        "data": data,
    })
def hapus(request, id):
    models.Makanan.objects.filter(id=id).delete()
    return redirect('/')

def detail(request, id):
    data = models.Makanan.objects.filter(id = id).first()
    print(data)
    return render(request, "detail.html", {
        "detailData": data,
    })

def edit(request, id):
    if request.POST:
        input = request.POST["nama"]
        print(input)
        models.Makanan.objects.filter(id=id).update(pesanan=input)
        return redirect('/')



        #input data ke database
        # models.Makanan.objects.create(nama = request.POST['fname'])
        #nampilin data
    data2 = models.Makanan.objects.filter(id = id).first()
    return render(request, 'edit.html', {
        "detailData" : data2
    })
    
def about(request):
    return  ("Halaman about")