from django.db import models

# Create your models here.
class Pengeditan(models.Model):
    pemotongan = models.CharField(max_length=255)
    penyesuaian_warna = models.CharField(max_length=255)
    filter = models.CharField(max_length=255)

    def __str__(self):
        return self.pemotongan

class Portofolio(models.Model):
    unggah = models.CharField(max_length=200)
    menambahkan_deskripsi = models.CharField(max_length=200)
    mengatur_kategori = models.CharField(max_length=255)

    def __str__(self):
        return self.unggah
    
class Kolaborasi(models.Model):
    ruang_kerja_bersama = models.CharField(max_length=200)
    undang_anggota_tim = models.CharField(max_length=200)
    komentar = models.CharField(max_length=200)

    def __str__(self):
        return self.ruang_kerja_bersama