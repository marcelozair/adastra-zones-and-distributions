from django.core.management.base import BaseCommand

from zones.models import Zone, Distribution


class Command(BaseCommand):
    help = 'Command to fill remaining dates'

    def handle(self, *args, **options):
        self.create_zones('A', [50, 50])
        self.create_zones('B', [25, 25, 25, 25])
        self.create_zones('C', [30, 30, 40])
        self.create_zones('D', [15, 15, 5, 10, 55])

    def create_zones(self, name, percentages):
        zone = Zone.objects.create(name=name)

        for percentage in percentages:
            Distribution.objects.create(zone=zone, percentage=percentage)
