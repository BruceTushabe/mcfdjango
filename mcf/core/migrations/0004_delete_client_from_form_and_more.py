# Generated by Django 5.0.2 on 2024-03-10 08:52

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_client_from_form_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Client_From_Form',
        ),
        migrations.AddField(
            model_name='client_account',
            name='address_location',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='client_account',
            name='business_financed',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='client_account',
            name='detailed_reason_for_default',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='client_account',
            name='group_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='client_account',
            name='loan_application_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client_account',
            name='purpose_of_loan',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='client_account',
            name='reason_for_default_summarised',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
