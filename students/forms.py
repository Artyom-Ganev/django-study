# coding=utf-8
from django.forms import ModelForm
from django.forms.extras import SelectDateWidget

from students.models import Student, Group


# noinspection PyMethodOverriding
class StudentForm(ModelForm):
    action = '/student-add/'

    class Meta:
        model = Student
        fields = '__all__'
        labels = {'number': 'Номер студенческого билета', 'sex': 'Пол', 'surname': 'Фамилия', 'name': 'Имя',
                  'middle_name': 'Отчество', 'birth_date': 'Дата рождения', 'group': 'Группа'}
        widgets = {'birth_date': SelectDateWidget()}
        help_texts = {}

    def save(self, username):
        obj = super(StudentForm, self).save(commit=False)
        obj.username = username
        return obj.save()


# noinspection PyMethodOverriding
class GroupForm(ModelForm):
    action = '/group-add/'

    class Meta:
        model = Group
        fields = '__all__'
        labels = {'name': 'Наименование', 'speciality': 'Специальность', 'year': 'Год'}
        help_texts = {}

    def save(self, username):
        obj = super(GroupForm, self).save(commit=False)
        obj.username = username
        return obj.save()
