from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name = "Home"),
    path("index/", views.index, name = "Home"),
    path("project_views/", views.project_views, name = "project views"),
    path("contact/", views.contact, name = "contact"),
    path("list/", views.my_list , name = "data_base")
]