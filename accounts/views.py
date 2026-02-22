from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
def loginView(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('task-list')  # Change 'home' to your desired URL name
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "accounts/login.html")


def logoutView(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('login')