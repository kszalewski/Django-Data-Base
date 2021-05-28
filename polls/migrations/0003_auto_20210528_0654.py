# Generated by Django 3.1.7 on 2021-05-28 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20210528_0619'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projekty',
            old_name='data_zak',
            new_name='do_data',
        ),
        migrations.RenameField(
            model_name='projekty',
            old_name='data_roz',
            new_name='od_data',
        ),
        migrations.RenameField(
            model_name='rekrutacja',
            old_name='id_stanowiska',
            new_name='stanowisko',
        ),
        migrations.RenameField(
            model_name='szkolenia',
            old_name='id_pracownika',
            new_name='pracownik',
        ),
        migrations.RenameField(
            model_name='urlopy',
            old_name='id_pracownika',
            new_name='pracownik',
        ),
        migrations.AddField(
            model_name='premia',
            name='nazwa',
            field=models.CharField(default='Bazowa', max_length=200),
            preserve_default=False,
        ),
    ]
