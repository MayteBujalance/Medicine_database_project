from django.contrib import admin
from .models import Medicine, Ingredient, Company


# Register your models here.

admin.site.register(Medicine)
admin.site.register(Ingredient)
admin.site.register(Company)
# The above code registers the Medicine, Ingredient, and Company models with the Django admin site.
# This allows these models to be managed through the Django admin interface, enabling CRUD operations on them
