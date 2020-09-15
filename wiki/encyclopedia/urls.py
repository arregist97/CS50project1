from django.urls import path

from . import views

#app_name = "encyclopedia"
urlpatterns = [
    path("CSS", views.css, name="CSS"),
    path("<str:entry>", views.page, name="entry"),
    path("", views.index, name="index")
]
