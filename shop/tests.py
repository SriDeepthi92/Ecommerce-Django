from django.test import TestCase
"""
    
def import_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            Product.objects.create(
                ProductId=row['ProductId'],
                ProductTitle=row['ProductTitle'],
                Gender=row['Gender'],
                category=row['Category'],
                ProductType=row['ProductType'],
                Colour=row['Colour'],
                price=row['Price'],
                image=row['Image'],
                imageURL=row['ImageURL']
            )

import_csv(r"C:\Users\sride\Downloads\fashion.csv")

def import_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            Category.objects.create(
                name=row['name'],
                description=row['description'] )

import_csv(r"C:\Users\sride\Downloads\category.csv")


import csv
from shop.models import Product, Category

def import_products(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Fetch the Category instance by name
            category_instance = Category.objects.get(name=row['Category'])
            
            # Create the Product instance
            Product.objects.create(
                ProductId=row['ProductId'],
                ProductTitle=row['ProductTitle'],
                Gender=row['Gender'],
                category=category_instance,  # Assign the Category instance
                ProductType=row['ProductType'],
                Colour=row['Colour'],
                price=row['Price'],
                image=row['Image'],
                imageURL=row['ImageURL']
            )

# Call the function to import products
import_products(r"C:\Users\sride\Downloads\fashion.csv")
"""