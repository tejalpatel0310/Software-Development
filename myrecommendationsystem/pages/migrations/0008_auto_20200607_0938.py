# Generated by Django 3.0.7 on 2020-06-07 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_myrating_places'),
    ]

    operations = [
        migrations.AlterField(
            model_name='places',
            name='descriptions',
            field=models.CharField(default='This is the amazing place.', max_length=500),
        ),
        migrations.AlterField(
            model_name='places',
            name='name',
            field=models.CharField(default='Location Name', max_length=100),
        ),
    ]