from django.core.management.base import BaseCommand, CommandError
from accounts.models import CustomUser
from listings.models import Listing
from news.models import BlogPost
from listings.factories import UserFactory, ListingFactory, BlogPostFactory

class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Import started')
        
        print('deleting old data')
        Listing.objects.all().delete()
        CustomUser.objects.all().delete()
        BlogPost.objects.all().delete()

        if not CustomUser.objects.filter(username='admin').exists():
            CustomUser.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='admin',
                phone='095 3234 142'
            )
        print('admin user creted')
        
        UserFactory.create_batch(size=30)
        print('Fake users created')
        ListingFactory.create_batch(size=50)
        print('Listings created')
        BlogPostFactory.create_batch(size=20)
        print('Blog posts created')
