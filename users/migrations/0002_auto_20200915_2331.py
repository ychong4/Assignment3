# Generated by Django 2.2 on 2020-09-16 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.IntegerField(blank=True, default=' ', null=True),
        ),
    ]
