from django.urls import path

from . import views

urlpatterns = [
    path("CSS", views.css, name="CSS"),
    path("", views.index, name="index")
]
