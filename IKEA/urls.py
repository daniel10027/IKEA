from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    path('tinymce/', include('tinymce.urls')),
    path('admin/', admin.site.urls),
    path('', include("sites.urls")),
    path('mon-panier/', include("cart.urls")),
    path('nos-produits/', include("product.urls")),
    path('accounts/', include("users.urls")),
   
]

if settings.DEBUG:
    
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)