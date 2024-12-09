from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from .models import Flavor, Cart, CartItem, Allergen
from .forms import FlavorSuggestionForm, AllergenForm

def home(request):
    return render(request, 'core/home.html')

def flavor_list(request):
    flavors = Flavor.objects.filter(is_available=True)
    
    # Search functionality
    query = request.GET.get('q')
    if query:
        flavors = flavors.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        )
    
    # Filter by season
    season = request.GET.get('season')
    if season:
        flavors = flavors.filter(season=season)

    context = {
        'flavors': flavors,
        'seasons': Flavor.SEASON_CHOICES,
    }
    return render(request, 'core/flavor_list.html', context)

def flavor_detail(request, pk):
    flavor = get_object_or_404(Flavor, pk=pk)
    return render(request, 'core/flavor_detail.html', {'flavor': flavor})

@login_required
def add_to_cart(request, flavor_id):
    flavor = get_object_or_404(Flavor, id=flavor_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, flavor=flavor)
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    messages.success(request, f'{flavor.name} added to cart!')
    return redirect('flavor_list')

@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'core/cart.html', {'cart': cart})

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    cart_item.delete()
    messages.success(request, 'Item removed from cart!')
    return redirect('view_cart')

@login_required
def suggest_flavor(request):
    if request.method == 'POST':
        form = FlavorSuggestionForm(request.POST)
        if form.is_valid():
            suggestion = form.save(commit=False)
            suggestion.user = request.user
            suggestion.save()
            form.save_m2m()
            messages.success(request, 'Thank you for your suggestion!')
            return redirect('flavor_list')
    else:
        form = FlavorSuggestionForm()
    return render(request, 'core/suggestion_form.html', {'form': form})

@login_required
def add_allergen(request):
    if request.method == 'POST':
        form = AllergenForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Allergen added successfully!')
            return redirect('flavor_list')
    else:
        form = AllergenForm()
    return render(request, 'core/allergen_form.html', {'form': form}) 