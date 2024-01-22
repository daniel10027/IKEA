from django.urls import path
from .views import (
    about,
    contact,
    faq,
    index,
    tracking

)

urlpatterns = [
    
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('gallerie/', faq, name='faq'),
    path('tracking/', tracking, name='tracking'),
    


]
