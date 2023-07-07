from django.shortcuts import render, redirect,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm


def sign_in(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "loged in!")
            return redirect("/")
        else:
            messages.error(request, "Username or password is not correct")

    return render(request, 'account/login.html', context={})

def logout_view(request):
    logout(request)
    return redirect("/")

def register_view(request):
    if request == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return render(request, "account/register.html",{'form': form})
