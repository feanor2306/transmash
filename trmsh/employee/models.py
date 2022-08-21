from django.db import models
from django.db.models import SET_NULL, PROTECT
from django.urls import reverse

import employee.models


class Skills(models.Model):
    LEVEL = (
        ("Отлично", "Отлично"),
        ("Хорошо", "Хорошо"),
        ("Удовлетворительно", "Удовлетворительно"),
        ("Неудовлетворительно", "Неудовлетворительно")
    )

    name = models.CharField(null=True, blank=True, max_length=20, verbose_name="Тип оборудования")
    grade = models.CharField(choices=LEVEL, null=True, blank=True, max_length=20, verbose_name='Уровень навыков')
    #skan = models.CharField(choices=LEVEL_SKILL, null=True, blank=True, max_length=20)
    #optic = models.CharField(choices=LEVEL_SKILL, null=True, blank=True, max_length=20)

    class Meta:
        verbose_name = 'Профессиональные навыки'
        verbose_name_plural = 'Профессиональные навыки'


class Branches(models.Model):

    branches = models.CharField(null=True, blank=True, max_length=50, verbose_name="Филиал")

    class Meta:
        verbose_name = 'Филиалы'
        verbose_name_plural = 'Филиалы'
        ordering = ['id']


class Personal(models.Model):
    PCYCHO = (
        (1, "Высокий уровень"),
        (2, "Средний уровень"),
        (3, "Низкий уровень"),

    )
    responsibility = models.CharField(choices=PCYCHO, null=True, blank=True, max_length=20, verbose_name="Ответственность")
    sociability = models.CharField(choices=PCYCHO, null=True, blank=True, max_length=20, verbose_name="Коммуникабельность")
    stress = models.CharField(choices=PCYCHO, null=True, blank=True, max_length=20, verbose_name="Стрессоустойчивость")
    conflict = models.CharField(choices=PCYCHO, null=True, blank=True, max_length=20, verbose_name="Конфликтность")

    class Meta:
        verbose_name = 'Личные качества'
        verbose_name_plural = 'Личные качества'




class Employee(models.Model):
    LEVEL_CATEGORY = (
        ("1", "1-я"),
        ("2", "2-я"),
        ("3", "3-я")
    )
    SENIORITY_LIST = (
        ("Инженер", "Инженер"),
        ("Стажер", "Стажер"),
    )
    name = models.CharField(max_length=255, verbose_name='Имя')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фото')
    seniority = models.CharField(choices=SENIORITY_LIST, max_length=20,  null=True, verbose_name='Должность')
    cat = models.CharField(choices=LEVEL_CATEGORY, max_length=10, null=True, verbose_name='Категория')
    explored_branches = models.ForeignKey(Branches, on_delete=models.PROTECT, null=True, verbose_name='Знакомые объекты')  # Выбираются все шахты, на которых сотрудник работал 2 недели и более
    favorite_branch = models.ForeignKey(Branches, related_name='favoritebranches', on_delete=models.PROTECT, null=True, verbose_name='Предпочитаемый объект')  # Выбирается одна шахта
    skills_level = models.ManyToManyField(Skills, verbose_name='Уровень навыков', null=True)
    personal_qualities = models.ForeignKey(Personal, on_delete=models.PROTECT, null=True, verbose_name='Личные качества')
    medical = models.TextField(blank=False, verbose_name='Мединформация', null=True)
    special = models.TextField(blank=False, verbose_name='Особые отметки', null=True)



    class Meta:
        verbose_name = 'Сотрудники'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})


from django.db import models

# Create your models here.
