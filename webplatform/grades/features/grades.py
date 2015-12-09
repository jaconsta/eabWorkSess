import json

from lettuce import *
from lettuce.django import django_url

from django.test.client import Client
from django.apps import apps
from django.conf import settings
from django.core.management.base import CommandError
from django.core.management import call_command


def load_fixture(fixture_name):
    call_command('loaddata', fixture_name, interactive=False, verbosity=0)

@before.all
def set_browser():
    world.browser = Client()
    for fixture in ['students', 'semesters', 'courses', 'grades']:
        load_fixture(fixture)


@step(r'This (.*) (.*) has this (.*) in the database')
def set_grades(step, user_model, user_name, grade_model):
    """
    Manual creation of the model
    Custom creation
    :param step:
    :param user_model:
    :param user_name:
    :param grade_model:
    :return:
    """
    # Get app model
    try:
        Model = apps.get_model(world.app_name, grade_model)
    except LookupError as e:
        assert False, 'Error loading model %s' % grade_model
        return

    for row in step.hashes:
        student = apps.get_model(world.app_name, 'student').objects.get(name=user_name)
        semester = apps.get_model(world.app_name, 'semester').objects.get(name=row['semester'])
        course = apps.get_model(world.app_name, 'course').objects.get(name=row['course'])

        grade = Model(student=student, semester=semester, course=course, grade=row['grade'] )
        grade.save()


@step(r'I access the url "(.*)"')
def access_url(step, url):
    full_url = django_url(url)
    response = world.browser.get(full_url)
    world.status_code = response.status_code
    world.res = response.content


@step(r'I expect response status (\d+)')
def see_status(step, status):
    assert world.status_code == int(status), \
        "Got %d" % world.status_code


@step(r'I expect content "(.*)"')
def see_content(step, content):
    response = json.loads(world.res)
    message = response['message']
    assert message == content, \
        "Got %s" % message


@step(r'I expect the average grade ([-+]?\d*\.\d+|\d+)')
def see_status(step, grade):
    response = json.loads(world.res)
    response_grade = float(response['average_grade'])

    assert response_grade == float(grade), \
        "Got %d" % response_grade
