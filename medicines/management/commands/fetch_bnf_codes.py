from django.core.management.base import BaseCommand
from medicines.models import Medicine
import requests

class Command(BaseCommand):
    help = 'Fetches BNF medicine data from API and store them in PostgreSQL.'

    def handle(self, *args, **kwargs):
       url = "https://openprescribing.net/api/1.0/bnf_code/" 

       response = requests.get(url)
       print(response.status_code)
       print(response.json())
       print(response.text)  # raw text response

       if response.status_code == 200:
           data = response.json()
           for item in data:
               Medicine.objects.update_or_create( 
                   bnf_code=item.get("bnf_code", ""),
                   defaults={
                       "name": item.get("name", "Unknown")
                   }
               ) # this inserts or creates records into PostgreSQL database
           self.stdout.write(self.style.SUCCESS("Medicine data imported successfully."))
       else:
           self.stderr.write("Failed to fetch data from API")

