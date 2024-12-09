from django.contrib import admin
from .models import Flavor, Ingredient, Allergen, Cart, CartItem, FlavorSuggestion

admin.site.register(Flavor)
admin.site.register(Ingredient)
admin.site.register(Allergen)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(FlavorSuggestion) 