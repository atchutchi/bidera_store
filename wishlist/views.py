from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.models import Product
from .models import WishlistItem
from django.http import JsonResponse

@login_required
def view_wishlist(request):
    """Display the user's wishlist with the items ordered by the date added."""
    wishlist_items = WishlistItem.objects.filter(user=request.user).order_by('-added_date')
    context = {'wishlist_items': wishlist_items}
    return render(request, 'wishlist/wishlist.html', context)

@login_required
def add_to_wishlist(request, product_id):
    """Add a product to the user's wishlist if not already added."""
    product = get_object_or_404(Product, id=product_id)
    # Ensure uniqueness with get_or_create
    wishlist_item, created = WishlistItem.objects.get_or_create(user=request.user, product=product)
    if created:
        messages.success(request, f'Added {product.name} to your wishlist!')
    else:
        messages.info(request, f'{product.name} is already in your wishlist.')
    return redirect(request.META.get('HTTP_REFERER', 'wishlist:view_wishlist'))

@login_required
def remove_from_wishlist(request, wishlist_item_id):
    """Remove an item from the user's wishlist."""
    wishlist_item = get_object_or_404(WishlistItem, id=wishlist_item_id, user=request.user)
    wishlist_item.delete()
    messages.success(request, 'Item removed from your wishlist.')
    return redirect(request.META.get('HTTP_REFERER', 'wishlist:view_wishlist'))


@login_required
def toggle_wishlist(request, product_id):
    """Toggle the wishlist status for a product."""
    product = get_object_or_404(Product, pk=product_id)
    wishlist_item, created = WishlistItem.objects.get_or_create(
        user=request.user, 
        product=product
    )
    
    if created:
        messages.success(request, f'{product.name} has been added to your wishlist.')
    else:
        wishlist_item.delete()
        messages.success(request, f'{product.name} has been removed from your wishlist.')
    
    return redirect(request.META.get('HTTP_REFERER', 'product_detail'))