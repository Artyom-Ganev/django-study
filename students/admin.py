# coding: utf-8
from django.contrib import admin

from students.models import Faculty, Group, Student

admin.site.register(Faculty)
admin.site.register(Group)
admin.site.register(Student)
