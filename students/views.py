# coding: utf-8
from django.http import Http404
from django.http import HttpResponse
from django.template import Context
from django.template import loader

from students.models import Student, Group, Speciality, Faculty, Department

html = ".html"


def get_template(objects, name):
    template = loader.get_template(name + html)
    context = Context({name: objects})
    return template.render(context)


def get_template_with_detail(objects, name, detail, detail_name):
    template = loader.get_template(name + html)
    context = Context({name: objects, detail_name: detail})
    return template.render(context)


def index(request):
    template = loader.get_template("base.html")
    return HttpResponse(template.render())


def faculties(request):
    objects = Faculty.objects.all()
    return HttpResponse(get_template(objects, "faculties"))


def faculty(request, fac_id):
    try:
        obj = Faculty.objects.get(id=fac_id)
    except Faculty.DoesNotExist:
        raise Http404
    detail = Department.objects.filter(faculty=fac_id)
    return HttpResponse(get_template_with_detail(obj, "faculty", detail, "departments"))


def departments(request):
    objects = Department.objects.all()
    return HttpResponse(get_template(objects, "departments"))


def department(request, dep_id):
    try:
        obj = Department.objects.get(id=dep_id)
    except Department.DoesNotExist:
        raise Http404
    detail = Speciality.objects.filter(department=dep_id)
    return HttpResponse(get_template_with_detail(obj, "department", detail, "specialities"))


def specialities(request):
    objects = Speciality.objects.all()
    return HttpResponse(get_template(objects, "specialities"))


def specialitiy(request, spec_id):
    try:
        obj = Speciality.objects.get(id=spec_id)
    except Speciality.DoesNotExist:
        raise Http404
    if request.user.is_authenticated():
        detail = Group.objects.filter(speciality=spec_id)
    else:
        detail = None
    return HttpResponse(get_template_with_detail(obj, "speciality", detail, "groups"))


def groups(request):
    if not request.user.is_authenticated():
        template = loader.get_template("login_error.html")
        return HttpResponse(template.render())
    objects = Group.objects.all()
    return HttpResponse(get_template(objects, "groups"))


def group(request, group_id):
    if not request.user.is_authenticated():
        template = loader.get_template("login_error.html")
        return HttpResponse(template.render())
    try:
        obj = Group.objects.get(id=group_id)
    except Group.DoesNotExist:
        raise Http404
    detail = Student.objects.filter(group=obj)
    return HttpResponse(get_template_with_detail(obj, "group", detail, "students"))


def students(request):
    if not request.user.is_authenticated():
        template = loader.get_template("login_error.html")
        return HttpResponse(template.render())
    objects = Student.objects.all()
    return HttpResponse(get_template(objects, "students"))


def student(request, student_number):
    if not request.user.is_authenticated():
        template = loader.get_template("login_error.html")
        return HttpResponse(template.render())
    try:
        obj = Student.objects.get(number=student_number)
    except Student.DoesNotExist:
        raise Http404
    return HttpResponse(get_template(obj, "student"))
