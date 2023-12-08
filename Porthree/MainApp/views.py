from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, LoginForm
from .forms import UserDetailsForm
from .models import UserDetails, Project


# Create your views here.
def index(request):
    """index view function

    Args:
        request (_object_): django http request

    Returns:
        _object_: interaction with template
    """
    context = {}
    return render(request, "MainApp/index.html", context)


@login_required
def user_details_form(request, username):
    user = request.user

    try:
        # Check if data already exists for the current user
        user_details = UserDetails.objects.get(user=user)
    except UserDetails.DoesNotExist:
        user_details = None

    if request.method == "POST":
        form = UserDetailsForm(request.POST, request.FILES, instance=user_details)
        if form.is_valid():
            user_details = form.save(commit=False)
            user_details.user = request.user
            user_details.save()
            return redirect("portfolio", username=request.user.username)
    else:
        form = UserDetailsForm(instance=user_details)

    return render(request, "MainApp/dashboard1.html", {"form": form})


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(
                "portfolio", username=request.user.username
            )  # redirect to user portfolio view
    else:
        form = SignUpForm()
    return render(request, "MainApp/sign-up.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(
                "portfolio", username=request.user.username
            )  # redirect to user portfolio view
    else:
        form = LoginForm()
    return render(request, "MainApp/login.html", {"form": form})


def user_logout(request):
    """logs out a logged in user

    Args:
        request (_object_): django http request

    Returns:
        _object_: page redirection
    """
    logout(request)
    return redirect("login")  # Change 'home' to desired redirect URL


def portfolio(request, username):
    """
    redirection method on login or signup containing portfolio
    """
    try:
        user_details = get_object_or_404(UserDetails, user__username=username)
    except UserDetails.DoesNotExist:
        user_details = None
    try:
        projects = Project.objects.select_related("user").filter(
            user__username=username
        )
    except Project.DoesNotExist:
        projects = None
    context = {
        "user": request.user,
        "user_details": user_details,
        "projects": projects,
    }
    return render(request, "MainApp/portfolio.html", context)


@login_required
def portfolio_nav(request):
    """
    redirection method on login or signup containing portfolio
    """
    context = {
        "user": request.user,
    }
    return render(request, "portfolio_nav.html", context)


def main_nav(request):
    """
    redirection method on login or signup containing portfolio
    """
    context = {
        "user": request.user,
    }
    return render(request, "base.html", context)


def projects(request):
    """projects view function

    Args:
        request (_object_): django http request

    Returns:
        _object_: interaction with template
    """
    return render(request, "MainApp/projects.html")


def case_study(request):
    """case_study view function

    Args:
        request (_object_): django http request

    Returns:
        _object_: interaction with template
    """
    return render(request, "MainApp/case-study.html")


def blog_home(request):
    """blog view function

    Args:
        request (_object_): django http request

    Returns:
        _object_: interaction with template
    """
    return render(request, "MainApp/blog-home.html")


def blog_post(request):
    """blog post view function

    Args:
        request (_object_): django http request

    Returns:
        _object_: interaction with template
    """
    return render(request, "MainApp/blog-post.html")


def resume(request):
    """resume view function

    Args:
        request (_object_): django http request

    Returns:
        _object_: interaction with template
    """
    return render(request, "MainApp/resume.html")


def contact(request):
    """contact view function

    Args:
        request (_object_): django http request

    Returns:
        _object_: interaction with template
    """
    return render(request, "MainApp/contact.html")
