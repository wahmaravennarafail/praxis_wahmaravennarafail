from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), 
    path('makanan/', views.makanan),
    path('minuman/', views.minuman),
    path('pesanan/', views.pesanan),
    path ('hapus/<id>/', views.hapus),
    path('detail/<id>/', views.detail),
    path('edit/<id>/', views.edit),
]
