# Generated by Django 4.2.2 on 2023-07-09 16:17

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_article_star'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='article',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
