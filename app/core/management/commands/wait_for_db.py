"""
Django command to wait for database to be avaliable
"""
from psycopg2 import OperationalError as Psycop2gError
from django.core.management.base import BaseCommand
import time
from django.db.utils import OperationalError


class Command(BaseCommand):
    """Django command to wait for db"""

    def handle(self, *args, **options):
        """Entrypoint for command"""

        self.stdout.write('Waiting for database....')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except(Psycop2gError, OperationalError):
                self.stdout.write("Database unavaliable, waiting 1 second....")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database avaliable"))
