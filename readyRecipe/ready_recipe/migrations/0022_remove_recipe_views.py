# Generated by Django 2.1.5 on 2020-03-17 23:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ready_recipe', '0021_remove_userprofile_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='views',
        ),
    ]
