from django.core.management.base import BaseCommand
from pokemon.models import Pokemon, Type

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
                url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}/'
                response = requests.get(url)
                response.raise_for_status()
                data = response.json()

                # retrive data
                pokemon_name = data.get('name')
                pokemon_photo_url = data.get('sprites').get('front_default')

                # create pokemon
                created_new_pokemon, created = Pokemon.objects.get_or_create(name=pokemon_name, photo_url=pokemon_photo_url)

                # type
                pokemon_type_data = data.get('types')
                pokemon_types_list = [_dict['type']['name'] for _dict in pokemon_type_data]

                for pokemon_type in pokemon_types_list:
                    listed_type, _ = Type.objects.get_or_create(name=pokemon_type)
                    created_new_pokemon.type.add(listed_type)
                
                print(f"Success! Added {pokemon_name} to the database.", file=self.stdout)

            except requests.RequestException as e:
                print(f"Request failed for ID {pokemon_id}: {e}", file=self.stderr)
            except Exception as e:
                print(f"Error processing {pokemon_id}: {e}", file=self.stderr)

        print("Command executed successfully", file=self.stdout)