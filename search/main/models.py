from django.db import models


class text_language(models.Model):
    text = models.TextField('Текст')
    language = models.CharField('Язык', max_length=34)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'текст'
        verbose_name_plural = 'тексты'
# Create your models here.
