# Generated by Django 3.0.3 on 2020-02-11 00:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('vat_number', models.CharField(max_length=32)),
                ('vat_applicable', models.BooleanField(default=True)),
                ('iban', models.CharField(blank=True, max_length=255)),
                ('bic', models.CharField(blank=True, max_length=32)),
                ('phone', models.CharField(blank=True, max_length=32)),
                ('email', models.EmailField(blank=True, max_length=255)),
                ('address_line_1', models.CharField(max_length=255)),
                ('address_line_2', models.CharField(blank=True, max_length=255)),
                ('state', models.CharField(blank=True, max_length=255)),
                ('postal_code', models.CharField(max_length=32)),
                ('city', models.CharField(max_length=255)),
                ('country_code', models.CharField(choices=[('BE', 'Belgium'), ('CN', 'China'), ('DE', 'Germany'), ('FR', 'France'), ('HK', 'Hong Kong'), ('NL', 'The Netherlands'), ('PL', 'Poland'), ('US', 'United States of America')], default='BE', max_length=2)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='consultantprofile',
            name='address_line_1',
        ),
        migrations.RemoveField(
            model_name='consultantprofile',
            name='address_line_2',
        ),
        migrations.RemoveField(
            model_name='consultantprofile',
            name='bic',
        ),
        migrations.RemoveField(
            model_name='consultantprofile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='consultantprofile',
            name='company_name',
        ),
        migrations.RemoveField(
            model_name='consultantprofile',
            name='country_code',
        ),
        migrations.RemoveField(
            model_name='consultantprofile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='consultantprofile',
            name='iban',
        ),
        migrations.RemoveField(
            model_name='consultantprofile',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='consultantprofile',
            name='postal_code',
        ),
        migrations.RemoveField(
            model_name='consultantprofile',
            name='state',
        ),
        migrations.RemoveField(
            model_name='consultantprofile',
            name='vat_applicable',
        ),
        migrations.RemoveField(
            model_name='consultantprofile',
            name='vat_number',
        ),
        migrations.AddField(
            model_name='consultantprofile',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.CompanyProfile'),
            preserve_default=False,
        ),
    ]