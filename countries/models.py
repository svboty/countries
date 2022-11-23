from django.db import models


class Country(models.Model):
    name = models.CharField('Название', max_length=250)
    languages = models.ManyToManyField('countries.Language', related_name='countries')

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class Language(models.Model):
    label = models.CharField('Наименование', max_length=250)

    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'
