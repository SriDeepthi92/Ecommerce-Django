from django.shortcuts import render
from django.views.generic import ListView, TemplateView, View
from .models import *
from django.core.paginator import Paginator
from django.db.models import Q, Count, F
from profiles.decorators import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from profiles.models import CartItem
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse


@login_required(login_url='login')
def product_list(request):
    if request.user.is_staff:
        products = Product.objects.all()
        paginator = Paginator(products, 10)  # Show 10 products per page
        page_number = request.GET.get('page')  # Get the current page number from the URL
        page_obj = paginator.get_page(page_number)  # Get the products for the current page
        return render(request, 'product-list.html', {'page_obj': page_obj})
    else:
        products = Product.objects.filter(stock__gt=0)
      # Fetch all products
        paginator = Paginator(products, 10)  # Show 10 products per page
        page_number = request.GET.get('page')  # Get the current page number from the URL
        page_obj = paginator.get_page(page_number)  # Get the products for the current page
        return render(request, 'product-list.html', {'page_obj': page_obj})


@login_required(login_url='login')
def product_women(request):
    if request.user.is_staff:
        products = Product.objects.filter(Gender='Women') # Fetch all products
        paginator = Paginator(products, 10)  # Show 10 products per page

        page_number = request.GET.get('page')  # Get the current page number from the URL
        page_obj = paginator.get_page(page_number)  # Get the products for the current page

        return render(request, 'product-list.html', {'page_obj': page_obj})
    else:
        products = Product.objects.filter(Gender='Women', stock__gt=0) # Fetch all products
        paginator = Paginator(products, 10)  # Show 10 products per page

        page_number = request.GET.get('page')  # Get the current page number from the URL
        page_obj = paginator.get_page(page_number)  # Get the products for the current page

        return render(request, 'product-list.html', {'page_obj': page_obj})



@login_required(login_url='login')
def product_men(request):
    if request.user.is_staff:
        products = Product.objects.filter(Gender='Men') # Fetch all products
        paginator = Paginator(products, 10)  # Show 10 products per page

        page_number = request.GET.get('page')  # Get the current page number from the URL
        page_obj = paginator.get_page(page_number)  # Get the products for the current page

        return render(request, 'product-list.html', {'page_obj': page_obj})
    else:
        products = Product.objects.filter(Gender='Men', stock__gt=0) # Fetch all products
        paginator = Paginator(products, 10)  # Show 10 products per page

        page_number = request.GET.get('page')  # Get the current page number from the URL
        page_obj = paginator.get_page(page_number)  # Get the products for the current page

        return render(request, 'product-list.html', {'page_obj': page_obj})


@login_required(login_url='login')
def product_kids(request):
    if request.user.is_staff:
        products = Product.objects.filter(Q(Gender='Boys') | Q(Gender='Girls') ) # Fetch all products
        paginator = Paginator(products, 10)  # Show 10 products per page

        page_number = request.GET.get('page')  # Get the current page number from the URL
        page_obj = paginator.get_page(page_number)  # Get the products for the current page

        return render(request, 'product-list.html', {'page_obj': page_obj})
    else:
        products = Product.objects.filter(Q(Gender='Boys') | Q(Gender='Girls') | Q(stock__gt=0) ) # Fetch all products
        paginator = Paginator(products, 10)  # Show 10 products per page

        page_number = request.GET.get('page')  # Get the current page number from the URL
        page_obj = paginator.get_page(page_number)  # Get the products for the current page

        return render(request, 'product-list.html', {'page_obj': page_obj})


