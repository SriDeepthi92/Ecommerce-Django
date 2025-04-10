from django.shortcuts import render
from django.views.generic import ListView, TemplateView, View
from .models import *
from django.core.paginator import Paginator
from django.db.models import Q, Count, F



def product_list(request):
    products = Product.objects.all()  # Fetch all products
    paginator = Paginator(products, 10)  # Show 10 products per page

    page_number = request.GET.get('page')  # Get the current page number from the URL
    page_obj = paginator.get_page(page_number)  # Get the products for the current page

    return render(request, 'product-list.html', {'page_obj': page_obj})

def product_women(request):
    products = Product.objects.filter(Gender='Women') # Fetch all products
    paginator = Paginator(products, 10)  # Show 10 products per page

    page_number = request.GET.get('page')  # Get the current page number from the URL
    page_obj = paginator.get_page(page_number)  # Get the products for the current page

    return render(request, 'product-list.html', {'page_obj': page_obj})

def product_men(request):
    products = Product.objects.filter(Gender='Men') # Fetch all products
    paginator = Paginator(products, 10)  # Show 10 products per page

    page_number = request.GET.get('page')  # Get the current page number from the URL
    page_obj = paginator.get_page(page_number)  # Get the products for the current page

    return render(request, 'product-list.html', {'page_obj': page_obj})

def product_kids(request):
    products = Product.objects.filter(Q(Gender='Boys') | Q(Gender='Girls') ) # Fetch all products
    paginator = Paginator(products, 10)  # Show 10 products per page

    page_number = request.GET.get('page')  # Get the current page number from the URL
    page_obj = paginator.get_page(page_number)  # Get the products for the current page

    return render(request, 'product-list.html', {'page_obj': page_obj})



def product_boys(request):
    products = Product.objects.filter(Gender='Boys') # Fetch all products
    paginator = Paginator(products, 10)  # Show 10 products per page

    page_number = request.GET.get('page')  # Get the current page number from the URL
    page_obj = paginator.get_page(page_number)  # Get the products for the current page

    return render(request, 'shop-products.html', {'page_obj': page_obj})

def product_girls(request):
    products = Product.objects.filter(Gender='Girls') # Fetch all products
    paginator = Paginator(products, 10)  # Show 10 products per page

    page_number = request.GET.get('page')  # Get the current page number from the URL
    page_obj = paginator.get_page(page_number)  # Get the products for the current page

    return render(request, 'shop-products.html', {'page_obj': page_obj})


def product_footwear(request):
    products = Product.objects.filter(Q(category__name='Shoes') | Q(category__name='Flip Flops') | Q(category__name='Socks'))  # Fetch all products
    paginator = Paginator(products, 10)  # Show 10 products per page

    page_number = request.GET.get('page')  # Get the current page number from the URL
    page_obj = paginator.get_page(page_number)  # Get the products for the current page

    return render(request, 'shop-products.html', {'page_obj': page_obj})



def product_footwear_women(request):
    products = Product.objects.filter(Gender='Women', category__name__in=['Shoes', 'Flip Flops','Socks'])  # Fetch all products
    paginator = Paginator(products, 10)  # Show 10 products per page

    page_number = request.GET.get('page')  # Get the current page number from the URL
    page_obj = paginator.get_page(page_number)  # Get the products for the current page

    return render(request, 'shop-products.html', {'page_obj': page_obj})



def product_footwear_men(request):
    products = Product.objects.filter(Gender='Men', category__name__in=['Shoes', 'Flip Flops','Socks'])  # Fetch all products
    paginator = Paginator(products, 10)  # Show 10 products per page

    page_number = request.GET.get('page')  # Get the current page number from the URL
    page_obj = paginator.get_page(page_number)  # Get the products for the current page

    return render(request, 'shop-products.html', {'page_obj': page_obj})



def product_footwear_girls(request):
    products = Product.objects.filter(Gender='Girls', category__name__in=['Shoes', 'Flip Flops','Socks'])  # Fetch all products
    paginator = Paginator(products, 10)  # Show 10 products per page

    page_number = request.GET.get('page')  # Get the current page number from the URL
    page_obj = paginator.get_page(page_number)  # Get the products for the current page

    return render(request, 'shop-products.html', {'page_obj': page_obj})


def product_footwear_boys(request):
    products = Product.objects.filter(Gender='Boys', category__name__in=['Shoes', 'Flip Flops','Socks'])  # Fetch all products
    paginator = Paginator(products, 10)  # Show 10 products per page

    page_number = request.GET.get('page')  # Get the current page number from the URL
    page_obj = paginator.get_page(page_number)  # Get the products for the current page

    return render(request, 'shop-products.html', {'page_obj': page_obj})