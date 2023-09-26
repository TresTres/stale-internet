"""
This management command scrubs the database of all data. 

Example usage:
python manage.py scrub_database --dryrun False

"""

from django.core.management.base import BaseCommand, CommandError
from django.db import connection

from db_admin.utils.commands import CustomCommandMixin

class Command(BaseCommand, CustomCommandMixin):

    def add_arguments(self, parser):
        parser.add_argument(
            "--dryrun",
            type=bool,
            default=True,
            help="If True, no data will be deleted.",
        )

    def handle(self, *args, **options):
        
        if connection.settings_dict["USER"] != "test":
            raise CommandError("This command can only be run on the test database.")
        self.dryrun = options["dryrun"]
        self.print_msg(self.style("WARNING: This will delete all data in the database."))
        
        
        