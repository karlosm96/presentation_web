from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name = "Home"),
    path("index/", views.index, name = "Home"),
    path("success/", views.index_form, name="Success")
]