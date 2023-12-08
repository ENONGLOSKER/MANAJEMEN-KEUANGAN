from django.urls import path
from .import views

urlpatterns = [
    path('',views.index, name='index'),
    path('tambah/', views.tambah_transaksi, name='tambah_transaksi'),
    path('hapus/<int:id>/', views.hapus_transaksi, name='hapus_transaksi'),
]
