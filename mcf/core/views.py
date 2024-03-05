
"""Views for the core app."""
import os
from django.http import HttpResponse, FileResponse
from django.shortcuts import redirect, render
from openpyxl import load_workbook
from docx import Document
from core.utils import find_account
from core.populate_excel import populate_excel
from core import populate_excel
from .forms import PopulateExcelForm

# Create your views here.

def index(request):
    '''View function for home page of site.'''   
    return render(request, 'core/index.html')

def contact(request):
    """View function for contact page of site."""
    return render(request, 'core/contact.html')

def upload(request):
    """View function for uplaod page """
    return render(request, 'core/upload.html')

def populate_excel_view(request):
    """View function for the loan form page."""

    if request.method == 'POST':
        form = PopulateExcelForm(request.POST)
        if form.is_valid():
            account_number = form.cleaned_data['account_number']
            form_data = form.cleaned_data
            populate_excel(account_number, form_data)
            return redirect('core:success')  # Redirect to success page
        else:
            return render(request, 'core/loan_form.html', {'form': form})
    else:
        account_number = request.GET.get('account')
        if account_number:
            account = find_account(account_number)
            if account:
                form = PopulateExcelForm(initial={'account_number': account_number})
                return render(request, 'core/loan_form.html', {'form': form})
            else:
                error_message = "Account not found. Please enter a valid account number."
                return render(request, 'core/error.html', {'error_message': error_message})
        else:
            form = PopulateExcelForm()
            return render(request, 'core/account_search.html', {'form': form})

def success_view(request):
    """View function for success page"""
    context = {'message': 'Your form has been submitted successfully!'}
    return render(request, 'core/success.html', context)



# Function to find data for a specific account number in the Excel sheet
def find_account_data(account_number):
    """Find account data in the Excel sheet."""
    try:
        account_number = int(account_number)  # Convert to integer for comparison
        workbook = load_workbook('data1.xlsx', data_only=True)
        sheet = workbook.active
        for row in sheet.iter_rows(min_row=2, values_only=True):
            if row[2] == account_number:
                
                return row  # Return the row data if account number is found
            
    except Exception as e:
        print(f"Error finding account data: {e}")
    return None  # Return None if account number is not found

# Function to populate the Word document with data for a specific account number
def populate_document_for_account(document, account_data):
    """Populate the Word document with data for a specific account number."""
    if account_data:
        placeholders = {
            "{{Name}}": 3,
            "{{disAmount}}": 7,
            "{{disDate}}": 8,
            "{{address}}": 21,
            "{{age}}": 16,
            "{{gender}}": 20,
            "{{dob}}": 18,
            "{{appdate}}": 19,
            "{{amtclaimed}}": 11,
            "{{datearrears}}": 10,
            "{{arrearsdays}}": 4,
            "{{loanterm}}": 6
        }

        for placeholder, index in placeholders.items():
            if index < len(account_data):
                try:
                    value = str(account_data[index])
                    for paragraph in document.paragraphs:
                        paragraph.text = paragraph.text.replace(placeholder, value)
                    for table in document.tables:
                        for row in table.rows:
                            for cell in row.cells:
                                cell.text = cell.text.replace(placeholder, value)
                except (AttributeError, TypeError) as e:
                    print(f"Error replacing placeholder {placeholder}: {e}")
            else:
                print(f"Index {index} out of range for account data")
                print(f"Error populating document: {e}")
                return False
        return True
    return False
def additional(account_data):
    """Check if additional information is needed for a specific account number."""
     # Define your logic here to check if additional information is needed
     # For now, let's just return False
    loan_date = account_data.get('loan_date', None)
    loan_purpose = account_data.get('loan_purpose', None)

    if not loan_date or not loan_purpose:
        return True  # Additional information is needed
    else:
        return False  # No additional information is needed
    

def generate(request):
    """View function for the generate page."""
    if request.method == 'POST':
        account_number = request.POST.get('account_number')
        account_data = find_account_data(account_number)
        if account_data:
            try:
                document = Document('template.docx')
                if populate_document_for_account(document, account_data):
                    output_filename = f"output_{account_number}.docx"
                    document.save(output_filename)
                    # Check if additional information is needed
                    # For example, you can check if any specific data is missing from the account_data
                    if additional(account_data):
                        # Save account_number in session to pass to the second form
                        request.session['account_number'] = account_number
                        return redirect('form')  # Redirect to the second form
                    else:
                        # Serve the file for download
                        file_path = os.path.join(os.path.dirname(__file__), output_filename)
                        if os.path.exists(file_path):
                            with open(file_path, 'rb') as f:
                                response = FileResponse(f)
                                response['Content-Disposition'] = f'attachment; filename="{output_filename}"'
                                return response
                        else:
                            return HttpResponse("File not found", status=404)
                else:
                    return HttpResponse("Failed to generate document", status=500)
            except Exception as e:
                return HttpResponse(f"An error occurred: {e}", status=500)
        else:
            return HttpResponse("Account number not found", status=404)
    else:
        return render(request, 'core/generate.html')