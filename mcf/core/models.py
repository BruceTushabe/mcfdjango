from django.db import models

# Create your models here.
class Client_Account(models.Model):
    SOL_ID = models.CharField(max_length=50)
    CIF_ID = models.CharField(max_length=50)
    COMBINED_CIF = models.CharField(max_length=50)
    SCHM_CODE = models.CharField(max_length=50)
    ACCT_MGR_USER_ID = models.CharField(max_length=50)
    ACCTNUM = models.CharField(max_length=50, unique=True)
    ACCT_NAME = models.CharField(max_length=100)
    ARREARSDAYS = models.CharField(max_length=50)
    LCYBALANCE = models.IntegerField(null=True)
    MAT_DATE = models.DateField(null=True)
    TERM = models.CharField(max_length=50)
    FLOW_AMT = models.DecimalField(max_digits=20, decimal_places=2)
    DIS_AMT = models.DecimalField(max_digits=20, decimal_places=2)
    DIS_SHDL_DATE = models.DateField()
    CLASSIFICATION = models.CharField(max_length=50)
    SCHEME_NAME = models.CharField(max_length=50)
    PRINCIPLE_BALANCE = models.DecimalField(max_digits=20, decimal_places=2)
    AMOUNT_CLAIMED = models.DecimalField(max_digits=20, decimal_places=2)
    DATE_ARREARS_START = models.DateField()
    LOAN_CYCLE = models.CharField(max_length=50)
    MODE_OF_ENGAGEMENT = models.CharField(max_length=50)
    CLAIM_STATUS = models.CharField(max_length=50)
    AGE_CATEGORY = models.CharField(max_length=100)
    AGE = models.IntegerField()
    CONTACT = models.CharField(max_length=50)
    DOB = models.DateField()     # Date of Birth
    Gender = models.CharField(max_length=50)
    loan_application_date = models.DateField(blank=True)
    address_location = models.CharField(max_length=255, blank=True)
    purpose_of_loan = models.CharField(max_length=255, blank=True)
    business_financed = models.CharField(max_length=255, blank=True)
    group_name = models.CharField(max_length=100, blank=True)
    reason_for_default_summarised = models.CharField(max_length=255, blank=True)
    detailed_reason_for_default = models.TextField(blank=True)



