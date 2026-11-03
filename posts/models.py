from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=255)
    # conteúdo armazenado como código HTML (renderizado com o filtro safe)
    content = models.TextField()
    # data de postagem: preenchida com o momento da criação
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.title}'
