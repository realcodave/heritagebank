# Generated by Django 4.0.3 on 2022-03-12 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amount',
            name='amount',
            field=models.CharField(max_length=30000),
        ),
    ]
