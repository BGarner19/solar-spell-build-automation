# Generated by Django 2.1.3 on 2019-02-25 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content_management', '0027_auto_20190225_0018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='metadatasheet',
            name='updated_time',
        ),
    ]
