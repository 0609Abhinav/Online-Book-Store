# Generated by Django 3.2.4 on 2021-10-04 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('senior', '0007_auto_20211001_2056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reg',
            name='id',
        ),
        migrations.AlterField(
            model_name='reg',
            name='email',
            field=models.EmailField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
