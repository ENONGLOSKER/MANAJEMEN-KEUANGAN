from django.db import models

# Create your models here.
class Transaksi(models.Model):
    keterangan = models.CharField(max_length=255)
    jumlah = models.DecimalField(max_digits=10, decimal_places=2)
    tanggal = models.DateField(auto_now_add=True)
    tipe = models.CharField(max_length=10, choices=[('masuk', 'Masuk'), ('keluar', 'Keluar')])

    def __str__(self):
        return self.tipe
    