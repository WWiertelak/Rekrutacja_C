from django.shortcuts import render
from .forms import UploadFileForm
import random


def mix_word(word):
    '''Mixes letters in a word, except for the first and last one.'''
    if len(word) > 3:
        middle = list(word[1:-1])
        random.shuffle(middle)
        return word[0] + ''.join(middle) + word[-1]
    return word


def process_text(text):
    '''Mixes letters in all words in a text'''
    if not text:
        return ''

    words = text.split()
    return ' '.join([mix_word(word) for word in words])


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file_content = request.FILES['file'].read().decode('utf-8')
            shuffled_content = process_text(file_content)
            return render(request, 'text/result.html', {'result': shuffled_content})
    else:
        form = UploadFileForm()
    return render(request, 'text/upload.html', {'form': form})