@login_required(login_url='login')
def product_boys(request):
    if request.user.is_staff:
        products = Product.objects.filter(Gender='Boys') # Fetch all products
        paginator = Paginator(products, 10)  # Show 10 products per page

        page_number = request.GET.get('page')  # Get the current page number from the URL
        page_obj = paginator.get_page(page_number)  # Get the products for the current page

        return render(request, 'shop-products.html', {'page_obj': page_obj})
    else:
        products = Product.objects.filter(Gender='Boys', stock__gt=0) # Fetch all products
        paginator = Paginator(products, 10)  # Show 10 products per page

        page_number = request.GET.get('page')  # Get the current page number from the URL
        page_obj = paginator.get_page(page_number)  # Get the products for the current page

        return render(request, 'shop-products.html', {'page_obj': page_obj})
    
    
@login_required(login_url='login')
def product_girls(request):
    if request.user.is_staff:
        products = Product.objects.filter(Gender='Girls') # Fetch all products
        paginator = Paginator(products, 10)  # Show 10 products per page

        page_number = request.GET.get('page')  # Get the current page number from the URL
        page_obj = paginator.get_page(page_number)  # Get the products for the current page

        return render(request, 'shop-products.html', {'page_obj': page_obj})
    else:
        products = Product.objects.filter(Gender='Girls', stock__gt=0) # Fetch all products
        paginator = Paginator(products, 10)  # Show 10 products per page

        page_number = request.GET.get('page')  # Get the current page number from the URL
        page_obj = paginator.get_page(page_number)  # Get the products for the current page

        return render(request, 'shop-products.html', {'page_obj': page_obj})
    

@login_required(login_url='login')
def product_footwear(request):
    if request.user.is_staff:
        products = Product.objects.filter(Q(category__name='Shoes') | Q(category__name='Flip Flops') | Q(category__name='Socks'))  # Fetch all products
        paginator = Paginator(products, 10)  # Show 10 products per page

        page_number = request.GET.get('page')  # Get the current page number from the URL
        page_obj = paginator.get_page(page_number)  # Get the products for the current page

        return render(request, 'shop-products.html', {'page_obj': page_obj})
    else:
        products = Product.objects.filter(Q(category__name='Shoes') | Q(category__name='Flip Flops') | Q(category__name='Socks') | Q(stock__gt=0))  # Fetch all products
        paginator = Paginator(products, 10)  # Show 10 products per page

        page_number = request.GET.get('page')  # Get the current page number from the URL
        page_obj = paginator.get_page(page_number)  # Get the products for the current page

        return render(request, 'shop-products.html', {'page_obj': page_obj})


@login_required(login_url='login')
def product_footwear_women(request):
    if request.user.is_staff:
        products = Product.objects.filter(Gender='Women', category__name__in=['Shoes', 'Flip Flops','Socks'])  # Fetch all products
        paginator = Paginator(products, 10)  # Show 10 products per page

        page_number = request.GET.get('page')  # Get the current page number from the URL
        page_obj = paginator.get_page(page_number)  # Get the products for the current page

        return render(request, 'shop-products.html', {'page_obj': page_obj})
    else:
        products = Product.objects.filter(Gender='Women', category__name__in=['Shoes', 'Flip Flops','Socks'], stock__gt=0)  # Fetch all products
        paginator = Paginator(products, 10)  # Show 10 products per page

        page_number = request.GET.get('page')  # Get the current page number from the URL
        page_obj = paginator.get_page(page_number)  # Get the products for the current page

        return render(request, 'shop-products.html', {'page_obj': page_obj})

@login_required(login_url='login')
def product_footwear_men(request):
    if request.user.is_staff:
        products = Product.objects.filter(Gender='Men', category__name__in=['Shoes', 'Flip Flops','Socks'])  # Fetch all products
        paginator = Paginator(products, 10)  # Show 10 products per page

        page_number = request.GET.get('page')  # Get the current page number from the URL
        page_obj = paginator.get_page(page_number)  # Get the products for the current page

        return render(request, 'shop-products.html', {'page_obj': page_obj})
    else:
        products = Product.objects.filter(Gender='Men', category__name__in=['Shoes', 'Flip Flops','Socks'], stock__gt=0)  # Fetch all products
        paginator = Paginator(products, 10)  # Show 10 products per page

        page_number = request.GET.get('page')  # Get the current page number from the URL
        page_obj = paginator.get_page(page_number)  # Get the products for the current page

        return render(request, 'shop-products.html', {'page_obj': page_obj})

