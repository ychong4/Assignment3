# Generated by Django 2.2 on 2020-09-16 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200915_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.CharField(blank=True, default=' ', max_length=10, null=True),
        ),
    ]
