from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, LoginForm
from .forms import UserDetailsForm, ProjectForm, SkillForm
from .models import UserDetails, Project, Skill


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
def user_details_form(request):
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
            user.email = user_details.email
            user.save() # update user instance email
            return redirect('user-details')
    else:
        email = user.email if user.email != "" else user_details.email
        form = UserDetailsForm(instance=user_details, initial={'email': email})
    context = {
        "form": form,
        "user_details": user_details,
    }

    return render(request, "MainApp/user-details.html", context)



@login_required
def create_skill(request):
    user = request.user

    try:
        # Check if data already exists for the current user
        user_skills = Skill.objects.get(user=user)
    except Skill.DoesNotExist:
        user_skills = None

    if request.method == "POST":
        form = SkillForm(request.POST, instance=user_skills)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.user = request.user  # associate user
            skill.save()
            return redirect("create-skills")  # Redirect to a success page
    else:
        form = SkillForm(instance=user_skills)

    context = {
        "form": form,
        "user_skills": user_skills,
    }

    return render(request, "MainApp/create-skills.html", context)


@login_required
def create_project(request, project_id=None):
    user = request.user

    # Handling project deletion
    if request.method == "POST" and "delete_project" in request.POST:
        project_id_to_delete = request.POST.get("delete_project")
        project_to_delete = get_object_or_404(
            Project, id=project_id_to_delete, user=user
        )
        project_to_delete.delete()
        return redirect("create-project")  # Redirect to current page with deletion

    if project_id:
        # Editing an existing project
        project = get_object_or_404(Project, id=project_id, user=user)

        if request.method == "POST":
            form = ProjectForm(request.POST, instance=project)
            if form.is_valid():
                project = form.save(commit=False)
                project.user = request.user
                project.save()
                return redirect(
                    "create-project"
                )  # Redirect to page containing list and form
        else:
            form = ProjectForm(instance=project)

    else:
        # Creating a new project
        project = Project(user=user)

        if request.method == "POST":
            form = ProjectForm(request.POST, instance=project)
            if form.is_valid():
                project = form.save(commit=False)
                project.user = request.user
                project.save()
                return redirect("create-project")  # Redirect to project
        else:
            form = ProjectForm()

    projects = Project.objects.filter(user=user)  # Retrieve all projects for display

    context = {"form": form, "projects": projects}
    return render(request, "MainApp/create-project.html", context)


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
                "login",
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
            return redirect("user-details")  # redirect to user portfolio view
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
    # this class throws error if the user's userdetails query is empty
    """
    redirection method on login or signup containing portfolio
    """
    try:
        user = get_object_or_404(User, username=username)
    except User.DoesNotExist:
        user = None
    try:
        user_details = get_object_or_404(UserDetails, user=user)
    except UserDetails.DoesNotExist:
        user_details = None
    try:
        projects = Project.objects.filter(user=user)
    except Project.DoesNotExist:
        projects = None
    try:
        value = Skill.objects.filter(user=user)
        if value:
            skills =  value[0].name.split(", ")
        else:
            skills = None
    except Skill.DoesNotExist:
        skills = None
    context = {
        "user": request.user,
        "user_details": user_details,
        "projects": projects,
        "skills": skills,
    }
    return render(request, "MainApp/portfolio.html", context)


@login_required
def portfolio_nav(request):
    """
    redirection method on login or signup containing portfolio
    """
    user = request.user
    user_details = get_object_or_404(UserDetails, user=user)
    context = {
        "user": user,
        "user_details": user_details,
    }
    return render(request, "portfolio_nav.html", context)


def main_nav(request):
    """
    redirection method on login or signup containing portfolio
    """
    user = request.user
    context = {
        "user": user,
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
