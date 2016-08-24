# coding=utf-8
from django.forms import ModelForm
from django.forms.extras import SelectDateWidget

from students.models import Student, Group


class StudentForm(ModelForm):
    action = '/student-add/'

    class Meta:
        model = Student
        fields = ['number', 'sex', 'surname', 'name', 'middle_name', 'birth_date', 'group']
        labels = {'number': 'Номер студенческого билета', 'sex': 'Пол', 'surname': 'Фамилия', 'name': 'Имя',
                  'middle_name': 'Отчество', 'birth_date': 'Дата рождения', 'group': 'Группа'}
        widgets = {'birth_date': SelectDateWidget()}
        help_texts = {}


class GroupForm(ModelForm):
    action = '/group-add/'

    class Meta:
        model = Group
        fields = ['name', 'speciality', 'year']
        labels = {'name': 'Наименование', 'speciality': 'Специальность', 'year': 'Год'}
        help_texts = {}
