# Generated by Django 3.0.8 on 2020-10-31 01:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_auto_20201028_1129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='category_icon',
        ),
    ]
