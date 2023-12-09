from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, LoginForm
from django.contrib.auth.models import User
from .forms import UserDetailsForm, SkillForm, ProjectForm
from .models import UserDetails, Skill, Project

# Create your views here.
def index(request):
    return render(request, "MainApp/index.html", {})

@login_required
def user_details_form(request):
    user = request.user

    try:
        # Check if data already exists for the current user
        user_details = UserDetails.objects.get(user=user)
    except UserDetails.DoesNotExist:
        user_details = None

    if request.method == 'POST':
        form = UserDetailsForm(request.POST, request.FILES, instance=user_details)
        if form.is_valid():
            user_details = form.save(commit=False)
            user_details.user = request.user
            user_details.save()
            return redirect('user-details')
    else:
        form = UserDetailsForm(instance=user_details)

    return render(request, 'MainApp/user_details_form.html', {'form': form})

@login_required
def create_skill(request):
    user = request.user

    try:
        # Check if data already exists for the current user
        user_skills = Skill.objects.get(user=user)
    except Skill.DoesNotExist:
        user_skills = None

    if request.method == 'POST':
        form = SkillForm(request.POST, instance = user_skills)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.user = request.user  # associate user
            skill.save()
            return redirect('create-skills')  # Redirect to a success page
    else:
        form = SkillForm(instance = user_skills)

    return render(request, 'MainApp/create_skills_form.html', {'form': form})

@login_required
def create_project(request, project_id=None):
    user = request.user
    user_projects = Project.objects.filter(user=user)

    if project_id:
        # Editing an existing project
        project = get_object_or_404(Project, id=project_id, user=user)

        if request.method == 'POST':
            form = ProjectForm(request.POST, instance=project)
            if form.is_valid():
                project = form.save(commit=False)
                project.user = request.user
                project.save()
                return redirect('create-project')  # Redirect to page containing list and form
        else:
            form = ProjectForm(instance=project)

    else:
        # Creating a new project
        project = Project(user=user)

        if request.method == 'POST':
            form = ProjectForm(request.POST, instance=project)
            if form.is_valid():
                project = form.save(commit=False)
                project.user = request.user
                project.save()
                return redirect('create-project')  # Redirect to project list or another appropriate page
        else:
            form = ProjectForm()

    projects = Project.objects.filter(user=user)  # Retrieve all projects for display

    return render(request, 'MainApp/create_project_form.html', {'form': form, 'projects': projects})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('user-details')  # redirect to user portfolio view
    else:
        form = SignUpForm()
    return render(request, "MainApp/sign-up.html", {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('user-details')  # redirect to user portfolio view
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
    user = get_object_or_404(User, username=username)
    user_details = get_object_or_404(UserDetails, user=user)
    user_skills = get_object_or_404(Skill, user=user).name.split(",")

    context = {"user_details": user_details,
                "user_skills": user_skills
            }
    return render(request, 'MainApp/portfolio.html', context)
