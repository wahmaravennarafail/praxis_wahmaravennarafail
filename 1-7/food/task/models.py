from django.db import models
from django.db.models.fields import CharField, IntegerField

# Create your models here.

class makanan(models.Model) :
    jenis = models.CharField(max_length=100)
    nama = CharField(max_length=100)
    harga = models.IntegerField()

class minuman(models.Model) :
    jenis = models.CharField(max_length=100)
    nama = CharField(max_length=100)
    harga = models.IntegerField()

class pesanan(models.Model) :
    makanan = models.ForeignKey(makanan,on_delete=models.CASCADE)
    minuman = models.ForeignKey(minuman,on_delete=models.CASCADE)
    jml_makanan = models.IntegerField()
    jml_minuman = models.IntegerField()
