# Generated by Django 4.0 on 2024-04-03 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='rank',
            field=models.IntegerField(blank=True, null=True, verbose_name='Rank do filme'),
        ),
    ]