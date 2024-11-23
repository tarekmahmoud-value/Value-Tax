from django.urls import path
from .import views

urlpatterns = [
path("", views.login_index,name ="login_index")
    ]