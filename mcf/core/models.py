from django.db import models

# Create your models here.
class Account(models.Model):
    
    account_number = models.CharField(max_length=50, unique=True)
    loan_application_date = models.DateField(null=True, blank=True)
    purpose_of_loan = models.CharField(max_length=255, blank=True)
    address_location = models.CharField(max_length=255, blank=True)
    business_financed = models.CharField(max_length=255, blank=True)
    group_name = models.CharField(max_length=100, blank=True)
    reason_for_default_summarised = models.CharField(max_length=255, blank=True)
    detailed_reason_for_default = models.TextField(blank=True)


