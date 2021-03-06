# Generated by Django 3.0.3 on 2020-02-11 23:44

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200211_0030'),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='consultant',
        ),
        migrations.AddField(
            model_name='project',
            name='billing_rate',
            field=models.CharField(choices=[('HR', 'Hourly Rate'), ('FD', 'Flat Daily Rate'), ('PR', 'Per-Project Basis')], default='HR', max_length=2),
        ),
        migrations.CreateModel(
            name='Timesheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(blank=True, max_length=100)),
                ('start_date', models.DateField(default=datetime.date.today)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('consultant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.ConsultantProfile')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project')),
            ],
        ),
        migrations.CreateModel(
            name='TimeEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('units', models.DecimalField(decimal_places=2, max_digits=10)),
                ('timesheet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Timesheet')),
            ],
        ),
    ]
