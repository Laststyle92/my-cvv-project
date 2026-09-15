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
class WorkExperience(models.Model):
    company_name = models.CharField(max_length=200, verbose_name="Компания / Организация")
    position = models.CharField(max_length=200, verbose_name="Должность")
    period = models.CharField(max_length=100, verbose_name="Период работы (например, 2024 — 2026)")
    skills_and_achievements = models.TextField(verbose_name="Мои навыки и достижения")
    description = models.TextField(verbose_name="Описание работы и обязанности")
    bg_image = models.ImageField(upload_to='work_bg/', blank=True, null=True, verbose_name="Фоновое изображение страницы")
    page_number = models.PositiveIntegerField(default=1, verbose_name="Номер страницы в книге (1, 2, 3...)")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

    class Meta:
        verbose_name = "Этап работы (Страница)"
        verbose_name_plural = "Этапы работы (Книга)"
        ordering = ['page_number']

    def __str__(self):
        return f"Страница {self.page_number}: {self.position} в {self.company_name}"