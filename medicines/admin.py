from django.contrib import admin
from .models import Medicine


# Register your models here.

admin.site.register(Medicine)

# The above code registers the Medicine, Ingredient, and Company models with the Django admin site.
# This allows these models to be managed through the Django admin interface, enabling CRUD operations on them
