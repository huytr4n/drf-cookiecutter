from django.core.management.base import BaseCommand
from . import log
from drf_core.sampling import Sampling
from drf_core import factories


class Command(BaseCommand):
    """
    Run loadtestdata command.
    """

    help = 'Init data for the app'

    def handle(self, *args, **options):
        log.info('::init_data::')

        sampling = Sampling()
        sampling.generate_all()
