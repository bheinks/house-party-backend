# Generated by Django 5.0.1 on 2025-01-01 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bartender', '0011_alter_drinkcategory_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drink',
            name='category',
        ),
        migrations.AddField(
            model_name='drink',
            name='categories',
            field=models.ManyToManyField(to='bartender.drinkcategory'),
        ),
    ]
