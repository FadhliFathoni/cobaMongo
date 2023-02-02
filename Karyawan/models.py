#Inisialisasi Tabel
from django.db import models
from mongoengine import Document, fields

class Karyawan(models.Model):
    nama = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    email = models.EmailField()
    alamat = models.TextField()
    
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)