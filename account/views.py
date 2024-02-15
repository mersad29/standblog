from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm


def sign_in(request):

    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                return redirect("/")
        else:
            messages.error(request, "Username or password is not correct")
    return render(request, 'account/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect("/")

# def register_view(request):
#     if request == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             user.username = user.username.lower()
#             user.save()
#             login(request, user)
#             return HttpResponseRedirect('/')
#         else:
#             return render(request, "account/register.html",{'form': form})
