# Generated by Django 3.1.6 on 2021-02-05 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compendium', '0004_auto_20210202_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crystal',
            name='image',
            field=models.ImageField(blank=True, upload_to='galleries'),
        ),
    ]
