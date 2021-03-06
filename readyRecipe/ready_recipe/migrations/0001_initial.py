# Generated by Django 2.1.5 on 2020-02-27 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('recommentations', models.CharField(max_length=3000)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, unique=True)),
                ('instuction', models.CharField(max_length=2000)),
                ('picture', models.ImageField(upload_to='')),
                ('portions', models.IntegerField(default=0)),
                ('difficulty', models.IntegerField(default=0)),
                ('completion_time', models.CharField(max_length=100)),
                ('calories', models.IntegerField(default=0)),
                ('average_overall_price', models.FloatField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='recipe_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ready_recipe.Recipe'),
        ),
    ]
