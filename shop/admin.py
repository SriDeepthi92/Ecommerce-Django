from django.contrib import admin
from shop import models
from django.contrib.auth.models import Group


admin.site.register(models.Category)
admin.site.register(models.Product)