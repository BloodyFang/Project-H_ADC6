# Generated by Django 3.0 on 2020-01-09 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pdf',
            field=models.FileField(null=True, upload_to='file/files'),
        ),
    ]