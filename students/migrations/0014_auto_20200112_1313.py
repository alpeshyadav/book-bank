# Generated by Django 3.0.2 on 2020-01-12 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0013_auto_20200112_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_edition',
            field=models.IntegerField(null=True),
        ),
    ]
