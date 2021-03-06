# Generated by Django 3.0.5 on 2020-04-03 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='confirmados',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='registro',
            name='decesos',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='registro',
            name='descartados',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='registro',
            name='recuperados',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='registro',
            name='sospechosos',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='registro',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]
