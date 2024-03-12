from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm

from wishlist.models import WishlistItem  # Import the WishlistItem model

from checkout.models import Order

@login_required
def profile(request):
    """Display the user's profile including their wishlist."""
    profile = get_object_or_404(UserProfile, user=request.user)

    # Retrieve all wishlist items for the current user.
    # This query gets the WishlistItems related to the user, ensuring you have access to the added_date attribute.
    wishlist_items = WishlistItem.objects.filter(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    # Updated context to include wishlist_items
    context = {
        'form': form,
        'orders': orders,
        # Pass the wishlist items to the template. Each item has access to 'added_date' now.
        'wishlist_items': wishlist_items,
        'on_profile_page': True
    }

    return render(request, 'profiles/profile.html', context)

def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
