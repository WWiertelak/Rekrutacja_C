from django import forms


class PeselForm(forms.Form):
    pesel = forms.CharField(label="Wprowadź numer PESEL", max_length=11, min_length=11)
