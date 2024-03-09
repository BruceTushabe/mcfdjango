from django.db import models

# Create your models here.
class Client_Account(models.Model):
    SOL_ID = models.CharField(max_length=50, unique=True)
    account_manager_user_id = models.CharField(max_length=50)
    account_number = models.CharField(max_length=50, unique=True)
    account_name = models.CharField(max_length=100)
    days_in_arrears = models.IntegerField()
    loan_balance = models.DecimalField(max_digits=20, decimal_places=2)
    loan_term = models.CharField(max_length=50)
    disbursed_amount = models.DecimalField(max_digits=20, decimal_places=2)
    disbursement_date = models.DateField()
    principal_balance = models.DecimalField(max_digits=20, decimal_places=2)
    debt_arrears_start_date = models.DateField()
    amount_claimed = models.DecimalField(max_digits=20, decimal_places=2)
    loan_cycle = models.CharField(max_length=50)
    mode_of_engagement = models.CharField(max_length=50)
    claim_status = models.CharField(max_length=50)
    age_category = models.CharField(max_length=100)
    age = models.IntegerField()
    contact = models.CharField(max_length=50)
    DOB = models.DateField()     # Date of Birth
    gender = models.CharField(max_length=50)
    loan_application_date = models.DateField(blank=True)
    address_location = models.CharField(max_length=255, blank=True)
    purpose_of_loan = models.CharField(max_length=255, blank=True)
    business_financed = models.CharField(max_length=255, blank=True)
    group_name = models.CharField(max_length=100, blank=True)
    reason_for_default_summarised = models.CharField(max_length=255, blank=True)
    detailed_reason_for_default = models.TextField(blank=True)



