# Generated by Django 2.1.2 on 2018-11-11 03:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instagram', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='following', to=settings.AUTH_USER_MODEL)),
                ('following', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='followers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='follows',
            name='follower',
        ),
        migrations.RemoveField(
            model_name='follows',
            name='following',
        ),
        migrations.DeleteModel(
            name='follows',
        ),
    ]
