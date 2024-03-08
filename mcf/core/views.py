
"""Views for the core app."""
import os
from datetime import datetime
from django.http import HttpResponse, FileResponse
from django.shortcuts import redirect, render
from openpyxl import load_workbook
from docx import Document
#from core.utils import find_account_data, additional
from .populate_excel import populate
from .forms import PopulateExcelForm

# Create your views here.

def index(request):
    '''View function for home page of site.'''   
    return render(request, 'core/index.html')

def contact(request):
    """View function for contact page of site."""
    return render(request, 'core/contact.html')

def upload(request):
    """View function for upload page"""
    return render(request, 'core/upload.html')

# Define the find_account_data function here
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

def populate_excel_view(request):
    """View function for the loan form page."""

    if request.method == 'POST':
        form = PopulateExcelForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data  # No need to extract account_number separately
            # Call populate with keyword arguments
            populate(form_data)  # Remove account_number from the call
            return redirect('core:success_view')  # Redirect to success page
        else:
            return render(request, 'core/loan_form.html', {'form': form})
    else:
        account_number = request.GET.get('account')
        if account_number:
            account = find_account_data(account_number)
            if account:
                account_name = account[3]
                form = PopulateExcelForm(initial={'account_number': account_number})
                return render(request, 'core/loan_form.html', {'form': form, 'account_name': account_name})
            else:
                error_message = "Account not found. Please enter a valid account number."
                return render(request, 'core/error.html', {'error_message': error_message})
        else:
            form = PopulateExcelForm()
            return render(request, 'core/account_search.html', {'form': form})
      
def success_view(request):
    
    context = {'message': 'Your form has been submitted successfully!'}
    return render(request, 'core/success.html', context)

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
