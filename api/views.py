from django.shortcuts import render
# Create your views here.
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets, views
from pokemon.models import Pokemon

from api.serializers import PokemonSerializer

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all().order_by('pk')
    serializer_class = PokemonSerializer
    # permission_classes = [permissions.IsAuthenticated]