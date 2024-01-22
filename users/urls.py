from django.contrib import admin
from django.urls import path, include


from .views import (

    login,
    signup,

)

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
]
