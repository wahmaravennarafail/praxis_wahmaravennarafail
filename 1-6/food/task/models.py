from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields import IntegerField

# Create your models here.
from django.db import models

class makanan(models.Model):
    jenis = models.CharField(max_length=200)
    nama = CharField(max_length=200)
    harga = models.IntegerField()

class minuman(models.Model):
    jenis = models.CharField(max_length=200)
    nama = CharField(max_length=200)
    harga = models.IntegerField()

class pesanan(models.Model):
    jenis = models.ForeignKey(makanan, on_delete=models.CASCADE)
    Jumlah_makanan = models.IntegerField()
    minuman = models.ForeignKey(minuman, on_delete=models.CASCADE)
    jumlah_minuman = models.IntegerField()