# Generated by Django 2.2.6 on 2019-10-05 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0008_auto_20191001_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.BooleanField(default=0),
        ),
    ]
