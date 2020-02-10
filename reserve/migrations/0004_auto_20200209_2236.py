# Generated by Django 3.0.1 on 2020-02-09 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_auto_20200207_1850'),
        ('reserve', '0003_auto_20200205_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='number',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='book',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rooms', to='rooms.Room'),
        ),
    ]