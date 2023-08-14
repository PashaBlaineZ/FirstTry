from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.CharField('Название', max_length=50)
    author = models.CharField('Автор', max_length=20)
    year = models.CharField('Год', max_length=4)
    amount =models.CharField('Количество', max_length=5)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'