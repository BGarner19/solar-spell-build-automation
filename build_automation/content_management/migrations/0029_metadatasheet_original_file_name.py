# Generated by Django 2.1.3 on 2019-02-26 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_management', '0028_remove_metadatasheet_updated_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='metadatasheet',
            name='original_file_name',
            field=models.CharField(max_length=300, null=True),
        ),
    ]