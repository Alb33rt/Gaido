# Generated by Django 3.1.6 on 2021-02-20 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_blogpost_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
