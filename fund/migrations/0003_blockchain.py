# Generated by Django 5.0.3 on 2024-03-21 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fund', '0002_fund'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blockchain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chain', models.TextField()),
                ('current_transactions', models.TextField(default='[]')),
            ],
        ),
    ]