@login_required(login_url='login')
def product_footwear_girls(request):
    if request.user.is_staff:
        products = Product.objects.filter(Gender='Girls', category__name__in=['Shoes', 'Flip Flops','Socks'])  # Fetch all products
        paginator = Paginator(products, 10)  # Show 10 products per page

        page_number = request.GET.get('page')  # Get the current page number from the URL
        page_obj = paginator.get_page(page_number)  # Get the products for the current page

        return render(request, 'shop-products.html', {'page_obj': page_obj})
    else:
        products = Product.objects.filter(Gender='Girls', category__name__in=['Shoes', 'Flip Flops','Socks'], stock__gt=0)  # Fetch all products
        paginator = Paginator(products, 10)  # Show 10 products per page

        page_number = request.GET.get('page')  # Get the current page number from the URL
        page_obj = paginator.get_page(page_number)  # Get the products for the current page

        return render(request, 'shop-products.html', {'page_obj': page_obj})

@login_required(login_url='login')
def product_footwear_boys(request):
    if request.user.is_staff:
        products = Product.objects.filter(Gender='Boys', category__name__in=['Shoes', 'Flip Flops','Socks'])  # Fetch all products
        paginator = Paginator(products, 10)  # Show 10 products per page

        page_number = request.GET.get('page')  # Get the current page number from the URL
        page_obj = paginator.get_page(page_number)  # Get the products for the current page

        return render(request, 'shop-products.html', {'page_obj': page_obj})
    else:
        products = Product.objects.filter(Gender='Boys', category__name__in=['Shoes', 'Flip Flops','Socks'], stock__gt=0)  # Fetch all products
        paginator = Paginator(products, 10)  # Show 10 products per page

        page_number = request.GET.get('page')  # Get the current page number from the URL
        page_obj = paginator.get_page(page_number)  # Get the products for the current page

        return render(request, 'shop-products.html', {'page_obj': page_obj})
    

"""
@login_required(login_url='login')
def add_to_cart(request, product_id):
    print(request.user)  # Should print the username or user object
    print(type(request.user)) 
    product = get_object_or_404(Product, ProductId=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)

    # Check if the product is already in the cart
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        # If the product is already in the cart, increase the quantity
        cart_item.quantity += 1
        cart_item.save()
        messages.info(request, f"Updated {product.ProductId} quantity in your cart.")
    else:
        messages.success(request, f"Added {product.ProductId} to your cart.")

    return redirect('cart_view')


@login_required
def cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.items.all()
    total_price = sum(item.product.price * item.quantity for item in cart_items)

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'cart.html', context)

@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, cart__user=request.user)
    cart_item.delete()
    messages.success(request, "Item removed from your cart.")
    return redirect('cart_view')"

"""
@login_required(login_url='login')
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, ProductId=product_id)

    # Check if the product is in stock
    if not product.is_in_stock:
        messages.error(request, f"Sorry, {product.ProductId} is out of stock.")
        return redirect('product_list')
    
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        if cart_item.quantity < product.stock:
            cart_item.quantity += 1
            cart_item.save()
            messages.info(request, f"Updated {product.name} quantity in your cart.")
        else:
            messages.error(request, f"Only {product.stock} of {product.name} available.")
    else:
        messages.success(request, f"Added {product.ProductId} to your cart.")

    return redirect('view_cart')


@login_required(login_url='login')
def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, ProductId=product_id)
    cart_item = CartItem.objects.filter(user=request.user, product=product).first()
    if cart_item:
        cart_item.delete()
        messages.success(request, "Item removed from your cart.")
    return redirect('view_cart')

@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, "cart.html", {"cart_items": cart_items, "total_price": total_price})