from django.db import models
from django.core.validators import MinValueValidator

class Ingredient(models.Model):
    name = models.CharField(
        max_length=30,
    )

    unit_price = models.DecimalField(max_digits=10, decimal_places=2,validators=[MinValueValidator(0)])
    stock_amount = models.DecimalField(max_digits=10, decimal_places=2,validators=[MinValueValidator(0)])

    def __str__(self):
        return self.name

# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(max_length=30)

    ingredients = models.ManyToManyField(
        Ingredient,
        through="RecipeRequirement",
        related_name="menu_items",
    )

    price = models.DecimalField(max_digits=10, decimal_places=2,validators=[MinValueValidator(0)])

    def __str__(self):
            return self.name


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

    quantity = models.DecimalField(max_digits=10, decimal_places=2,validators=[MinValueValidator(1)])

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["menu_item", "ingredient"],
                name="unique_menu_item_ingredient",
            )
        ]

    def __str__(self):
            return f"{self.menu_item} - {self.ingredient}: {self.quantity}"

class Purchase(models.Model):
    #   models.PROTECT: avoids deleting a menu item if there is a purchase including this menu
    purchased_item = models.ForeignKey(MenuItem, on_delete=models.PROTECT, related_name="purchases")
    purchase_amount = models.IntegerField(validators=[MinValueValidator(1)])
    purchase_date = models.DateTimeField(auto_now_add=True)

    #   this field is not edited by the user. It will be modifed by the app in views
    total_price_at_purchase = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        editable=False,
    )

    def __str__(self):
            return f"{self.purchased_item} x {self.purchase_amount}"