from django.shortcuts import get_object_or_404, render


# Create your views here.
def portfolio(request):
    """Portfolio page view

    Args:
        request (_object_): django Http request

    Returns:
        _object_: current class view object
    """
    return render(request, "UserApp/portfolio.html", {})
