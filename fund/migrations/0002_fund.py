# Generated by Django 5.0.3 on 2024-03-21 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fund', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('mobile', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('description', models.TextField()),
            ],
        ),
    ]