# Generated by Django 3.0 on 2020-01-09 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20200109_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload_files',
            name='pdf',
            field=models.FileField(null=True, upload_to='files/'),
        ),
    ]
