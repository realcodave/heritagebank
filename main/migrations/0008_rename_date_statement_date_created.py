# Generated by Django 4.0.3 on 2022-03-12 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_amount_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='statement',
            old_name='date',
            new_name='date_created',
        ),
    ]
