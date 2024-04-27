# Generated by Django 5.0.3 on 2024-03-21 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fund', '0004_alter_blockchain_current_transactions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=100)),
                ('recipient', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Blockchain',
        ),
    ]
