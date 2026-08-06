from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Ingredient, MenuItem, Purchase, RecipeRequirement
from .forms import IngredientCreateForm, MenuItemCreateForm, PurchaseCreateForm, RecipeRequirementCreateForm

# Create your views here.
class HomeView(TemplateView):
    template_name = "inventory/home.html"

class MenuView(TemplateView):
    template_name = "inventory/menus.html"

    #   send menu objects to menus.html template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menus"] = MenuItem.objects.all()
        return context

class IngredientsView(TemplateView):
    template_name = "inventory/ingredients.html"

class PurchasesView(TemplateView):
    template_name = "inventory/purchases.html"

#   Create views
class MenuCreate(CreateView):
    model = MenuItem
    form_class = MenuItemCreateForm
    template_name = "inventory/menuitem_create_form.html"

    def get_success_url(self):
        return reverse(
            "createreciperequirement", #    this should match url name
            kwargs={"menu_pk":  self.object.pk},    #   this argument should match url argument menu_pk
        )

class RecipeRequirementsCreate(CreateView):
    model = RecipeRequirement
    form_class = RecipeRequirementCreateForm
    template_name = "inventory/reciperequirement_create_form.html"

    def form_valid(self, form):
        # fetch the menu to which a recipe requirement will be added
        menu_item = get_object_or_404(
            MenuItem,
            pk = self.kwargs["menu_pk"],
        )

        form.instance.menu_item = menu_item
        return super().form_valid(form)

    def get_success_url(self):
        action = self.request.POST.get("action")

        #   redirect to the same page to add another ingredient
        if action == "add_another":
            return reverse(
                "createreciperequirement",
                kwargs={"menu_pk": self.kwargs["menu_pk"]},
            )

        #   redirect to menus page when all ingredients are added
        return reverse("menus")