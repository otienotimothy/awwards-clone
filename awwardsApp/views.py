from multiprocessing import context
from django.shortcuts import render
from .forms import RegisterUserForm, LoginUserForm


# Create your views here.
def index(request):
    return render(request, 'index.html')

def signupUser(request):
    form = RegisterUserForm()
    context = {'form': form}
    return render(request, 'signup.html', context)

def loginUser(request):
    form = LoginUserForm()
    context = {'form': form}
    return render(request, 'login.html', context)