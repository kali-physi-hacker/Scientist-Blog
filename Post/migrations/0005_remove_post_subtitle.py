# Generated by Django 2.2.5 on 2019-09-12 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0004_post_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='subtitle',
        ),
    ]