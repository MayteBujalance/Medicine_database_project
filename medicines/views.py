from django.shortcuts import render
from .models import Medicine

# Create your views here.


def index(request):
    medicines = Medicine.objects.all()
    return render(request, 'medicines/index.html', {'medicines': medicines})
