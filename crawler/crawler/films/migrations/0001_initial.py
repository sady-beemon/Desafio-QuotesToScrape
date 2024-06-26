# Generated by Django 4.0 on 2024-04-02 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.TextField(blank=True, null=True, verbose_name='Rank do filme')),
                ('title', models.TextField(blank=True, null=True, verbose_name='Titulo do filme')),
                ('date', models.TextField(blank=True, null=True, verbose_name='Data de filme')),
                ('time', models.TextField(blank=True, null=True, verbose_name='Tempo do filme')),
                ('minage', models.TextField(blank=True, null=True, verbose_name='Idade minima')),
                ('score', models.TextField(blank=True, null=True, verbose_name='Nota do filme')),
            ],
        ),
    ]
