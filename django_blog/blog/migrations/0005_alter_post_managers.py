# Generated by Django 4.2.2 on 2023-07-08 05:48

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='post',
            managers=[
                ('public', django.db.models.manager.Manager()),
            ],
        ),
    ]
