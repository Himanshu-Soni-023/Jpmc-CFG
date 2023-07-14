from django.shortcuts import render,redirect
from django.http import HttpResponse
# importing forms
from .forms import *


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegistrationForm()
    context = {'form':form}
    return render(request, 'cfg_app/register.html', context)

def home(request):
    return HttpResponse('<h1>Home Page</h1>')
