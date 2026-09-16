from django.shortcuts import render
from .models import WorkExperience, Post, Item

def index(request):
    """
    Главная страница: загружает данные для 3D-книги (WorkExperience),
    новостей/записей (Post) и элементов (Item).
    """
    # 1. Страницы 3D-книги (сортировка по номеру страницы)
    try:
        pages = WorkExperience.objects.filter(is_published=True).order_by('page_number')
    except Exception:
        pages = WorkExperience.objects.all()

    # 2. Записи / Посты
    try:
        posts = Post.objects.filter(is_published=True).order_by('-created_at')
    except Exception:
        posts = Post.objects.all()

    # 3. Дополнительные элементы
    try:
        items = Item.objects.all().order_by('-created_at')
    except Exception:
        items = Item.objects.all()

    # Единый контекст со всеми данными
    context = {
        'pages': pages,
        'posts': posts,
        'items': items,
    }

    return render(request, 'main/index.html', context)


from django.shortcuts import render
from .models import WorkExperience, Post, Item, Skill, Project

def index(request):
    # Загружаем опубликованные страницы книги по порядку номеров
    try:
        pages = WorkExperience.objects.filter(is_published=True).order_by('page_number')
    except Exception:
        pages = WorkExperience.objects.all()

    context = {
        'pages': pages,
    }

    return render(request, 'main/index.html', context)

from django.shortcuts import render
from .models import WorkExperience, Profile

def index(request):
    pages = WorkExperience.objects.filter(is_published=True).order_by('page_number')
    profile = Profile.objects.first()  # Берем первую запись профиля

    return render(request, 'main/index.html', {
        'pages': pages,
        'profile': profile,
    })