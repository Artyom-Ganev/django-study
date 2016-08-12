from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Student(models.Model):
    group = models.ForeignKey(Group)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birth_date = models.DateTimeField('birth date')

    def __unicode__(self):
        return self.name
