from django.urls import path
from .views import (

    cart,
    checkout,
    wishlist,
    updateItem
)

urlpatterns = [

    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('wishlist/', wishlist, name='wishlist'),
    path('update_item/', updateItem, name='updateItem'),

     
   
    
]
