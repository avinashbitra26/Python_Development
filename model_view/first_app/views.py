from django.shortcuts import render
from django.http import HttpResponse
# from first_app.models import User
from first_app.forms import NewUser


# Create your views here.
def index(request):
    return render(request, 'first_app/index.html')


# def users(request):
#     user_list = User.objects.order_by('first_name')
#     my_dict = {'user_info': user_list}
#     return render(request, 'first_app/users.html', context=my_dict)
def users(request):
    form = NewUser()
    if request.method == 'POST':
        form = NewUser(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Form Invalid")
    return render(request, 'first_app/users.html', {'form': form})
