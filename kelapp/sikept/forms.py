from . models import Order, Dokumen
from django.forms import ModelForm, widgets, DateInput
from django import forms


class DateInputForm(DateInput):
    input_type = 'date'


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['nomor'].queryset = self.fields['nomor'].queryset.order_by(
            '-date_created')


class DokumenForm(ModelForm):
    class Meta:
        model = Dokumen
        fields = '__all__'
        widgets = {'tanggal_surat': DateInputForm(),
                   'nomor': forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Text goes here', 'cols': '10'})
                   }

    def clean_nomor(self):  # validate the nomor fields
        nomor = self.cleaned_data.get('nomor')
        if (nomor == ""):
            raise forms.ValidationError('Tidak Boleh Kosong')

        for instance in Dokumen.objects.all():
            if instance.nomor == nomor:
                raise forms.ValidationError(
                    ' _______________ Dokumen dengan nomor ' + nomor + ' sudah ada')
        return nomor
