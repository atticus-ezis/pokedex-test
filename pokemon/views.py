from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pokemon.models import Pokemon
from pokemon.forms import SearchForm


class PokemonListView(ListView):
    queryset = Pokemon.objects.all().order_by('pk')
    paginate_by = 20 
    
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('pokemon_search')
        if query:
            return queryset.filter(name__istartswith=query)
        return queryset

class PokemonDetailView(DetailView):
    model = Pokemon

class PokemonCreateView(CreateView):
    model = Pokemon
    fields = ['name', 'type', 'photo_url']
    success_url = reverse_lazy('pokemon_list_view')

class PokemonUpdateView(UpdateView):
    model = Pokemon
    fields = ['name', 'type', 'photo_url']
    success_url = reverse_lazy('pokemon_list_view')

class PokemonDeleteView(DeleteView):
    model = Pokemon
    success_url = reverse_lazy('pokemon_list_view')
    
    



