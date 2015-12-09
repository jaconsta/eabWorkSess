from lettuce import *

from django.conf import settings
from django.apps import apps
from django.core.management.base import CommandError
from django.core.management import call_command
from django.test.runner import DiscoverRunner

def assert_test_database():
    """
    """
    if not '-test' in settings.DATABASES['default']['NAME']:
        raise CommandError('Harvest with test db')


@before.runserver
def create_database(server):
    """

    :param server:
    :return:
    """
    # assert_test_database()
    world.test_runner = DiscoverRunner(interactive=False)
    DiscoverRunner.setup_test_environment(world.test_runner)
    world.create_db = DiscoverRunner.setup_databases(world.test_runner)


@before.each_app
def set_app_name(app):
    world.app_name = app.__name__

# @world.absorb
@step(r'I have (.*) in the database')
def create_user(step, model_name):
    """
    Manual creation of the model
    Generic creation
    :param step:
    :param user:
    :return:
    """
    # Get app model
    try:
        Model = apps.get_model(world.app_name, model_name)
    except LookupError as e:
        assert False, 'Error loading model %s' % model_name
        return

    for row in step.hashes:
        db_row = Model(**row)
        db_row.save()


@after.runserver
def flush_database(server):
    """

    :param server:
    :return:
    """
    # assert_test_database()
    # call_command('flush', interactive=False, verbosity=0)
    pass
