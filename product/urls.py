from django.urls import path

from .views import (
   
    order_tracking,
    product_details,
    shoplist,
    ShopListView,
    ProductDetailView
   


)

urlpatterns = [
    path('order-tracking/', order_tracking, name='order_tracking'),
    path('produit/<int:pk>/<slug:slug>/', ProductDetailView.as_view(), name='product_details'),
    path('shoplist/', shoplist, name='shoplist'),
    path('shop/', ShopListView.as_view(), name='shop'),
]
