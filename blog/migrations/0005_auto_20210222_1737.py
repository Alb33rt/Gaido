# Generated by Django 3.1.6 on 2021-02-22 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210222_0834'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-time_created']},
        ),
    ]