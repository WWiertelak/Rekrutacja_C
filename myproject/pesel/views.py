from django.shortcuts import render
from .forms import PeselForm
from pesel import utils as pesel_utils


def validate_pesel(request):
    '''Validates PESEL number.'''
    message = ''
    birth_date = None
    gender = None

    if request.method == 'POST':
        form = PeselForm(request.POST)
        if form.is_valid():
            pesel = form.cleaned_data['pesel']
            if pesel_utils.is_valid_pesel(pesel):
                birth_date = pesel_utils.extract_birth_date(pesel)
                gender = pesel_utils.extract_gender(pesel)
                message = "Numer PESEL jest prawidłowy"
            else:
                message = "Nieprawidłowy numer PESEL"
    else:
        form = PeselForm()

    context = {
        'form': form,
        'message': message,
        'birth_date': birth_date,
        'gender': gender
    }

    return render(request, 'pesel/index.html', context)
