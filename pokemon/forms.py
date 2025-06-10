from django import forms
from pokemon.models import Type


class SearchForm(forms.Form):
    pokemon_name = forms.CharField(max_length=100, required=False)
    pokemon_types = forms.ModelChoiceField(required=False,
                                           queryset=Type.objects.all().order_by('name'),
                                           label="Type",
                                           empty_label="All Types")