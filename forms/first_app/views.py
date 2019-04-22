from django.shortcuts import render
from first_app import forms


# Create your views here.
def index(request):
    return render(request, 'first_app/index.html')


def forms_view(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            print("Validated Successfully!")
            print("Name:", form.cleaned_data['name'])
            print("Email:", form.cleaned_data['email'])
            print("Text:", form.cleaned_data['text'])

    return render(request, 'first_app/form_page.html', {'form': form})
