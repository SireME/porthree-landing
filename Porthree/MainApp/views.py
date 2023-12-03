from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, LoginForm


# Create your views here.
def index(request):
    """index page view

    Args:
        request (_object_): django Http request

    Returns:
        _object_: current class view object
    """
    return render(request, "MainApp/index.html", {})


def signup(request):
    """sign-up page view

    Args:
        request (_object_): django Http request

    Returns:
        _object_: current class view object
    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('portfolio', username=request.user.username)  # redirect to user portfolio view
    else:
        form = SignUpForm()
    return render(request, "MainApp/sign-up.html", {'form': form})

def user_login(request):
    """login page view

    Args:
        request (_object_): django Http request

    Returns:
        _object_: current class view object
    """
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('portfolio', username=request.user.username)  # redirect to user portfolio view
    else:
        form = LoginForm()
    return render(request, 'MainApp/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')  # Change 'home' to desired redirect URL

def portfolio(request, username):
    """
    redirection method on login or signup containing portfolio
    """
    uid = str(request.user.id)
    return render(request, 'MainApp/portfolio.html', {"user": uid})
