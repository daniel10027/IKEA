from django.contrib import admin
from .models import Order, OrderItem, WishList, WishListItem, AdressseLivraison

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

class WishListItemInline(admin.TabularInline):
    model = WishListItem
    extra = 1

class AddressLivraisonInline(admin.TabularInline):
    model = AdressseLivraison
    extra = 1

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'created', 'complete', 'livre')
    inlines = [OrderItemInline, AddressLivraisonInline]

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('Produit', 'order', 'quantity', 'price', 'active', 'created')
    list_filter = ('active', 'created')

@admin.register(WishList)
class WishListAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'created', 'complete')
    inlines = [WishListItemInline]

@admin.register(WishListItem)
class WishListItemAdmin(admin.ModelAdmin):
    list_display = ('Produit', 'wish', 'quantity', 'active', 'created')
    list_filter = ('active', 'created')

@admin.register(AdressseLivraison)
class AddressLivraisonAdmin(admin.ModelAdmin):
    list_display = ('customer', 'localite', 'nom', 'email', 'telephone', 'order', 'created', 'date_update')

# Register your models here.
