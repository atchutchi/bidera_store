from django.urls import path
from . import views

app_name = 'wishlist'

urlpatterns = [
    path('', views.view_wishlist, name='view_wishlist'),
    path('add/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('remove/<int:wishlist_item_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('toggle/<int:product_id>/', views.toggle_wishlist, name='toggle_wishlist'),

]
