from django.shortcuts import render


def index(request):  # pragma: no cover
    return render(request, 'frontend/index.html')