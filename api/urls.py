from django.urls import path, include
from api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'pokemon', views.PokemonViewSet)


urlpatterns = [
    path('', include(router.urls)),
]