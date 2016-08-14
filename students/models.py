# coding: utf-8
from django.db import models


class Named(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name


class Faculty(Named):
    class Meta:
        verbose_name = "Факультет"
        verbose_name_plural = "Факультеты"


class Group(Named):
    faculty = models.ForeignKey(Faculty)
    year = models.IntegerField

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"


class Student(models.Model):
    number = models.IntegerField(verbose_name=u'Номер студенческого билета', primary_key=True, db_index=True,
                                 null=False, blank=False, unique=True)
    group = models.ForeignKey(Group)
    surname = models.CharField(verbose_name=u'Фамилия', null=False, blank=False, max_length=50)
    name = models.CharField(verbose_name=u'Имя', null=False, blank=False, max_length=50)
    middle_name = models.CharField(verbose_name=u'Отчество', null=False, blank=False, max_length=50)
    birth_date = models.DateField(verbose_name=u'Дата рождения', null=False, blank=False)

    class Meta:
        ordering = ["surname", "name", "middle_name"]
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"
        unique_together = ("surname", "name", "middle_name")
