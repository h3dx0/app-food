# Generated by Django 3.0.5 on 2020-04-29 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general_admin', '0002_auto_20200429_2221'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['first_name'], 'verbose_name_plural': 'Usuarios'},
        ),
        migrations.AlterModelOptions(
            name='usertype',
            options={'ordering': ['type'], 'verbose_name_plural': 'Tipos Usuarios'},
        ),
    ]