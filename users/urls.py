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
    
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='sites/password/password_reset.html'), name="password_reset"),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(  template_name='sites/password/password_reset_done.html'), name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view( template_name='sites/password/password_reset_confirm.html'),name="password_reset_confirm"),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='sites/password/password_reset_complete.html'), name="password_reset_complete"),
    
    
]
