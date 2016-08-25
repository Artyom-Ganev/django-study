from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    url(r'^faculties/$', views.faculties, name='faculties'),
    url(r'^faculties/(?P<fac_id>\d+)/$', views.faculty, name='faculty'),
    url(r'^departments/$', views.departments, name='departments'),
    url(r'^departments/(?P<dep_id>\d+)/$', views.department, name='department'),
    url(r'^specialities/$', views.specialities, name='specialities'),
    url(r'^specialities/(?P<spec_id>\d+)/$', views.specialitiy, name='speciality'),
    url(r'^groups/$', views.groups, name='groups'),
    url(r'^groups/(?P<group_id>\d+)/$', views.group, name='group'),
    url(r'^group-add/$', views.group_add, name='group-add'),
    url(r'^group-delete/(?P<group_id>\d+)/$', views.group_delete, name='group-delete'),
    url(r'^group-edit/(?P<group_id>\d+)/$', views.group_edit, name='group-edit'),
    url(r'^students/$', views.students, name='students'),
    url(r'^students/(?P<student_number>\d+)/$', views.student, name='student'),
    url(r'^student-add/$', views.student_add, name='student-add'),
    url(r'^student-delete/(?P<student_number>\d+)/$', views.student_delete, name='student-delete'),
    url(r'^student-edit/(?P<student_number>\d+)/$', views.student_edit, name='student-edit'),
]
