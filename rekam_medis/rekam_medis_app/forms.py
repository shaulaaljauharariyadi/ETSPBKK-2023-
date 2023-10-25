from django import forms
from .models import RekamMedis

class RekamMedisForm(forms.ModelForm):
    class Meta:
        model = RekamMedis
        fields = ['pasien', 'dokter', 'kondisi_kesehatan', 'suhu_tubuh', 'resep']
