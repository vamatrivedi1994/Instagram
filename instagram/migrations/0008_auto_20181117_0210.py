# Generated by Django 2.1.2 on 2018-11-17 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0007_auto_20181117_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='photo',
            field=models.FileField(upload_to='documents/'),
        ),
    ]
