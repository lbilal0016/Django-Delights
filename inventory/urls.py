from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('menus', views.MenuView.as_view(), name='menus'),
]