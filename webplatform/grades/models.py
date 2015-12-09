from __future__ import unicode_literals

from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return 'Student name: %s.' % self.name

    #class Meta:
    #    verbose_name = 'student'


class Course(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return 'Course name: %s.' % self.name


class Semester(models.Model):
    name = models.CharField(max_length=250)
    start_date = models.DateField()
    end_date =models.DateField()

    def __str__(self):
        return 'Semester %s: From %s to %s' % (self.name, self.start_date, self.end_date)


class Grades(models.Model):
    student = models.ForeignKey('Student')
    course = models.ForeignKey('Course')
    semester = models.ForeignKey('Semester')
    grade = models.FloatField()

    def __str__(self):
        return 'Student %s in course %s got a grade %s for semester %s' % \
             (self.student.name, self.course.name, self.grade, self.semester.name)
