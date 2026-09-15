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


from django.shortcuts import render
from .models import Post


def index(request):
    # Получаем из базы только опубликованные записи (is_published=True)
    posts = Post.objects.filter(is_published=True)

    # Передаем список записей в контексте шаблона под именем 'posts'
    context = {
        'posts': posts
    }

    return render(request, 'main/index.html', context)