# Generated by Django 3.0.2 on 2020-01-12 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0017_auto_20200112_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='purchase_year',
            field=models.DateTimeField(null=True),
        ),
    ]