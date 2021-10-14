from django.contrib import admin
from django.urls import path
from task import views

urlpatterns = [
    path('', views.home),
    path('pesanan/', views.index),
    path('makan/', views.makanan),
    path('minum/', views.minuman),
    path('<id>/deletemakanan/', views.deletemakanan),
    path('<id>/deleteminuman/', views.deleteminuman),
    path('<id>/detailmakanan/', views.detailmakanan),
    path('<id>/detailminuman/', views.detailminuman),
    path('<id>/updatemakanan/', views.editmakanan),
    path('<id>/updateminuman/', views.editminuman),
    path('<id>/deletepesanan/', views.deletepesanan),
]
