from django import template
from wishlist.models import WishlistItem

register = template.Library()

@register.filter(name='in_user_wishlist')
def in_user_wishlist(product, user):
    """
    Checks if a given product is in the user's wishlist.
    Usage in template: {% if product|in_user_wishlist:user %}
    """
    return WishlistItem.objects.filter(user=user, product=product).exists()
