from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    """Модель сообществ сайта"""

    title = models.CharField(
        verbose_name="Название сообщества", max_length=200)
    slug = models.SlugField(
        verbose_name="Адрес страницы сообщества", unique=True)
    description = models.TextField(
        max_length=500, blank=True, verbose_name="Описание сообщества"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Сообщество"
        verbose_name_plural = "Сообщества"


class Post(models.Model):
    """Модель публикации"""

    text = models.TextField(verbose_name="Текст публикации", max_length=200)
    pub_date = models.DateTimeField(
        verbose_name="Дата публикации", auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts",
        verbose_name="Автор публикации",
    )

    def __str__(self):
        return self.text

    group = models.ForeignKey(
        "Group",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="posts",
        verbose_name="Сообщество",
    )

    class Meta:
        ordering = ["-pub_date"]
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
