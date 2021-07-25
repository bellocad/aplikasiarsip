import django_filters
from django_filters import CharFilter
from django_filters.conf import DEFAULTS

from .models import *


class DokumenFilter(django_filters.FilterSet):
    perihal = CharFilter(field_name='perihal',
                         lookup_expr='icontains', label='Perihal ')
    nomor = CharFilter(field_name='nomor',
                       lookup_expr='icontains', label='Nomor ')
    category = CharFilter(field_name='category',
                          lookup_expr='icontains', label='Jenis ')

    class Meta:
        model = Dokumen
        fields = {
            'category'
        }
        #exclude = ['tags','nama_pejabat']


class OrderFilter(django_filters.FilterSet):
    nomor = CharFilter(field_name="nomor__nomor",
                       lookup_expr='icontains', label='Nomor ')
    nama_pts = CharFilter(field_name="nama_pts__nama_pts",
                          lookup_expr='icontains', label='Nama Perguruan Tinggi ')
    Perihal = CharFilter(field_name="nomor__perihal",
                         lookup_expr='icontains', label='Perihal ')

    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['Jenis', 'status', 'date_created', ]
