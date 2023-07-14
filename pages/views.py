from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def home(request):
    return render(request, 'base.html')
def about(request):
    return render(request, 'pages/about.html')
def clothes(request):
    clothes = Clothes.objects.all()
    context = {
        'clothes': clothes
        }
    return render(
        request,
        'categories/clothes.html',
        context
    )
def clothes_detail(request, pk):
    try:
        cloth = Clothes.objects.get(id=pk)
    except Clothes.DoesNotExist:
        return render(request, 'errors/404.html')
    context = {
        'cloth': cloth
    }
    return render(
        request,
        'categories/clothes_detail.html',
        context
    )

def electronics(request):
    electronics = Electronics.objects.all()
    context = {
        'electronics': electronics
        }
    return render(request, 'categories/elec.html', context)
def elec_detail(request, pk):
    try:
        electronic = Electronics.objects.get(id=pk)
    except Electronics.DoesNotExist:
        return render(request, 'errors/404.html')
    context = {
        'electronic': electronic
    }
    return render(
        request,
        'categories/elec_detail.html',
        context
    )

def furnitures(request):
    furnitures = Furnutures.objects.all()
    context = {
        'furnitures': furnitures
        }
    return render(request, 'categories/furniture.html', context)
def fur_detail(request, pk):
    try:
        furniture = Furnutures.objects.get(id=pk)
    except Furnutures.DoesNotExist:
        return render(request, 'errors/404.html')
    context = {
        'furniture': furniture
    }
    return render(
        request,
        'categories/fur_detail.html',
        context
    )
def sports(request):
    sports = Sports.objects.all()
    context = {
        'sports': sports
        }
    return render(
        request,
        'categories/sport.html',
        context
    )
def sports_detail(request, pk):
    try:
        sport = Sports.objects.get(id=pk)
    except Sports.DoesNotExist:
        return render(request, 'errors/404.html')
    context = {
        'sport': sport
    }
    return render(
        request,
        'categories/sport_detail.html',
        context
    )
def households(request):
    households = Households.objects.all()
    context = {
        'households': households
        }
    return render(
        request,
        'categories/house.html',
        context
    )
def house_detail(request, pk):
    try:
        household = Households.objects.get(id=pk)
    except Households.DoesNotExist:
        return render(request, 'errors/404.html')
    context = {
        'household': household
    }
    return render(
        request,
        'categories/house_detail.html',
        context
    )
def cart(request):
    return render(request, 'pages/cart.html')
