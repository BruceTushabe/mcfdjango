import psycopg2


def populate_database(**form_data):
   """Populate the core_client_account table in the mcfyaw database with form data."""
   try:
       # Connect to the PostgreSQL database
       conn = psycopg2.connect(database="mcfyaw")
       cur = conn.cursor()

       # Form data to insert (adjust column names as needed)
       data = {
           "loan_application_date": form_data.get("Loan Application Date"),
           "purpose_of_the_loan": form_data.get("Purpose of the Loan"),
           "address_location": form_data.get("Address/Location"),
           "business_financed": form_data.get("Business Financed"),
           "group_name": form_data.get("Group Name"),
           "reason_for_default_summarised": form_data.get("Reason for Default (Summarised)"),
           "detailed_reason_for_default": form_data.get("Detailed Reason for Default"),
           # Add other fields as needed, ensuring they match database column names
       }

       # Insert data into the core_client_account table
       sql = """INSERT INTO core_client_account (
                      loan_application_date,
                      purpose_of_the_loan,
                      address_location,
                      business_financed,
                      group_name,
                      reason_for_default_summarised,
                      detailed_reason_for_default
                  ) VALUES (
                      %s, %s, %s, %s, %s, %s, %s
                  )"""
       cur.execute(sql, tuple(data.values()))

       # Commit the changes to the database
       conn.commit()

       print("Data added to database successfully.")
   except Exception as e:
       print(f"An error occurred: {e}")
   finally:
       # Close the cursor and connection
       cur.close()
       conn.close()

"""def populate(template_path="data1.xlsx", **form_data):
    Populate an Excel template with data from the core_client_account table.
    try:
        wb = load_workbook(template_path)
        sheet = wb.active

        # Mapping form data to column indices
        column_indices = {
            "Account Number": 1,  # Assuming it's in the first column
            "Loan Application Date": 23,
            "Purpose of the Loan": 24,
            "Address/Location": 25,
            "Business Financed": 26,
            "Group Name": 27,
            "Reason for Default (Summarised)": 28,
            "Detailed Reason for Default": 29,
        }

        # Querying data from core_client_account table
        client_account = Client_Account.objects.get(account_number=form_data['account_number'])

        # Adding current timestamp for Loan Application Date

        # Writing form data to Excel
        for field, value in form_data.items():
            if field in column_indices:
                column_index = column_indices[field]
                sheet.cell(row=2, column=column_index, value=value)

        wb.save(template_path)
        print("Data added successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")"""
