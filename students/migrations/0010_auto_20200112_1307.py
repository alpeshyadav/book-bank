# Generated by Django 3.0.2 on 2020-01-12 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0009_auto_20200112_1302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='id',
        ),
        migrations.AddField(
            model_name='book',
            name='book_id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
