# Generated by Django 5.0.3 on 2024-04-13 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0008_order_receipt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='receipt',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
