import os
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from scraper.services import ScraperManager

class Command(BaseCommand):
    help = 'Scrape the news platforms'

    def handle(self, *args, **options):
        scraper_manager = ScraperManager()
        errors = scraper_manager.run_requests()

        if not settings.DEBUG and errors:
            message = Mail(
                from_email='support@newsify.com',
                to_emails=os.environ.get('DEVELOPERS_SUPPORT_EMAIL'),
                subject='Scrape got some errors',
                html_content=f'{errors}')
            try:
                sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
                sg.send(message)
            except Exception as error:
                print(str(error))

        self.stdout.write(self.style.ERROR(f'Scraping errors "{errors}"'))
