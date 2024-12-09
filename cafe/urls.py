from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('flavors/', views.flavor_list, name='flavor_list'),
    path('flavor/<int:pk>/', views.flavor_detail, name='flavor_detail'),
    path('cart/', views.view_cart, name='view_cart'),
    path('cart/add/<int:flavor_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('suggest/', views.suggest_flavor, name='suggest_flavor'),
    path('allergen/add/', views.add_allergen, name='add_allergen'),
] 