from django.test import TestCase
from pokemon.models import Pokemon, Type
from django.urls import reverse

class MyTestCase(TestCase):
    def setUp(self):

        self.name_1 = "Fat Albert"
        self.name_2 = "Fatter Albert"

        self.type_1_name = 'water'
        self.type_2_name = 'fire'

        self.create_name = 'Skinny Albert'
        self.create_photo_url = 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/1.png'
        # create type and pokemon

        self.fire_type = Type.objects.create(name=self.type_1_name)
        self.water_type = Type.objects.create(name=self.type_2_name)

        Pokemon.objects.create(name=self.name_1, photo_url='https://img3.hulu.com/user/v3/artwork/7e22c7c5-9cc0-4969-a56f-dc8f6096f1a8?base_image_bucket_name=image_manager&base_image=c6de0e11-8185-4e8f-8526-94077f958fdf&size=458x687&format=webp').type.add(self.fire_type)
        Pokemon.objects.create(name=self.name_2, photo_url='https://img3.hulu.com/user/v3/artwork/7e22c7c5-9cc0-4969-a56f-dc8f6096f1a8?base_image_bucket_name=image_manager&base_image=c6de0e11-8185-4e8f-8526-94077f958fdf&size=458x687&format=webp').type.add(self.water_type)
        pass

    def test_display(self):

        # does view display all objects?

        response = self.client.get(reverse('pokemon_list_view'))

        self.assertEqual(response.status_code, 200)
        self.assertIn('pokemon_list', response.context)

        pokemon_list = response.context['pokemon_list']
        self.assertEqual(len(pokemon_list), 2)

        names = [pokemon.name for pokemon in pokemon_list]
        self.assertIn(self.name_1, names)
        self.assertIn(self.name_2, names)

        types = [type.name for type in Type.objects.all()]
        self.assertIn(self.type_1_name, types)
        self.assertIn(self.type_2_name, types)

    def test_detail(self):

        response = self.client.get(reverse('pokemon_detail', kwargs={'pk':1}))
        self.assertEqual(response.status_code, 200)

        pokemon_displayed = response.context['pokemon']
        expected_pokemon = Pokemon.objects.get(pk=1)
        self.assertEqual(pokemon_displayed.pk, expected_pokemon.pk)

    def test_update(self):
        
        response = self.client.post(reverse('update_pokemon', kwargs={'pk':1}), {
            "name":self.create_name,
            "type":[self.water_type.pk],
            "photo_url":self.create_photo_url
        })

        self.assertEqual(response.status_code, 302)

        updated_object = Pokemon.objects.get(pk=1)
        self.assertEqual(updated_object.name, self.create_name)

    def test_create(self):

        response = self.client.post(reverse('create_pokemon'), {
            "name":self.create_name,
            "type":[self.water_type.pk],
            "photo_url":self.create_photo_url

        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Pokemon.objects.count(), 3)

    def test_delete(self):
        
        response = self.client.post(reverse('delete_pokemon', kwargs={"pk":1}))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Pokemon.objects.count(),1)




        



        


