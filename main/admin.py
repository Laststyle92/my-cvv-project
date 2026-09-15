from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'description')

from django.contrib import admin
from .models import Skill, Experience, Project

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('title', 'percent')

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('position', 'company', 'period')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'link')


from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Колонки, которые будут отображаться в списке записей
    list_display = ('title', 'created_at', 'is_published')

    # Поля, по которым можно кликнуть для перехода к редактированию
    list_display_links = ('title',)

    # Поля, по которым работает поиск
    search_fields = ('title', 'content')

    # Фильтры в правой колонке
    list_filter = ('is_published', 'created_at')

    # Возможность менять статус публикации прямо из списка
    list_editable = ('is_published',)