from django.http import HttpResponse, FileResponse
from django.shortcuts import render
from openpyxl import load_workbook
from docx import Document
import os

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def contact(request):
    return render(request, 'core/contact.html')

def upload(request):
    return render(request, 'core/upload.html')

def form(request):
    return render(request, 'core/form.html')

# def download(request):
  #  return render(request, 'core/download.html')



# Function to find data for a specific account number in the Excel sheet
def find_account_data(account_number):
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
            try:
                value = str(account_data[index])
                for paragraph in document.paragraphs:
                    paragraph.text = paragraph.text.replace(placeholder, value)
                for table in document.tables:
                    for row in table.rows:
                        for cell in row.cells:
                            cell.text = cell.text.replace(placeholder, value)
            except Exception as e:
                print(f"Error populating document: {e}")
                return False
        return True
    return False

def generate(request):
    if request.method == 'POST':
        account_number = request.POST.get('account_number')
        account_data = find_account_data(account_number)
        if account_data:
            try:
                document = Document('template.docx')
                if populate_document_for_account(document, account_data):
                    output_filename = f"output_{account_number}.docx"
                    document.save(output_filename)
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
