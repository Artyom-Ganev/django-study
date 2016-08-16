# coding: utf-8
from django.contrib import admin

from students.models import Department, Group, Student, Employee, Faculty, Speciality


class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'year', 'name', 'speciality')


admin.site.register(Employee)
admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Speciality)
admin.site.register(Group, GroupAdmin)
admin.site.register(Student)
