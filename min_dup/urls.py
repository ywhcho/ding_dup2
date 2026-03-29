from django.urls import path

from . import views

app_name = "min_dup"

urlpatterns = [
    path("", views.index, name="index"),
]