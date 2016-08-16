# coding: utf-8
from django.test import TestCase

from students.models import Faculty, Employee


class FacultyTest(TestCase):
    def test_unicode(self):
        faculty = Faculty(name="СЭФ")
        self.assertEquals(faculty.__unicode__(), "СЭФ")


class EmployeeTest(TestCase):
    def test_unicode(self):
        employee = Employee(surname="Иванов", name="Иван", middle_name="Иванович")
        self.assertEquals(employee.__unicode__(), "Иванов Иван Иванович")
