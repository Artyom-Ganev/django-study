# coding: utf-8
from django.contrib import admin

from students.models import Department, Group, Student, Employee, Faculty, Speciality

admin.site.register(Employee)
admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Speciality)
admin.site.register(Group)
admin.site.register(Student)
