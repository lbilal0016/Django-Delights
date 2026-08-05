from django.db import models
from django.core.validators import MinValueValidator
import datetime

class Ingredient(models.Model):
    name = models.CharField(
        max_length=30,
    )

    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_amount = models.DecimalField(max_digits=10, decimal_places=2)

# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(max_length=30)

    ingredients = models.ManyToManyField(
        Ingredient,
        through="RecipeRequirement",
        related_name="menu_items",
    )

    price = models.DecimalField(max_digits=10, decimal_places=2)

#   This model manages menu N --- N ingredient many-to-many relationship
class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(
        MenuItem,
        on_delete=models.CASCADE,
        related_name="recipe_requirements",
    )

    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name="recipe_requirements"
    )

    quantity = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["menu_item", "ingredient"],
                name="unique_menu_item_ingredient",
            )
        ]

class Purchase(models.Model):
    #   models.PROTECT: avoids deleting a menu item if there is a purchase including this menu
    purchased_item = models.ForeignKey(MenuItem, on_delete=models.PROTECT, related_name="purchases")
    purchase_amount = models.IntegerField(validators=[MinValueValidator(1)])
    purchase_date = models.DateTimeField()

    #   this field is not edited by the user. It will be modifed by the app in views
    total_price_at_purchase = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        editable=False,
    )
