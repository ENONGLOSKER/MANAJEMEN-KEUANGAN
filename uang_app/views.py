from django.shortcuts import render,redirect, get_object_or_404
from .models import Transaksi
from django.db.models import Sum
from django.http import HttpResponse

# melihat data
def index(request):
    transaksi_list = Transaksi.objects.all()

    # semua data keuangan di urutkan berdasarkan yang terakhir diinput
    uang = transaksi_list.order_by('-id')
    # satu data terakhir diinput
    detail = transaksi_list.order_by('-id')[:1]
    # hitung uang masuk, keluar dan sisa
    uang_masuk = transaksi_list.filter(tipe='masuk').aggregate(total_masuk=Sum('jumlah'))['total_masuk'] or 0
    uang_keluar = transaksi_list.filter(tipe='keluar').aggregate(total_keluar=Sum('jumlah'))['total_keluar'] or 0
    sisa_uang = uang_masuk - uang_keluar

    context = {
        'transaksi_list': transaksi_list,
        'uang_masuk': uang_masuk,
        'uang_keluar': uang_keluar,
        'sisa_uang': sisa_uang,
        'uang': uang,
        'detail': detail,
    }
    
    print(detail)
    return render(request, 'index.html', context)

# membuat data
def tambah_transaksi(request):
    if request.method == 'POST':
        tipe = request.POST.get('tipe')
        jumlah = request.POST.get('jumlah')
        keterangan = request.POST.get('keterangan')
        tanggal = request.POST.get('tanggal')

        Transaksi.objects.create(tipe=tipe, jumlah=jumlah, keterangan=keterangan, tanggal=tanggal)

        return redirect('index')

    return render(request, 'keuangan/tambah_transaksi.html')

# menghapus data
def hapus_transaksi(request, id):
    transaksi = get_object_or_404(Transaksi, pk=id)
    transaksi.delete()

    return redirect('index')
