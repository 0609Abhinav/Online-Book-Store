# Generated by Django 3.2.4 on 2021-09-30 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('senior', '0005_msg'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=120)),
                ('address', models.CharField(max_length=200)),
                ('mobile', models.CharField(max_length=20)),
                ('message', models.CharField(max_length=600)),
            ],
        ),
        migrations.DeleteModel(
            name='msg',
        ),
    ]
