from django.urls import path
from .views import tax_calculation_view

urlpatterns = [
    path("", tax_calculation_view, name="tax_calculation"),
]