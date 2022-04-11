from multiprocessing import context
from django.shortcuts import render
from .forms import RegisterUserForm


# Create your views here.
def index(request):
    return render(request, 'index.html')

def signupUser(request):
    form = RegisterUserForm()
    context = {'form': form}
    return render(request, 'signup.html', context)

def loginUser(request):
    return render(request, 'login.html')