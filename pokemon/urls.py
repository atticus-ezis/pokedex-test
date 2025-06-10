from django.urls import path
from pokemon import views 

urlpatterns = [
    path('', views.PokemonListView.as_view(), name="pokemon_list_view"),
    path('<int:pk>/', views.PokemonDetailView.as_view(), name="pokemon_detail"),
    path('create/', views.PokemonCreateView.as_view(), name="create_pokemon"),
    path('update/<int:pk>/', views.PokemonUpdateView.as_view(), name='update_pokemon'),
    path('delete/<int:pk>/', views.PokemonDeleteView.as_view(), name="delete_pokemon"),
]
