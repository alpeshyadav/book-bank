# Generated by Django 3.0.2 on 2020-01-12 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0010_auto_20200112_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='barcode',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='book',
            name='purchase_year',
            field=models.DateTimeField(),
        ),
    ]