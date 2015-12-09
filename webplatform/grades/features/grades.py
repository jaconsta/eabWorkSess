from lettuce import *
from lettuce.django import django_url
from django.test.client import Client

from django.conf import settings
from django.core.management.base import CommandError
from django.core.management import call_command

import json


def load_fixture(fixture_name):
    call_command('loaddata', fixture_name, interactive=False, verbosity=0)

@before.all
def set_browser():
    world.browser = Client()
    for fixture in ['students', 'semesters', 'courses', 'grades']:
        load_fixture(fixture)



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
