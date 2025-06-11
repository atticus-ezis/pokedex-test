from django.test import TestCase
from django.core.management import call_command
from io import StringIO

from pokemon.models import Pokemon, Type

# Create your tests here.

class TestCreatePokemonCommand(TestCase):
    def setUp(self):

        self.pokemon_1_a = Pokemon.objects.create(name="bulbasaur")
        self.pokemon_1_b = Pokemon.objects.create(name="ivysaur")
        self.pokemon_1_c = Pokemon.objects.create(name="venusaur")

        self.pokemon_2_a = Pokemon.objects.create(name="charmander")
        self.pokemon_2_b = Pokemon.objects.create(name="charmeleon")
        self.pokemon_2_c = Pokemon.objects.create(name="charizard")
      
        pass

    def test_create__chain_command(self):
     
        # create all 151 pokemon with the command
        call_command('get_evolution_chain', '1', '6')

        print(self.pokemon_1_a.evolution_chain)

        expected_chain_1 = [self.pokemon_1_a, self.pokemon_1_b, self.pokemon_1_c]
        expected_chain_2 = [self.pokemon_2_a, self.pokemon_2_b, self.pokemon_2_c]

        created_chain_1_a = list(self.pokemon_1_a.evolution_chain.all())
        created_chain_1_c = list(self.pokemon_1_c.evolution_chain.all())

        breakpoint()

        self.assertEqual(expected_chain_1, created_chain_1_a)
        self.assertEqual(expected_chain_1, created_chain_1_c)

        created_chain_2_a = list(self.pokemon_2_a.evolution_chain.all())
        created_chain_2_c = list(self.pokemon_2_c.evolution_chain.all())

        self.assertEqual(expected_chain_2, created_chain_2_a)
        self.assertEqual(expected_chain_2, created_chain_2_c)
