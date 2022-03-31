from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.index, name = "Home"),
    path("index/", views.index, name = "Home"),
    path("success/", views.index_form, name="Success")
] ##


