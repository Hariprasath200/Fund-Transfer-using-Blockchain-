# Generated by Django 5.0.3 on 2024-03-21 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fund', '0003_blockchain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blockchain',
            name='current_transactions',
            field=models.JSONField(default=list),
        ),
    ]
