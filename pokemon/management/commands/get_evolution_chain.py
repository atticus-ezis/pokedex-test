from django.core.management.base import BaseCommand
from pokemon.models import Pokemon, Type, EvolutionChain

import requests

class Command(BaseCommand):
    help = "Adds Pokemon"

    def add_arguments(self, parser):
        # Optional: add custom arguments
        parser.add_argument('start_id', type=int)
        parser.add_argument('end_id', type=int)
        pass

    def handle(self, *args, **options):
        for pokemon_id in range(options['start_id'], options['end_id']+1):
            try:
                url = f'https://pokeapi.co/api/v2/pokemon-species/{pokemon_id}'
                response = requests.get(url)
                response.raise_for_status()
                data = response.json()

                evolves_from = data.get('evolves_from_species').get('name')

                if evolves_from is None:
                    first_evolution = True 




            except requests.RequestException as e:
                print(f"Request failed for ID {pokemon_id}: {e}", file=self.stderr)
            except Exception as e:
                print(f"Error processing {pokemon_id}: {e}", file=self.stderr)