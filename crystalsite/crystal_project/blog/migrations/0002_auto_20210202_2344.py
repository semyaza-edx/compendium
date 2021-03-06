# Generated by Django 3.1.6 on 2021-02-02 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compendium', '0003_auto_20210202_2344'),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='crystals',
            field=models.ManyToManyField(blank=True, related_name='blog_posts', to='compendium.Crystal'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='blog_posts', to='compendium.Tag'),
        ),
    ]
