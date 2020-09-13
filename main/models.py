from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=255, verbose_name='Ten sach')
    author = models.CharField(max_length=255, verbose_name='Tac gia')
    publisher = models.CharField(max_length=255, verbose_name='Nha xuat ban', null=True)
    year = models.IntegerField(verbose_name='Nam xuat ban', null=True)
    cost = models.IntegerField(verbose_name='Gia')

    def __str__(self):
        return self.name + '---' + self.author
    