from django.contrib import admin

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
    filter_horizontal = ['evolution_chain']

# class PokemonInline(admin.TabularInline):
#     model = Pokemon

class TypeAdmin(admin.ModelAdmin):
    list_display = ['name','related_pokemon']
    fields = ['name', 'related_pokemon']
    search_fields = ['name']
    # get pokemon for each
    def related_pokemon(self, obj):
        return ", ".join(p.name for p in obj.pokemon_set.all())
    readonly_fields = ['related_pokemon']


admin.site.register(Pokemon, PokemonAdmin)
admin.site.register(Type, TypeAdmin)