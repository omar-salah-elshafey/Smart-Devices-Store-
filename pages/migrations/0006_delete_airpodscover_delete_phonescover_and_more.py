# Generated by Django 4.2.4 on 2023-08-17 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_airpodscover_blogcover_phonescover_tabscover_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AirpodsCover',
        ),
        migrations.DeleteModel(
            name='PhonesCover',
        ),
        migrations.DeleteModel(
            name='TabsCover',
        ),
        migrations.DeleteModel(
            name='WatchesCover',
        ),
    ]
