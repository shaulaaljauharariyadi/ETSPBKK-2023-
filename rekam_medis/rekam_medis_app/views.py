from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib import messages  # Import modul flash messages
from .models import Pasien, Dokter, RekamMedis
from django.contrib.auth.decorators import login_required

@login_required
def semua_rekam_medis(request):
    rekam_medis = RekamMedis.objects.all()
    return render(request, 'semua_rekam_medis.html', {'rekam_medis': rekam_medis})

def riwayat_rekam_medis_pasien(request, pasien_id):
    pasien = Pasien.objects.get(id=pasien_id)
    rekam_medis = RekamMedis.objects.filter(pasien=pasien)
    return render(request, 'riwayat_rekam_medis_pasien.html', {'pasien': pasien, 'rekam_medis': rekam_medis})

def rekam_medis_per_dokter(request, dokter_id):
    dokter = Dokter.objects.get(id=dokter_id)
    rekam_medis = RekamMedis.objects.filter(dokter=dokter)
    return render(request, 'rekam_medis_per_dokter.html', {'dokter': dokter, 'rekam_medis': rekam_medis})

def tambah_rekam_medis(request):
    if request.method == 'POST':
        # Proses data formulir
        # Cek jika data telah diisi sesuai ketentuan
        # Misalnya, Anda dapat menggunakan form.is_valid() atau kondisi lainnya

        # Jika data valid, tambahkan flash message berhasil
        messages.success(request, 'Formulir rekam medis berhasil diisi!')
        
        # Redirect ke halaman yang sesuai
        return redirect('semua_rekam_medis')

    return render(request, 'tambah_rekam_medis.html')

