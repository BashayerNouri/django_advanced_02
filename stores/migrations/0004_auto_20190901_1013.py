# Generated by Django 2.1.5 on 2019-09-01 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0003_auto_20190901_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
