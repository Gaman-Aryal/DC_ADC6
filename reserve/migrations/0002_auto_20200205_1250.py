# Generated by Django 3.0.1 on 2020-02-05 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='room',
            new_name='Room_ID',
        ),
        migrations.RenameField(
            model_name='reserve',
            old_name='user',
            new_name='Buyer_ID',
        ),
        migrations.RenameField(
            model_name='reserve',
            old_name='rooms',
            new_name='Room_ID',
        ),
    ]