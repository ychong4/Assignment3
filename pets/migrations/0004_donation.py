# Generated by Django 3.0.10 on 2020-11-07 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0003_pet_available'),
    ]

    operations = [
        migrations.CreateModel(
            name='donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('braintree_id', models.CharField(blank=True, max_length=150)),
            ],
        ),
    ]
