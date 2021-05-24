from django.db import models

# Create your models here.
class ItemTag(models.Model): # for add tag to our article
    tag = models.CharField("Tag", max_length= 50)

    def __str__(self):
        return self.tag
    
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

class Articles(models.Model):
    title = models.CharField('Назва', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публ')
    tag = models.ManyToManyField(ItemTag, verbose_name='Тег')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новина'
        verbose_name_plural = 'Новини'