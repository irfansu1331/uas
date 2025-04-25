from django import forms
from .models import Alumni

class AlumniForm(forms.ModelForm):
    class Meta:
        model = Alumni
        fields = ['nama', 'email', 'graduation_year', 'major', 'job_position', 'company']
        labels = {
            'nama': 'Nama Lengkap',
            'email': 'Email',
            'graduation_year': 'Tahun Lulus',
            'major': 'Jurusan',
            'job_position': 'Posisi Pekerjaan',
            'company': 'Perusahaan',
        }
