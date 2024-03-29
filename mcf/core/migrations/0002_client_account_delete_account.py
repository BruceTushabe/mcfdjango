# Generated by Django 5.0.2 on 2024-03-08 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client_Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SOL_ID', models.CharField(max_length=50, unique=True)),
                ('account_manager_user_id', models.CharField(max_length=50)),
                ('account_number', models.CharField(max_length=50, unique=True)),
                ('account_name', models.CharField(max_length=100)),
                ('days_in_arrears', models.IntegerField()),
                ('loan_balance', models.DecimalField(decimal_places=2, max_digits=20)),
                ('loan_term', models.CharField(max_length=50)),
                ('disbursed_amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('disbursement_date', models.DateField()),
                ('principal_balance', models.DecimalField(decimal_places=2, max_digits=20)),
                ('debt_arrears_start_date', models.DateField()),
                ('amount_claimed', models.DecimalField(decimal_places=2, max_digits=20)),
                ('loan_cycle', models.CharField(max_length=50)),
                ('mode_of_engagement', models.CharField(max_length=50)),
                ('claim_status', models.CharField(max_length=50)),
                ('age_category', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('contact', models.CharField(max_length=50)),
                ('DOB', models.DateField()),
                ('gender', models.CharField(max_length=50)),
                ('loan_application_date', models.DateField(blank=True, null=True)),
                ('address_location', models.CharField(blank=True, max_length=255)),
                ('purpose_of_loan', models.CharField(blank=True, max_length=255)),
                ('business_financed', models.CharField(blank=True, max_length=255)),
                ('group_name', models.CharField(blank=True, max_length=100)),
                ('reason_for_default_summarised', models.CharField(blank=True, max_length=255)),
                ('detailed_reason_for_default', models.TextField(blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Account',
        ),
    ]
