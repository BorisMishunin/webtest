from django.db import models
# Create your models here.



class Author(models.Model):
    name = models.CharField('Название', max_length=150)

class Book(models.Model):
    name = models.CharField('Название',max_length=150)
    author = models.ManyToManyField(Author, verbose_name="Автор")