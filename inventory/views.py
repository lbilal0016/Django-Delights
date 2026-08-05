from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomeView(TemplateView):
    template_name = "inventory/home.html"

class MenuView(TemplateView):
    template_name = "inventory/menus.html"

class IngredientsView(TemplateView):
    template_name = "inventory/ingredients.html"

class PurchasesView(TemplateView):
    template_name = "inventory/purchases.html"