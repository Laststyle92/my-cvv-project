from django.contrib import admin
from .models import Item, Skill, Experience, Project, Post, WorkExperience


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'description')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('title', 'percent')


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('position', 'company', 'period')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'link')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_published')
    list_display_links = ('title',)
    search_fields = ('title', 'content')
    list_filter = ('is_published', 'created_at')
    list_editable = ('is_published',)


@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('page_number', 'position', 'company_name', 'period', 'is_published')
    list_display_links = ('position',)  # Делаем ссылкой должность, чтобы исправить ошибку E124
    list_editable = ('page_number', 'is_published')
    ordering = ('page_number',)

from django.contrib import admin
from .models import Profile, WorkExperience  # Замените на ваши модели

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'title')