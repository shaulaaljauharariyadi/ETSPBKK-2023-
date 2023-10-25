from django.contrib import admin
from django.urls import path
from rekam_medis_app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('semua-rekam-medis/', views.semua_rekam_medis, name='semua_rekam_medis'),
    path('riwayat-rekam-medis/<int:pasien_id>/', views.riwayat_rekam_medis_pasien, name='riwayat_rekam_medis_pasien'),
    path('rekam-medis-dokter/<int:dokter_id>/', views.rekam_medis_per_dokter, name='rekam_medis_per_dokter'),
    path('tambah-rekam-medis/', views.tambah_rekam_medis, name='tambah_rekam_medis'),
]

