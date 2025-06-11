from django.core.management.base import BaseCommand
from pokemon.models import Pokemon, Type
import requests
import time
from django.core.exceptions import ObjectDoesNotExist

class Command(BaseCommand):
    help = "Adds Evoltion Chain to Pokemon"

    def add_arguments(self, parser):
        # Optional: add custom arguments
        parser.add_argument('start_id', type=int)
        parser.add_argument('end_id', type=int)
        pass

    def handle(self, *args, **options):

        evolution_list_dict = {}
        
        for pokemon_id in range(options['start_id'], options['end_id']+1):
            try:
                url = f'https://pokeapi.co/api/v2/pokemon-species/{pokemon_id}'
                response = requests.get(url)
                response.raise_for_status()
                data = response.json()

                evolution_chain_url = data.get('evolution_chain').get('url')

                def get_chain(chain):
                    names = []

                    species_name = chain['species']['name']
                    if species_name:
                        try:
                            name = chain['species']['name']
                            pokemon = Pokemon.objects.get(name=name)
                            names.append(pokemon)
                        except ObjectDoesNotExist:
                            print(f"Pokemon '{species_name}' not found in DB.")
                            return names

                    if chain['evolves_to']:
                        time.sleep(1)
                        next_chain = chain['evolves_to'][0]
                        names.extend(get_chain(next_chain))

                    return names

                if evolution_chain_url not in evolution_list_dict:
              
                    chain_response = requests.get(evolution_chain_url)
                    chain_data = chain_response.json()

                    chain = chain_data.get('chain') 
                    
                    result = get_chain(chain)

                    evolution_list_dict[evolution_chain_url] = result
                
                current_pokemon_name = data.get('name')
                current_pokemon = Pokemon.objects.get(name=current_pokemon_name)

                chain_to_assign = evolution_list_dict[evolution_chain_url]

                if set(current_pokemon.evolution_chain.all()) != set(chain_to_assign):
                    current_pokemon.evolution_chain.set(chain_to_assign)
                    print(f'made change to {current_pokemon}: {current_pokemon.pk}')
                else:
                    print(f"no update needed for {current_pokemon}")

            except requests.RequestException as e:
                print(f"Request failed for ID {pokemon_id}: {e}", file=self.stderr)
            except Exception as e:
                print(f"Error processing {pokemon_id}: {e}", file=self.stderr)