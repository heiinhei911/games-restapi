# Generated by Django 4.1.1 on 2022-09-29 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_alter_game_rating_for'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='price',
            field=models.DecimalField(decimal_places=2, default=19.99, max_digits=4),
        ),
    ]
