# Generated by Django 5.0.3 on 2024-03-20 03:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_rename_gender_client_account_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client_account',
            name='id',
        ),
        migrations.AlterField(
            model_name='client_account',
            name='ACCTNUM',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, unique=True),
        ),
        migrations.CreateModel(
            name='RelatedModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.client_account')),
            ],
        ),
    ]