from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pokemon.models import Pokemon, Type
from pokemon.forms import SearchForm
from django.contrib.auth.mixins import LoginRequiredMixin

class PokemonListView(ListView):
    queryset = Pokemon.objects.all().order_by('pk')
    paginate_by = 20 

    # render search form 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = SearchForm(self.request.GET or None)
        return context

    # triggered after GET request
    def get_queryset(self):
        queryset = super().get_queryset()
        form = SearchForm(self.request.GET)
        if form.is_valid():
            name_query = form.cleaned_data['pokemon_name']
            type_query = form.cleaned_data['pokemon_types']

            if name_query:
                queryset = queryset.filter(name__istartswith=name_query)
                
            if type_query:
                queryset = queryset.filter(type__name__icontains=type_query)

        return queryset


class PokemonDetailView(DetailView):
    model = Pokemon

class PokemonCreateView(LoginRequiredMixin, CreateView):
    model = Pokemon
    fields = ['name', 'type', 'photo_url', 'evolution_chain']
    success_url = reverse_lazy('pokemon_list_view')
    # default to pokemon_form.html

class PokemonUpdateView(LoginRequiredMixin, UpdateView):
    model = Pokemon
    fields = ['name', 'type', 'photo_url', 'evolution_chain']
    success_url = reverse_lazy('pokemon_list_view')
    # default to pokemon_form.html

class PokemonDeleteView(LoginRequiredMixin, DeleteView):
    model = Pokemon
    success_url = reverse_lazy('pokemon_list_view')
    
    



