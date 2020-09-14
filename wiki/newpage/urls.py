from django.urls import path

from . import views

app_name = "newpage"
urlpatterns = [
    path("",views.index, name="index")
]