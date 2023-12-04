from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, LoginForm
from .forms import UserDetailsForm

# Create your views here.
def index(request):
    return render(request, "MainApp/index.html", {})

@login_required
def user_details_form(request):
    if request.method == 'POST':
        form = UserDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            user_details = form.save(commit=False)
            user_details.user = request.user  # Assuming you have user authentication implemented
            user_details.save()
            return redirect('portfolio', username=request.user.username)  # Redirect to portfolio screen
    else:
        form = UserDetailsForm()

    return render(request, 'MainApp/user_details_form.html', {'form': form})


def signup(request):
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
    user = request.user
    return render(request, 'MainApp/portfolio.html', {"user": user})
