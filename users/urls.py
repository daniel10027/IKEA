from django.urls import path
from django.contrib.auth import views as auth_views

from .views import (

    
    signup,
    activate_account,
    profile, 
    logout_view, 
    adminOrder
    

)

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='sites/login.html'), name="login"),
    path('activate/<uidb64>/<token>/', activate_account, name='activate_account'),
    path('myProfile/', profile, name='profile'),
    path('logout_view/', logout_view, name='logout_view'),
    path('adminOrder/', adminOrder, name='adminOrder'),
    
    
]
