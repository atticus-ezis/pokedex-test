# from django.contrib.auth.models import Group, User
from rest_framework import serializers
from pokemon.models import Pokemon, Type

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'

class PokemonSerializer(serializers.ModelSerializer):
    type = TypeSerializer(many=True, read_only=True)
    evolution_chain = serializers.SerializerMethodField()
    class Meta:
        model = Pokemon
        fields = '__all__'

    def get_evolution_chain(self, obj):
        return [
            {
                "id": p.id,
                "name": p.name,
                "photo_url": p.photo_url
            }
            for p in obj.evolution_chain.all()
        ]

