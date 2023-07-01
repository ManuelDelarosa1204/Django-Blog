# Generated by Django 4.2.2 on 2023-07-01 16:13

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('body', models.TextField()),
                ('posted_date', models.DateTimeField(default=datetime.datetime(2023, 7, 1, 16, 13, 52, 6276, tzinfo=datetime.timezone.utc))),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField()),
                ('status', models.CharField(choices=[('PUBLIC', 'Public'), ('DRAFT', 'Draft')], default='PUBLIC', max_length=6)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-posted_date'],
                'indexes': [models.Index(fields=['-posted_date'], name='blog_post_posted__836476_idx')],
            },
        ),
    ]
