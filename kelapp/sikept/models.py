from django.db import models
from datetime import datetime

# Create your models here.


class Yayasan(models.Model):
    nama_yayasan = models.CharField(max_length=200, null=True)
    phone_yayasan = models.CharField(max_length=200, null=True)
    email_yayasan = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nama_yayasan


class Pts(models.Model):
    Provinsi = (
        ('NTB', 'Nusa Tenggara Barat'),
        ('Bali', 'Bali')
    )

    Status_pts = (
        ('Aktif', 'Aktif'),
        ('Alih Bentuk', 'Alih Bentuk'),
        ('Tutup', 'Tutup'),
        ('Pembinaan', 'Pembinaan')
    )

    Jenis_pts = (
        ('Akademi Komunitas', 'Akademi Komunitas'),
        ('Akademi', 'Akademi'),
        ('Politeknik', 'Politeknik'),
        ('Sekolah Tinggi', 'Sekolah Tinggi'),
        ('Institut', 'Institut'),
        ('Universitas', 'Universitas')
    )

    nama_yayasan = models.ForeignKey(
        Yayasan, null=True, on_delete=models.SET_NULL)
    nama_pts = models.CharField(max_length=200, null=True)
    jenis_pts = models.CharField(max_length=200, null=True, choices=Jenis_pts)
    status_pts = models.CharField(
        max_length=200, null=True, choices=Status_pts)
    provinsi = models.CharField(max_length=200, null=True, choices=Provinsi)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nama_pts


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Dokumen(models.Model):
    CATEGORY = (
        ('SK Pendirian', 'SK Pendirian'),
        ('SK Perubahan', 'SK Perubahan'),
        ('SK Penutupan', 'SK Penutupan'),
        ('SK Pembukaan', 'SK Pembukaan'),
        ('SK Penyesuaian Nomenklatur', 'SK Penyesuaian Nomenklatur'),
        ('Akta Pendirian', 'Akta Pendirian'),
        ('Akta Perubahan', 'Akta Perubahan'),
        ('SK Menkumham', 'SK Menkumham'),
        ('SK Menkumham Pencatatan', 'SK Menkumham Pencatatan'),
        ('Rekomendasi', 'Rekomendasi'),
        ('Rekomendasi Akreditasi', 'Rekomendasi Akreditasi'),
        ('Surat Permohonan', 'Surat Permohonan'),
        ('Berita Acara', 'Berita Acara')
    )
    nomor = models.CharField(max_length=200, null=True)
    perihal = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    tanggal_surat = models.DateField(
        "Tanggal Surat", null=True)
    nama_pejabat = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    dokumen_file = models.FileField(
        "Unggah File", null=True, blank=True, upload_to="file/")
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.nomor


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Ditolak', 'Ditolak'),
        ('Dikirim', 'Dikirim'),
        ('Disimpan', 'Disimpan'),
    )

    Jenis = (
        ('Akta', 'Akta'),
        ('SK Menkumham', 'SK Menkumham'),
        ('SK', 'SK'),
        ('Rekomendasi', 'Rekomendasi'),
        ('Surat', 'Surat'),
        ('Berita Acara', 'Berita Acara')
    )

    nama_pts = models.ForeignKey(Pts, null=True, on_delete=models.SET_NULL)
    nomor = models.ForeignKey(Dokumen, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    Jenis = models.CharField(max_length=200, null=True, choices=Jenis)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return str(self.nomor)
