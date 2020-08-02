from django.urls import path

from . import views

app_name="wiki"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:name>", views.title, name="title"),
    path("?q="+"<str:search>", views.query, name="query")
]
