from django import forms
from django.core.validators import FileExtensionValidator


class UploadFileForm(forms.Form):
    file = forms.FileField(
        label='Wybierz plik tekstowy',
        validators=[FileExtensionValidator(allowed_extensions=['txt'])]
    )
