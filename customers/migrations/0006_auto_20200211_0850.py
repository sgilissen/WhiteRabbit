# Generated by Django 3.0.3 on 2020-02-11 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_auto_20200211_0841'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customercontact',
            name='address_line_1',
        ),
        migrations.RemoveField(
            model_name='customercontact',
            name='address_line_2',
        ),
        migrations.RemoveField(
            model_name='customercontact',
            name='city',
        ),
        migrations.RemoveField(
            model_name='customercontact',
            name='country_code',
        ),
        migrations.RemoveField(
            model_name='customercontact',
            name='postal_code',
        ),
        migrations.RemoveField(
            model_name='customercontact',
            name='state',
        ),
    ]
