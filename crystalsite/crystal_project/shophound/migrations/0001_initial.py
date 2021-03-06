# Generated by Django 3.1.6 on 2021-02-23 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RockShop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(help_text='for URL; no spaces')),
                ('address', models.CharField(max_length=100)),
                ('website', models.URLField()),
                ('hours', models.CharField(max_length=150)),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
