"""URLs da app portfolio."""

from django.urls import path
from .views import HomeView

# namespace declarado aqui e no include do config/urls.py
app_name = "portfolio"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
]
