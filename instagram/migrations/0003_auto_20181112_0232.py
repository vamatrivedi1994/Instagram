# Generated by Django 2.1.2 on 2018-11-12 02:32

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instagram', '0002_auto_20181111_0356'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='follower',
            unique_together={('follower', 'following')},
        ),
    ]
