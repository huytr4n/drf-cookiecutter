from django.core.management.base import BaseCommand

from . import log


class Command(BaseCommand):
    """
    Run loadtestdata command.
    """

    help = 'Init data for the app'

    def handle(self, *args, **options):
        log.info('::init_data::')
