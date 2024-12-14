from django.core.management.base import BaseCommand
from ClientDiary.settings import mongo_db

class Command(BaseCommand):
    help = 'Check MongoDB connection'

    def handle(self, *args, **kwargs):
        try:
            print(mongo_db)
            # Attempt to list collections to check the connection
            collections = mongo_db.list_collection_names()
            self.stdout.write(self.style.SUCCESS('Successfully connected to MongoDB'))
            self.stdout.write(self.style.SUCCESS(f'Collections: {collections}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error connecting to MongoDB: {e}'))