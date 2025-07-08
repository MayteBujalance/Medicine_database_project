from django.core.management.base import BaseCommand
from medicines.models import Medicine
import requests


class Command(BaseCommand):
    help = 'Fetches BNF medicine data from API and store them in PostgreSQL.'

    def handle(self, *args, **kwargs):
        url = "https://openprescribing.net/api/1.0/bnf_code/?format=json"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            if not isinstance(data, list):
                self.stderr.write("Unexpected data format received from API.")
                return
            for item in data:
                Medicine.objects.update_or_create(
                    bnf_code=item.get("bnf_code", ""),
                    defaults={
                        "name": item.get("name", "Unknown")
                    }
                )  # this inserts or creates records into PostgreSQL database
            self.stdout.write(
                self.style.SUCCESS(
                    "Medicine data imported successfully."
                )
            )
        except requests.RequestException as e:
            self.stderr.write(f"Failed to fetch data from API: {e}")
        except Exception as e:
            self.stderr.write(f"An error occurred: {e}")
