# coding: utf-8
from django.db import models


class UserInfo(models.Model):
    username = models.CharField(max_length=100, null=False, blank=False, editable=False)

    class Meta:
        abstract = True


class Named(UserInfo):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name


class Human(UserInfo):
    SEX_CHOICES = (
        ('m', u"мужской"),
        ('w', u"женский"),
    )
    sex = models.CharField(max_length=1, verbose_name=u"Пол", choices=SEX_CHOICES)
    surname = models.CharField(verbose_name=u'Фамилия', null=False, blank=False, max_length=50)
    name = models.CharField(verbose_name=u'Имя', null=False, blank=False, max_length=50)
    middle_name = models.CharField(verbose_name=u'Отчество', null=False, blank=False, max_length=50)
    birth_date = models.DateField(verbose_name=u'Дата рождения', null=False, blank=False)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.surname + ' ' + self.name + ' ' + self.middle_name


class Employee(Human):
    fired = models.BooleanField(default=False)
    employment_date = models.DateField(verbose_name=u'Дата приёма на работу')
    fire_date = models.DateField(verbose_name=u'Дата увольнения', null=True, blank=True)

    class Meta:
        db_table = "employee"
        ordering = ["surname", "name", "middle_name"]
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
        unique_together = ("surname", "name", "middle_name")


class Faculty(Named):
    dean = models.OneToOneField(Employee)

    class Meta:
        db_table = "faculty"
        ordering = ["name", ]
        verbose_name = "Факультет"
        verbose_name_plural = "Факультеты"


class Department(Named):
    faculty = models.ForeignKey(Faculty)
    head = models.OneToOneField(Employee)

    class Meta:
        db_table = "department"
        ordering = ["name", ]
        verbose_name = "Кафедра"
        verbose_name_plural = "Кафедры"


class Speciality(Named):
    code = models.IntegerField(verbose_name=u'Код специальности', null=False, blank=False)
    department = models.ForeignKey(Department)

    class Meta:
        db_table = "speciality"
        ordering = ["code", ]
        verbose_name = "Специальность"
        verbose_name_plural = "Специальности"


class Group(Named):
    speciality = models.ForeignKey(Speciality)
    year = models.PositiveSmallIntegerField(verbose_name=u'Год создания', db_index=True)

    class Meta:
        db_table = "group"
        ordering = ["name", ]
        verbose_name = "Группа"
        verbose_name_plural = "Группы"


class Student(Human):
    number = models.IntegerField(verbose_name=u'Номер студенческого билета', primary_key=True, db_index=True,
                                 null=False, blank=False, unique=True)
    group = models.ForeignKey(Group, null=True, blank=False)

    class Meta:
        db_table = "student"
        ordering = ["group", "surname", "name", "middle_name"]
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"
        unique_together = ("surname", "name", "middle_name")
