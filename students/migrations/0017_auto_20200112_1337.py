# Generated by Django 3.0.2 on 2020-01-12 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0016_auto_20200112_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]