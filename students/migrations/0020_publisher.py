# Generated by Django 3.0.2 on 2020-01-18 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0019_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publisher', models.CharField(max_length=40)),
            ],
        ),
    ]
