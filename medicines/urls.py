from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),  # this shows all medicines
    path('search/', views.search, name='search'),  # this lets users search
]
