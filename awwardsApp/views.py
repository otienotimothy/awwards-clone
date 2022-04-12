from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterUserForm, LoginUserForm, EditProfileForm
from .models import Profile


# Create your views here.
def index(request):
    return render(request, 'index.html')

def signupUser(request):

    if request.user.is_authenticated:
        return redirect(index)

    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        user = form.save(commit=False)
        if form.is_valid():
            if User.objects.filter(username=user.username.lower()).exists():
                messages.error(request, f'A User with the username, {user.username}, Already exists')
            elif User.objects.filter(email=user.email.lower()).exists():
                messages.error(request, f'A user with the email, {user.email}, Already exists')
            else:
                user.email = user.email.lower()
                user.username = user.username.lower()
                user.save()
                userProfile = Profile(user=user)
                userProfile.save()
                login(request, user)
                return redirect(index)

    form = RegisterUserForm()
    context = {'form': form}
    return render(request, 'signup.html', context)

def loginUser(request):

    if request.user.is_authenticated:
        return redirect(index)

    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username'].lower()
            password = form.cleaned_data['password']
            try:
                user_exist = User.objects.get(username=username)
                if user_exist:
                    user = authenticate(
                        request, username=username, password=password)
                    if user:
                        login(request, user)
                        return redirect(index)
                    else:
                        messages.error(request, 'Invalid username or password')
            except:
                messages.error(request, 'User does not exist, sign-up')

    form = LoginUserForm()
    context = {'form': form}
    return render(request, 'login.html', context)


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect(loginUser)


@login_required(login_url='login')
def loadProfile(request, username):

    if request.user.username != username:
        logout(request)
        return redirect(loginUser)

    try:
        userProfile = User.objects.get(username = username)
        projects = userProfile.projects.all()
    except:
        messages.error(request, f'An Error occurred while trying to load your profile ')

    form = EditProfileForm()

    context = {'userProfile': userProfile, 'projects': projects, 'form':form}
    return render(request, 'profile.html', context)
