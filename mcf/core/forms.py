from django import forms

class PopulateExcelForm(forms.Form):
    """Form for populating the excel template"""
    account_number = forms.IntegerField(label="Account Number", required=True)
    loan_application_date = forms.DateField(label="Loan Application Date", required=True)
    purpose_of_the_loan = forms.CharField(label="Purpose of the Loan", required=True)
    address_location = forms.CharField(label="Address/Location", required=True)
    business_financed = forms.CharField(label="Business Financed", required=True)
    group_name = forms.CharField(label="Group Name", required=True)
    reason_for_default_summarised = forms.CharField(label="Reason for Default (Summarised)", required=True)
    detailed_reason_for_default = forms.CharField(label="Detailed Reason for Default", required=True)