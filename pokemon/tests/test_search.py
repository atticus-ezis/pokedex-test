from django.test import TestCase
from pokemon.models import Pokemon, Type
from django.urls import reverse 

class TestSearch(TestCase):
    def setUp(self):

        self.name_1 = "Fat Albert"
        self.name_2 = "Fatter Albert"

        self.type_1_name = 'water'
        self.type_2_name = 'fire'

        # create type and pokemon

        self.fire_type = Type.objects.create(name=self.type_1_name)
        self.water_type = Type.objects.create(name=self.type_2_name)

        Pokemon.objects.create(name=self.name_1, photo_url='https://img3.hulu.com/user/v3/artwork/7e22c7c5-9cc0-4969-a56f-dc8f6096f1a8?base_image_bucket_name=image_manager&base_image=c6de0e11-8185-4e8f-8526-94077f958fdf&size=458x687&format=webp').type.add(self.fire_type)
        Pokemon.objects.create(name=self.name_2, photo_url='https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/1.png').type.add(self.water_type)
        self.query = "Fatt"
        pass

    def test_search(self):
        response = self.client.get(reverse('pokemon_list_view'), {
            "pokemon_search":self.query
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual("pokemon_search=Fatt", response.request['QUERY_STRING'])

        expected_pokemon_list = Pokemon.objects.filter(name__istartswith='Fatt')
        pokemon_list = response.context['object_list']
        self.assertEqual(expected_pokemon_list[0], pokemon_list[0])
  
        


