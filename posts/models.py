from django.db import models
from django.conf import settings
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'


class Post(models.Model):
    title = models.CharField(max_length=255)
    # conteúdo armazenado como código HTML (renderizado com o filtro safe)
    content = models.TextField()
    # data de postagem: preenchida com o momento da criação
    date = models.DateTimeField(default=timezone.now)
    # um post pode estar em várias categorias (relacionamento N para N)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'"{self.text}" - {self.author.username}'
