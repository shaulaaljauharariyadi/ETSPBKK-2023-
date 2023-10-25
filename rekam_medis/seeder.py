import os
import django
from faker import Faker

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rekam_medis.settings")  # Ganti "nama_proyek" dengan nama proyek Django Anda.
django.setup()

from rekam_medis_app.models import Pasien, Dokter, RekamMedis

fake = Faker()

# Fungsi untuk menambahkan data Pasien secara acak
def add_random_pasien():
    nama = fake.first_name() + ' ' + fake.last_name()
    pasien = Pasien.objects.create(nama=nama)
    print(f"Data Pasien ditambahkan: {nama}")

# Fungsi untuk menambahkan data Dokter secara acak
def add_random_dokter():
    nama = fake.first_name() + ' ' + fake.last_name()
    dokter = Dokter.objects.create(nama=nama)
    print(f"Data Dokter ditambahkan: {nama}")

def add_random_rekam_medis():
    # Pilih pasien dan dokter secara acak
    pasien = Pasien.objects.order_by("?").first()
    dokter = Dokter.objects.order_by("?").first()
    
    kondisi_kesehatan = fake.text(max_nb_chars=200)  # Teks acak dengan maksimal 200 karakter
    suhu_tubuh = fake.pydecimal(left_digits=2, right_digits=1, positive=True)  # Decimal antara 36.0 hingga 45.5
    resep = fake.file_name(extension="pdf")  # Nama file PDF acak

    rekam_medis = RekamMedis.objects.create(
        pasien=pasien,
        dokter=dokter,
        kondisi_kesehatan=kondisi_kesehatan,
        suhu_tubuh=suhu_tubuh,
        resep=resep,
    )

    print(f"Data RekamMedis ditambahkan untuk Pasien: {pasien.nama}, Dokter: {dokter.nama}")



# Menambahkan data Pasien dan Dokter
for _ in range(10):  # Ubah jumlah data sesuai kebutuhan Anda
    add_random_pasien()

for _ in range(5):  # Ubah jumlah data sesuai kebutuhan Anda
    add_random_dokter()

# Menambahkan data RekamMedis
for _ in range(10):  # Ubah jumlah data sesuai kebutuhan Anda
    add_random_rekam_medis()