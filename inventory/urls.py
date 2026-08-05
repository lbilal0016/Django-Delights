from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('menus', views.MenuView.as_view(), name='menus'),
    path('ingredients', views.IngredientsView.as_view(), name='ingredients'),
    path('purchases', views.PurchasesView.as_view(), name='purchases'),
]