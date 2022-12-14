# Generated by Django 4.1.1 on 2022-09-29 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0005_game_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='developer',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='game',
            name='genre',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='game',
            name='publisher',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='game',
            name='rating_for',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='title',
            field=models.CharField(max_length=120),
        ),
    ]
