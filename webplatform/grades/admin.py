from django.contrib import admin

from .models import Student, Course, Semester, Grades

class GradeAdmin(admin.ModelAdmin):
    list_display = ('id', 'student_name', 'course_name', 'semester_name', 'grade')
    search_fields = ['student__name', 'course__name']
    list_filter = ('semester__name', )

    def student_name(self, object):
        return object.student.name
    def course_name(self, object):
        return object.course.name
    def semester_name(self, object):
        return object.semester.name

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Semester)
admin.site.register(Grades, GradeAdmin)
