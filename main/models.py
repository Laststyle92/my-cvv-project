from django.db import models


class Item(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='items/', blank=True, null=True, verbose_name="Изображение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Элемент"
        verbose_name_plural = "Элементы"


class Skill(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название навыка")
    percent = models.PositiveIntegerField(default=50, verbose_name="Уровень владения (%)")

    class Meta:
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"

    def __str__(self):
        return self.title


class Experience(models.Model):
    company = models.CharField(max_length=100, verbose_name="Компания/Организация")
    position = models.CharField(max_length=100, verbose_name="Должность")
    period = models.CharField(max_length=50, verbose_name="Период работы")
    description = models.TextField(verbose_name="Описание обязанностей")

    class Meta:
        verbose_name = "Опыт работы"
        verbose_name_plural = "Опыт работы"

    def __str__(self):
        return f"{self.position} — {self.company}"


class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название проекта")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='projects/', verbose_name="Скриншот/Обложка")
    link = models.URLField(blank=True, null=True, verbose_name="Ссылка на проект")

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержимое")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
        ordering = ['-created_at']

    def __str__(self):
        return self.title


# --- НОВАЯ МОДЕЛЬ ДЛЯ 3D-КНИГИ ИСТОРИИ РАБОТ ---
from django.db import models

class WorkExperience(models.Model):
    page_number = models.IntegerField(default=1, verbose_name="Номер страницы")
    position = models.CharField(max_length=255, verbose_name="Должность / Название этапа")
    company_name = models.CharField(max_length=255, verbose_name="Организация / Компания")
    period = models.CharField(max_length=100, verbose_name="Период (например: 2020 — 2022)")
    skills_and_achievements = models.TextField(verbose_name="Навыки и достижения")
    description = models.TextField(verbose_name="Описание работы")
    bg_image = models.ImageField(upload_to='book_bg/', blank=True, null=True, verbose_name="Фоновый рисунок")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

    class Meta:
        verbose_name = "Этап работы (Книга)"
        verbose_name_plural = "Этапы работы (Книга)"
        ordering = ['page_number']

    def __str__(self):
        return f"Страница {self.page_number}: {self.position}"


from django.db import models


class Page(models.Model):
    position = models.CharField(max_length=200, verbose_name="Должность / Заголовок")
    company_name = models.CharField(max_length=200, verbose_name="Организация")
    period = models.CharField(max_length=100, verbose_name="Период работы")
    skills_and_achievements = models.TextField(blank=True, verbose_name="Навыки и достижения")
    description = models.TextField(blank=True, verbose_name="Подробное описание")

    # Поле для фотографии (занимает 1/3 в верстке)
    image = models.ImageField(upload_to='pages_photos/', blank=True, null=True, verbose_name="Фото страницы")

    # Флаг публикации / сортировка
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    order = models.IntegerField(default=0, verbose_name="Порядок сортировки")

    class Meta:
        verbose_name = "Страница книги"
        verbose_name_plural = "Страницы книги"
        ordering = ['order', 'id']

    def __str__(self):
        return f"{self.position} - {self.company_name}"

class WorkPage(models.Model):  # Ваша модель
    # ... ваши текущие поля ...
    photo = models.ImageField(upload_to='profiles/', blank=True, null=True, verbose_name="Фото профиля")

from django.db import models

class Profile(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="Имя и Фамилия")
    title = models.CharField(max_length=150, verbose_name="Должность / Специализация")
    photo = models.ImageField(upload_to='profiles/', verbose_name="Фото профиля", blank=True, null=True)
    bio = models.TextField(verbose_name="О себе / Краткое описание", blank=True)

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профиль"

    def __str__(self):
        return self.full_name