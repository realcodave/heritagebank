# Generated by Django 4.0.3 on 2022-03-12 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_statement_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statement',
            name='alert',
            field=models.CharField(blank=True, choices=[('Transfer', 'Transfer'), ('Withdraw', 'Withdraw')], max_length=300, null=True),
        ),
    ]
