# Generated by Django 5.0.3 on 2024-03-22 05:11

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fund', '0006_auto_20240322_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='fund',
            name='hash_value',
            field=models.CharField(default=django.utils.timezone.now, editable=False, max_length=64),
            preserve_default=False,
        ),
    ]
