from django.shortcuts import get_object_or_404, render


# Create your views here.
def index(request):
    """index page view

    Args:
        request (_object_): django Http request

    Returns:
        _object_: current class view object
    """
    return render(request, "MainApp/index.html", {})


def signUp(request):
    """sign-up page view

    Args:
        request (_object_): django Http request

    Returns:
        _object_: current class view object
    """
    return render(request, "MainApp/sign-up.html", {})

def logIn(request):
    """login page view

    Args:
        request (_object_): django Http request

    Returns:
        _object_: current class view object
    """
    return render(request, "MainApp/login.html", {})
