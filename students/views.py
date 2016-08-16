# coding: utf-8
from django.http import HttpResponse
from django.template import Context
from django.template import loader

from students.models import Student, Group


def groups(request):
    objects = Group.objects.all()
    template = loader.get_template("groups.html")
    context = Context({"groups": objects})
    return HttpResponse(template.render(context))


def students(request):
    objects = Student.objects.all()
    template = loader.get_template("students.html")
    context = Context({"students": objects})
    return HttpResponse(template.render(context))
