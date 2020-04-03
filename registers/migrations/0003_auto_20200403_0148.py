# Generated by Django 3.0.5 on 2020-04-03 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registers', '0002_auto_20200403_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='confirmados',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='registro',
            name='decesos',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='registro',
            name='descartados',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='registro',
            name='recuperados',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='registro',
            name='sospechosos',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='registro',
            name='total',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
