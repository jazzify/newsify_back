from django.core.management.base import BaseCommand, CommandError
from scraper.services import ScraperManager

class Command(BaseCommand):
    help = 'Scrape the news platforms'

    def handle(self, *args, **options):
        scraper_manager = ScraperManager()
        errors = scraper_manager.run_requests()

        self.stdout.write(self.style.ERROR(f'Scraping errors "{errors}"'))
