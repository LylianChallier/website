from django.urls import path

from . import views

urlpatterns = [
    path("portfolio/", views.get_portfolio_data, name="portfolio-data"),
]
