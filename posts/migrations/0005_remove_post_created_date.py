# Generated by Django 2.2.5 on 2019-11-21 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='created_date',
        ),
    ]
