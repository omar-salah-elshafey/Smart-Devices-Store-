# Generated by Django 4.2.4 on 2023-08-15 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='airpod',
            options={'ordering': ['date_added']},
        ),
        migrations.AlterModelOptions(
            name='phone',
            options={'ordering': ['date_added']},
        ),
        migrations.AlterModelOptions(
            name='tab',
            options={'ordering': ['date_added']},
        ),
        migrations.AlterModelOptions(
            name='watch',
            options={'ordering': ['date_added']},
        ),
    ]
