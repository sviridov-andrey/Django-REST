from django.db import models

from users.utils import NULLABLE


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='название курса')
    prevew = models.ImageField(upload_to='education/', verbose_name='превью', **NULLABLE)
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f' {self.name}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Leson(models.Model):
    name = models.CharField(max_length=100, verbose_name='название урока')
    prevew = models.ImageField(upload_to='education/', verbose_name='превью', **NULLABLE)
    description = models.TextField(verbose_name='описание')
    video = models.URLField(verbose_name='ссылка на видео', **NULLABLE)
    сourse = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f' {self.name}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
