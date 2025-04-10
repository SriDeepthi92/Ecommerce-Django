from django.urls import path, include
from shop import views
#from .views import  ProductsListView
from .views import add_to_cart, remove_from_cart, view_cart


urlpatterns = [
   path('products/', views.product_list, name='product'), 
   path('women/', views.product_women, name='women'),
   path('men/', views.product_men, name='men'),
   path('kids/', views.product_kids, name='kids'),
   path('boys/', views.product_boys, name='boys'),
   path('girls/', views.product_girls, name='girls'),
   path('footwear/', views.product_footwear, name='footwear'),
   path('footwear/women', views.product_women, name='footwear_women'),
   path('footwear/men', views.product_men, name='footwear_men'),
   path('footwear/girls', views.product_footwear_girls, name='footwear_girls'),
   path('footwear/boys', views.product_footwear_boys, name='footwear_boys'),
   path("cart/add/<int:product_id>/", add_to_cart, name="add_to_cart"),
    path("cart/remove/<int:product_id>/", remove_from_cart, name="remove_from_cart"),
    path("cart/", view_cart, name="view_cart"),
   #path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
   #path('cart/', views.cart_view, name='cart_view'),
   #path('remove-from-cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
   #path("products/", ProductsListView.as_view(), name='product' ),
]