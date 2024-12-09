from django.urls import path
from .import views

urlpatterns = [
    path("", views.register_index, name="register_index")
]