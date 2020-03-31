# Generated by Django 2.1.5 on 2020-03-25 00:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ready_recipe', '0024_auto_20200325_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='recipe_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ready_recipe.Recipe'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user1',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
