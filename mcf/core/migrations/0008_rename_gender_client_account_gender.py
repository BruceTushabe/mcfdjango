# Generated by Django 5.0.3 on 2024-03-20 03:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_client_account_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client_account',
            old_name='Gender',
            new_name='GENDER',
        ),
    ]
