from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def index(request):
    return render(request, "min_dup/index.html")


def about(request):
    return render(request, "min_dup/about.html")
