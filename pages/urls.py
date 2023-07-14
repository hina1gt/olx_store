from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('clothes/', clothes, name='clothes'),
    path('clothes/<pk>/', clothes_detail, name='clothes_detail'),
    path('electronics/', electronics, name='electronics'),
    path('electronics/<pk>/', elec_detail, name='elec_detail'),
    path('furnitures/', furnitures, name='furnitures'),
    path('furnitures/<pk>/', fur_detail, name='fur_detail'),
    path('sport/', sports, name='sports'),
    path('sport/<pk>/', sports_detail, name='sports_detail'),
    path('household/', households, name='household'),
    path('household/<pk>/', house_detail, name='house_detail'),
    path('about/', about, name='about'),
    path('cart/', cart, name='cart'),
]