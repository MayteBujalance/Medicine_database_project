from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin interface
    path('medicines/', include('medicines.urls')),  # Include the medicines app URLs
    path('', views.index, name='index'),  # this shows all medicines
    path('search/', views.search, name='search'),  # this lets users search
]
