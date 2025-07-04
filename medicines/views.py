from django.shortcuts import render
from .models import Medicine, Ingredient

# View to show all medicines
def index(request):
    medicines = Medicine.objects.all()
    return render(request, 'medicines/index.html', {'medicines': medicines})

# View to search by ingredient
def search(request):
    query = request.GET.get('ingredient')
    medicines = []

    if query:
        medicines = Medicine.objects.filter(ingredients__name__icontains=query).distinct()

    return render(request, 'medicines/search.html', {
        'query': query,
        'medicines': medicines
    })
