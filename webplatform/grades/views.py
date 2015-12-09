from django.shortcuts import render
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

from .models import Student, Course, Semester, Grades


def sum(numb):
    if len(numb) <= 1:
        return numb[0].grade
    else:
        return numb[0].grade + sum(numb[1:])


def averageGrade(request):
    semesterFrom = request.GET.get('from')
    semesterTo = request.GET.get('to')
    studentName = request.GET.get('student')

    # Find student
    try:
        student = Student.objects.get(name=studentName)
    except ObjectDoesNotExist:
        return JsonResponse({
            'status':400,
            'message': 'Student doesnt exists.'
            }, status=400)
    # Validate Semesters
    # From
    try:
        start = Semester.objects.get(name=semesterFrom).start_date
    except ObjectDoesNotExist:
        return JsonResponse({
            'status':400,
            'message': 'Start semester name doesnt exists.'
            }, status=400)
    # To
    try:
        end = Semester.objects.get(name=semesterTo).end_date
    except ObjectDoesNotExist:
        return JsonResponse({
            'status':400,
            'message': 'End semester name doesnt exists.'
            }, status=400)

    grades = Grades.objects.filter(student=student, semester__start_date__gte=start, semester__end_date__lte=end)

    if len(grades) < 1:
        return JsonResponse({
            'status':400,
            'message': 'Student has no grades.'
            }, status=400)

    averageGrade = sum(grades) / len(grades)
    return JsonResponse({
        'status': 200,
        'message': 'Got grade',
        'average_grade': averageGrade
        })
