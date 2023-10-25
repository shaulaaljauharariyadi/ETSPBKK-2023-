from django.db import models

class Pasien(models.Model):
    nama = models.CharField(max_length=100)

class Dokter(models.Model):
    nama = models.CharField(max_length=100)

class RekamMedis(models.Model):
    pasien = models.ForeignKey(Pasien, on_delete=models.CASCADE)
    dokter = models.ForeignKey(Dokter, on_delete=models.CASCADE)
    kondisi_kesehatan = models.TextField()
    suhu_tubuh = models.DecimalField(max_digits=4, decimal_places=1, default=36.0)
    resep = models.FileField(upload_to='resep/')
