from django.core.management.base import BaseCommand

from tenant_only.models import TableTwo


class Command(BaseCommand):
    help = 'Test table two'

    def add_arguments(self, parser):
        parser.add_argument('--id', nargs='+', type=int)

    def handle(self, *args, **options):
        print(options['id'])
        table_two = TableTwo.objects.filter(pk__in=options['id'])
        print(table_two)

# 使用方法
# python3 manage.py tenant_command dtest --id 1 --schema=tenant1
# python3 manage.py tenant_command dtest --id 1 --schema=tenant2
