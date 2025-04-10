from django.urls import path, include
from shop import views
#from .views import  ProductsListView


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
   #path("products/", ProductsListView.as_view(), name='product' ),
]