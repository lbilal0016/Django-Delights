from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('menus/', views.MenuView.as_view(), name='menus'),
    path('menus/<int:menu_pk>/requirements/', views.MenuRequirementsView.as_view(), name='menurequirements'),
    path('ingredients/', views.IngredientsView.as_view(), name='ingredients'),
    path('purchases/', views.PurchasesView.as_view(), name='purchases'),
    path('menus/create/', views.MenuCreate.as_view(), name="menucreate"),
    path('menus/<int:menu_pk>/update/', views.UpdateMenuView.as_view(), name="menuupdate"),
    path('ingredients/create/', views.IngredientCreate.as_view(), name="ingredientcreate"),
    path('menus/<int:menu_pk>/requirements/create/', views.RecipeRequirementsCreate.as_view(), name="createreciperequirement"),
    path('menus/<int:menu_pk>/requirements/<int:requirement_pk>/update/', views.RecipeRequirementUpdate.as_view(), name="updatereciperequirement"),
]