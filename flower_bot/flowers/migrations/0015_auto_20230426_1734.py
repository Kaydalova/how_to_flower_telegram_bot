# Generated by Django 2.2.16 on 2023-04-26 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flowers', '0014_auto_20230424_1742'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flower',
            old_name='pat_friendly',
            new_name='pet_friendly',
        ),
    ]
