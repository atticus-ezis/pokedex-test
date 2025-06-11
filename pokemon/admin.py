from django.contrib import admin
from django.db.models import Count

from .models import Pokemon, Type

# Register your models here.
class PokemonAdmin(admin.ModelAdmin):
    list_display = ['name']
    fieldsets = [
        (None, {"fields": ["name", "type", "photo_url",]}), # re-ordered fields in change form
        ("evolution chain", {
            "fields": ["evolution_chain"],
            "classes": ["collapse"],
        }),
    ]
    search_fields = ['name']
    filter_horizontal = ['evolution_chain', 'type']


class TypeAdmin(admin.ModelAdmin):
    list_display = ['name','related_pokemon', 'related_pokemon_count']
    fields = ['name', 'related_pokemon']
    search_fields = ['name']

    # find pokemon in each type with type.pokemon_set "pokemon_set is related name"

    def get_queryset(self, request):
        query = super().get_queryset(request)
        return query.annotate(pokemon_count=Count('pokemon_set'))

    def related_pokemon(self, obj):
        return ", ".join(p.name for p in obj.pokemon_set.all())
    readonly_fields = ['related_pokemon']

    def related_pokemon_count(self, obj):
        return obj.pokemon_count
    related_pokemon_count.admin_order_field = 'pokemon_count'
    related_pokemon_count.short_description = 'Number of Pokémon for each'
    


admin.site.register(Pokemon, PokemonAdmin)
admin.site.register(Type, TypeAdmin)