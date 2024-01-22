from django.contrib import admin
from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'email', 'contact', 'active', 'created', 'date_update')
    list_filter = ('active',)
    search_fields = ['name', 'email', 'contact']
  
# Register your model here.
