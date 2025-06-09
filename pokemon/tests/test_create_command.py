from django.test import TestCase
from django.core.management import call_command
from io import StringIO

from pokemon.models import Pokemon, Type

# Create your tests here.

class TestCreatePokemonCommand(TestCase):
    def setUp(self):

        # expected values for 1st created
        self.name = 'bulbasaur'
        self.photo_url = 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png'
        self.first_type_name = 'grass'
        self.second_type_name = 'poison'

        # expected values for 151st created
        self.name_151 = 'mew'
        self.photo_url_151 = 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/151.png'
        self.first_type_name_151 = 'psychic'
      
        pass

    def test_add_pokemon_command(self):
     
        # create all 151 pokemon with the command
        out = StringIO()
        call_command('add_pokemon', '1', '151', stdout=out)

        # types exist?
        first_type = Type.objects.get(name=self.first_type_name)
        second_type = Type.objects.get(name=self.second_type_name)

        type_151 = Type.objects.get(name=self.first_type_name_151)

        # 1st pokemon search
        bulbasour = Pokemon.objects.filter(
            name=self.name, 
            photo_url=self.photo_url
            ).filter(type=first_type).filter(type=second_type)
        
        # 151st pokemon search
        mew = Pokemon.objects.filter(
            name=self.name_151, 
            photo_url=self.photo_url_151
            ).filter(type=type_151)

        # pokemon exist?
        self.assertTrue(bulbasour.exists())
        self.assertTrue(mew.exists())

        # types exist?
        self.assertTrue(Type.objects.filter(name=first_type).exists())
        self.assertTrue(Type.objects.filter(name=second_type).exists())
        self.assertTrue(Type.objects.filter(name=type_151))
        
        # all 151 objects created?
        total_objects = Pokemon.objects.count()
        self.assertEqual(total_objects, 151)

        # check for success message
        output = out.getvalue()
        self.assertIn('Command executed successfully', output)