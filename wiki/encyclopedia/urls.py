from django.urls import path

from . import views

#app_name = "encyclopedia"
urlpatterns = [
    path("random/", views.randompage, name="randompage"),
    path("search/", views.search, name="query"),
    path("<str:entry>", views.page, name="entry"),
    path("", views.index, name="index")
]
