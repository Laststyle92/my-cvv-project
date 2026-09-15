from django.shortcuts import render
from .models import Item

def index(request):
    # Получаем все объекты из PostgreSQL, отсортированные по дате
    items = Item.objects.all().order_by('-created_at')

    # Передаем данные в контекст шаблона
    context = {
        'items': items
    }
    return render(request, 'main/index.html', context)

from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')