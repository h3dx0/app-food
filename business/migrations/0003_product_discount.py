# Generated by Django 3.0.5 on 2020-04-29 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0002_auto_20200429_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.IntegerField(default=50),
        ),
    ]