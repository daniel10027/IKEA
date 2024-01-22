from django.contrib import admin
from .models import Categorie, Produit, ImageProduit

# Register your models here.

class ImageProduitInline(admin.TabularInline):
    model = ImageProduit
    extra = 1
    
@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('titre', 'active', 'created', 'date_update')
    search_fields = ['titre']

@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ('titre', 'categorie', 'prix', 'en_promo', 'pourcentage_promo', 'active', 'created', 'date_update')
    list_filter = ('categorie', 'en_promo', 'active')
    inlines = [ImageProduitInline,]
    search_fields = ['titre']

@admin.register(ImageProduit)
class ImageProduitAdmin(admin.ModelAdmin):
    list_display = ('produit', 'active', 'created', 'date_update')
    list_filter = ('active',)
    search_fields = ['produit__titre']


