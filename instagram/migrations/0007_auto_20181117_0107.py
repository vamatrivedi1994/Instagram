# Generated by Django 2.1.2 on 2018-11-17 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0006_auto_20181117_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='photo',
            field=models.FileField(upload_to='media'),
        ),
    ]
