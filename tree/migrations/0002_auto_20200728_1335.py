# Generated by Django 3.0.8 on 2020-07-28 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='name',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='node',
            name='value',
            field=models.IntegerField(null=True, unique=True),
        ),
    ]
