# Generated by Django 3.0 on 2020-01-09 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20200109_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload_files',
            name='File_Type',
            field=models.CharField(max_length=140, null=True),
        ),
    ]
