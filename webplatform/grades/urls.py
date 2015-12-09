from django.conf.urls import url

from . import views

urlpatterns = [
    # /students/
    url(r'^averagegrade/$', views.averageGrade, name='studentsGrade'),
]