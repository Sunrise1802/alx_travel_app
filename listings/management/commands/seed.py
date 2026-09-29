from django.core.management.base import BaseCommand
from listings.models import Listing


class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        Listing.objects.create(
            title='Modern Apartment',
            description='A comfortable apartment in the city.',
            location='Lusaka',
            price=500.00,
            bedrooms=2,
            bathrooms=1
        )

        Listing.objects.create(
            title='Luxury House',
            description='A spacious house suitable for families.',
            location='Kitwe',
            price=1200.00,
            bedrooms=4,
            bathrooms=3
        )

        self.stdout.write(
            self.style.SUCCESS('Sample listings created successfully!')
        )