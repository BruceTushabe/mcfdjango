
from core.models import Account  # Import your Account model
from openpyxl import load_workbook

def find_account(account_number):
    try:
        # Assuming Account model has a field 'account_number'
        # pylint: disable=no-member
        account = Account.objects.get(account_number=account_number)
        return account  # Return the found account object
    except Account.DoesNotExist:
        return None  # Account with the given account number does not exist


def populate_excel(account_number, form_data):
    # Load the Excel workbook
    workbook = load_workbook('path/to/your/excel_file.xlsx')

    # Select the active worksheet
    worksheet = workbook.active

    # Find the row corresponding to the given account number
    for row in worksheet.iter_rows(min_row=2, values_only=True):
        if row[0] == account_number:
            # Fill in the form data to the respective columns
            worksheet.cell(row=row[0], column=2).value = form_data['loan_application_date']
            worksheet.cell(row=row[0], column=3).value = form_data['purpose_of_the_loan']
            worksheet.cell(row=row[0], column=4).value = form_data['address_location']
            worksheet.cell(row=row[0], column=5).value = form_data['business_financed']
            worksheet.cell(row=row[0], column=6).value = form_data['group_name']
            worksheet.cell(row=row[0], column=7).value = form_data['reason_for_default_summarised']
            worksheet.cell(row=row[0], column=8).value = form_data['detailed_reason_for_default']

            # Save the workbook
            workbook.save('path/to/your/excel_file.xlsx')
            return

    # If the account number is not found, you can handle this case accordingly
    raise ValueError("Account number not found in the Excel sheet")