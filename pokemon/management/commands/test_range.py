from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "test range function"

    def add_arguments(self, parser):
        # Optional: add custom arguments
        parser.add_argument('start_id', type=int)
        parser.add_argument('end_id', type=int)
        pass

    def handle(self, *args, **options):
        for sample in range(options['start_id'], options['end_id']+1):
            print(f'{sample}', file=self.stdout)