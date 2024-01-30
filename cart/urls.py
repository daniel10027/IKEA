from django.urls import path
from .views import (

    cart,
    checkout,
    wishlist,
    updateItem, 
    orderdetails
)

urlpatterns = [

    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('wishlist/', wishlist, name='wishlist'),
    path('update_item/', updateItem, name='updateItem'),
    path('orderdetails/ZjaHJvbWUqDggAEEUYJxg7GIAEG<int:pk>IoFMg4IABBFGCcYOxiABBiKBTIGCAEQRRg5Mg0IAhAAGIMBGLEDGIAEMgYIAxBFGDwyBggEEEUYPDIGCAUQRRg8MgYIBhBFGEEyBggHEEUYQagCALACAA&sourceid=chrome&ie=', orderdetails, name='orderdetails'),

     
   
    
]
