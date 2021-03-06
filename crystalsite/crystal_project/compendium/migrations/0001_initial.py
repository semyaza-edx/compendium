# Generated by Django 3.1.6 on 2021-02-01 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=31, unique=True)),
                ('slug', models.SlugField(help_text='A label for URL config', max_length=31, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Crystal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=31)),
                ('slug', models.SlugField(help_text='A label for URL config', max_length=31, unique=True)),
                ('color', models.CharField(max_length=31)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('tags', models.ManyToManyField(to='compendium.Tag')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
