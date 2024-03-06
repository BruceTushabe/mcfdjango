from datetime import datetime
from openpyxl import load_workbook

def populate(template_path="data1.xlsx", **form_data):
    """Populate an Excel template with form data."""
    try:
        wb = load_workbook(template_path)
        sheet = wb.active

        # Mapping form data to column indices
        column_indices = {
            "Loan Application Date": 23,
            "Purpose of the Loan": 24,
            "Address/Location": 25,
            "Business Financed": 26,
            "Group Name": 27,
            "Reason for Default (Summarised)": 28,
            "Detailed Reason for Default": 29,
        }

        # Adding current timestamp for Loan Application Date
        form_data["Loan Application Date"] = datetime.now()

        # Writing form data to Excel
        for field, value in form_data.items():
            if field in column_indices:
                column_index = column_indices[field]
                sheet.cell(row=2, column=column_index, value=value)

        wb.save(template_path)
        print("Data added successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
