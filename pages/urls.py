from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('clothes/', clothes, name='clothes'),
    path('clothes/<pk>/', clothes_detail, name='clothes_detail'),
    path('clothes/<pk>/delete/', clothes_delete, name='clothes_delete'),
    path('clothes/<pk>/update/', clothes_update, name='clothes_update'),
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
    path('create/', create, name='create'),
    path('create2/', create2, name='create2'),
    path('create3/', create3, name='create3'),
    path('create4/', create4, name='create4'),
    path('create5/', create5, name='create5'),

]