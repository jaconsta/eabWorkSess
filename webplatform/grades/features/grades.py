from lettuce import *
from lettuce.django import django_url
from django.test.client import Client

from django.conf import settings
from django.core.management.base import CommandError
from django.core.management import call_command

import json

@before.all
def set_browser():
    world.browser = Client()
    call_command('loaddata', 'students', interactive=False, verbosity=0)

def load_fixture(step, fixture_name):
    call_command('loaddata', 'students', interactive=False, verbosity=0)

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
