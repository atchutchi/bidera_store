from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class WishlistItem(models.Model):
    user = models.ForeignKey(
            User, on_delete=models.CASCADE, related_name='wishlist_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} on {self.user.username}'s wishlist"
