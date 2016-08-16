# coding: utf-8
from django.http import HttpResponse
from django.template import Context
from django.template import loader

from students.models import Student, Group, Speciality, Faculty, Department


def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())


def faculties(request):
    objects = Faculty.objects.all()
    template = loader.get_template("faculties.html")
    context = Context({"faculties": objects})
    return HttpResponse(template.render(context))


def faculty(request, fac_id):
    obj = Faculty.objects.get(id=fac_id)
    template = loader.get_template("faculty.html")
    context = Context({"faculty": obj})
    return HttpResponse(template.render(context))


def departments(request):
    objects = Department.objects.all()
    template = loader.get_template("departments.html")
    context = Context({"departments": objects})
    return HttpResponse(template.render(context))


def department(request, dep_id):
    obj = Department.objects.get(id=dep_id)
    template = loader.get_template("department.html")
    context = Context({"department": obj})
    return HttpResponse(template.render(context))


def specialities(request):
    objects = Speciality.objects.all()
    template = loader.get_template("specialities.html")
    context = Context({"specialities": objects})
    return HttpResponse(template.render(context))


def specialitiy(request, spec_id):
    obj = Speciality.objects.get(id=spec_id)
    template = loader.get_template("speciality.html")
    context = Context({"speciality": obj})
    return HttpResponse(template.render(context))


def groups(request):
    objects = Group.objects.all()
    template = loader.get_template("groups.html")
    context = Context({"groups": objects})
    return HttpResponse(template.render(context))


def group(request, group_id):
    obj = Group.objects.get(id=group_id)
    template = loader.get_template("group.html")
    context = Context({"group": obj})
    return HttpResponse(template.render(context))


def students(request):
    objects = Student.objects.all()
    template = loader.get_template("students.html")
    context = Context({"students": objects})
    return HttpResponse(template.render(context))


def student(request, student_number):
    obj = Student.objects.get(number=student_number)
    template = loader.get_template("student.html")
    context = Context({"student": obj})
    return HttpResponse(template.render(context))
