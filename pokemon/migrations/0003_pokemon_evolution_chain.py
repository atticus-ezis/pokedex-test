# Generated by Django 5.2.2 on 2025-06-10 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0002_alter_pokemon_photo_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='evolution_chain',
            field=models.ManyToManyField(blank=True, to='pokemon.pokemon'),
        ),
    ]
