from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from pokemon.models import Pokemon

class MyTestCase(TestCase):
    def setUp(self):
        self.username = 'JohnnyPotato'
        self.first_name = 'Johnny'
        self.last_name = 'Potato'
        self.email = 'johnny.potato@gmail.com'
        self.password = 'Pandas098'

        self.pokemon_1 = Pokemon.objects.create(name="bulbasaur")


        pass

    def test_register_and_login_logout(self):
        register_response = self.client.post(reverse('register'), {
            "first_name":self.first_name,
            "last_name":self.last_name,
            "email":self.email,
            "username":self.username,
            "password1":self.password, 
            "password2":self.password,

        })
        self.assertEqual(register_response.status_code, 302)

        user = User.objects.get(username=self.username)

        self.assertIsInstance(user, User)

        # logout 
        logout_response = self.client.post(reverse('logout'))

        self.assertEqual(logout_response.status_code, 302)

        follow_response = self.client.get('/', follow=True)
        self.assertFalse(follow_response.wsgi_request.user.is_authenticated)

        # login
        login_response = self.client.post(reverse('login'), {
            "username":self.username,
            "password":self.password
        })

        self.assertEqual(login_response.status_code, 302)

        self.assertTrue(login_response.wsgi_request.user.is_authenticated)


    def test_user_permissions(self):

        delete_response = self.client.post(reverse('delete_pokemon', kwargs={'pk':1}))

        self.assertEqual(delete_response.status_code, 302)

        pokemon_query = Pokemon.objects.filter(pk=1).exists()

        self.assertTrue(pokemon_query)

        # login user 
        register_response = self.client.post(reverse('register'), {
            "first_name":self.first_name,
            "last_name":self.last_name,
            "email":self.email,
            "username":self.username,
            "password1":self.password, 
            "password2":self.password,

        })

        login_delete_response = self.client.post(reverse('delete_pokemon', kwargs={'pk':1}))

        login_pokemon_query = Pokemon.objects.filter(pk=1).exists()

        self.assertFalse(login_pokemon_query)



  