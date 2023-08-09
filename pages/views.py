from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *

def home(request):
    return render(request, 'base.html')
def about(request):
    return render(request, 'pages/about.html')

@login_required(login_url='login')
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
def clothes_delete(request, pk):
    product = Clothes.objects.get(id=pk)
    product.delete()
    return redirect(to='clothes')
def clothes_update(request, pk):
    product = Clothes.objects.get(id=pk)
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            image = form.cleaned_data['image']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            author = form.cleaned_data['author']
            authornum = form.cleaned_data['author_num']
            condition = form.cleaned_data['condition']
            product.title = title
            product.image = image
            product.description = description
            product.price = price
            product.author = author
            product.author_num = authornum
            product.condition = condition
            product.save()

            return redirect(to='clothes')
    context = {
        'form': form
    }
    return render(request, 'pages/update.html', context)
@login_required(login_url='login')
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
@login_required(login_url='login')
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
@login_required(login_url='login')
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
@login_required(login_url='login')
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
@login_required(login_url='login')
def create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect(to='clothes')
    else:
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, 'pages/create.html', context)

@login_required(login_url='login')
def create2(request):
    if request.method == 'POST':
        form = ProductForm2(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect(to='electronics')
    else:
        form = ProductForm2()
    context = {
        'form': form
    }
    return render(request, 'pages/create.html', context)
@login_required(login_url='login')
def create3(request):
    if request.method == 'POST':
        form = ProductForm3(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect(to='furnitures')
    else:
        form = ProductForm3()
    context = {
        'form': form
    }
    return render(request, 'pages/create.html', context)
@login_required(login_url='login')
def create4(request):
    if request.method == 'POST':
        form = ProductForm4(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect(to='sports')
    else:
        form = ProductForm4()
    context = {
        'form': form
    }
    return render(request, 'pages/create.html', context)
@login_required(login_url='login')
def create5(request):
    if request.method == 'POST':
        form = ProductForm5(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect(to='households')
    else:
        form = ProductForm5()
    context = {
        'form': form
    }
    return render(request, 'pages/create.html', context)