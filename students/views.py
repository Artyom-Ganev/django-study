# coding: utf-8
from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.template import loader

from students.forms import StudentForm, GroupForm
from students.models import Student, Group, Speciality, Faculty, Department

html = ".html"


def get_template(request, objects, name):
    template = loader.get_template(name + html)
    context = RequestContext(request, {name: objects})
    return template.render(context)


def get_template_with_detail(request, objects, name, detail, detail_name):
    template = loader.get_template(name + html)
    context = RequestContext(request, {name: objects, detail_name: detail})
    return template.render(context)


def index(request):
    return HttpResponse(get_template(request, None, "base"))


def faculties(request):
    objects = Faculty.objects.all()
    return HttpResponse(get_template(request, objects, "faculties"))


def faculty(request, fac_id):
    try:
        obj = Faculty.objects.get(id=fac_id)
    except Faculty.DoesNotExist:
        raise Http404
    detail = Department.objects.filter(faculty=fac_id)
    return HttpResponse(get_template_with_detail(request, obj, "faculty", detail, "departments"))


def departments(request):
    objects = Department.objects.all()
    return HttpResponse(get_template(request, objects, "departments"))


def department(request, dep_id):
    try:
        obj = Department.objects.get(id=dep_id)
    except Department.DoesNotExist:
        raise Http404
    detail = Speciality.objects.filter(department=dep_id)
    return HttpResponse(get_template_with_detail(request, obj, "department", detail, "specialities"))


def specialities(request):
    objects = Speciality.objects.all()
    return HttpResponse(get_template(request, objects, "specialities"))


def specialitiy(request, spec_id):
    try:
        obj = Speciality.objects.get(id=spec_id)
    except Speciality.DoesNotExist:
        raise Http404
    if request.user.is_authenticated():
        detail = Group.objects.filter(speciality=spec_id)
    else:
        detail = None
    return HttpResponse(get_template_with_detail(request, obj, "speciality", detail, "groups"))


def groups(request):
    if not request.user.is_authenticated():
        template = loader.get_template("login_error.html")
        return HttpResponse(template.render())
    objects = Group.objects.all()
    return HttpResponse(get_template(request, objects, "groups"))


def group(request, group_id):
    if not request.user.is_authenticated():
        template = loader.get_template("login_error.html")
        return HttpResponse(template.render())
    try:
        obj = Group.objects.get(id=group_id)
    except Group.DoesNotExist:
        raise Http404
    detail = Student.objects.filter(group=obj)
    return HttpResponse(get_template_with_detail(request, obj, "group", detail, "students"))


def group_add(request):
    if not request.user.is_authenticated():
        template = loader.get_template("login_error.html")
        return HttpResponse(template.render())
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/groups/')
    else:
        form = GroupForm()
    return render(request, 'add.html', {'form': form})


def group_delete(request, group_id):
    if not request.user.is_authenticated():
        template = loader.get_template("login_error.html")
        return HttpResponse(template.render())
    try:
        obj = Group.objects.get(id=group_id)
    except Student.DoesNotExist:
        raise Http404
    obj.delete()
    return HttpResponseRedirect('/groups/')


def group_edit(request, group_id):
    if not request.user.is_authenticated():
        template = loader.get_template("login_error.html")
        return HttpResponse(template.render())
    try:
        obj = Group.objects.get(id=group_id)
    except Student.DoesNotExist:
        raise Http404
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/groups/' + group_id)
    form = GroupForm(instance=obj)
    form.action = ''
    return render(request, 'add.html', {'form': form})


def students(request):
    if not request.user.is_authenticated():
        template = loader.get_template("login_error.html")
        return HttpResponse(template.render())
    objects = Student.objects.all()
    return HttpResponse(get_template(request, objects, "students"))


def student(request, student_number):
    if not request.user.is_authenticated():
        template = loader.get_template("login_error.html")
        return HttpResponse(template.render())
    try:
        obj = Student.objects.get(number=student_number)
    except Student.DoesNotExist:
        raise Http404
    return HttpResponse(get_template(request, obj, "student"))


def student_add(request):
    if not request.user.is_authenticated():
        template = loader.get_template("login_error.html")
        return HttpResponse(template.render())
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/students/')
    else:
        form = StudentForm()
    return render(request, 'add.html', {'form': form})


def student_delete(request, student_number):
    if not request.user.is_authenticated():
        template = loader.get_template("login_error.html")
        return HttpResponse(template.render())
    try:
        obj = Student.objects.get(number=student_number)
    except Student.DoesNotExist:
        raise Http404
    obj.delete()
    return HttpResponseRedirect('/students/')


def student_edit(request, student_number):
    if not request.user.is_authenticated():
        template = loader.get_template("login_error.html")
        return HttpResponse(template.render())
    try:
        obj = Student.objects.get(number=student_number)
    except Student.DoesNotExist:
        raise Http404
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/students/' + student_number)
    form = StudentForm(instance=obj)
    form.action = ''
    return render(request, 'add.html', {'form': form})
