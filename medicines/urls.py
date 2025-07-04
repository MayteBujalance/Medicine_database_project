from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_medicines, name='search_medicines'),
]
