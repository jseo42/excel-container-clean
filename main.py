import pandas as pd
from modules.customer import clean_customer_column
from modules.cntr import clean_cntr_column
from modules.size import clean_size_column
from modules.dates import clean_date_column
from modules.ssl import clean_ssl_column
from modules.time import clean_time_column_with_misc
from modules.pu import clean_pu_column_with_misc
from modules.inv import clean_inv_status_column
from modules.rail import clean_rail_column


# Load the Excel file
file_path = 'Data/ABL CNTR - Copy.xlsx'  # Replace with actual path
excel_data = pd.ExcelFile(file_path)

# Selected sheets to process
selected_sheets = ['JUL 2024', 'AUG 2024', 'SEP 2024', 'OCT 2024', 'NOV 2024']

# List of date columns to process
date_columns = ['ETA PORT', 'ETA', 'APPT', 'LFD', 'OG', 'IG']

# Dictionary to store cleaned data for saving
cleaned_sheets = {}

# Process each selected sheet
for sheet_name in selected_sheets:
    if sheet_name in excel_data.sheet_names:
        print(f"\nProcessing sheet: {sheet_name}")
        sheet_data = excel_data.parse(sheet_name)
        
        # Clean the CUSTOMER column
        if 'CUSTOMER' in sheet_data.columns:
            sheet_data['CUSTOMER'] = clean_customer_column(sheet_data['CUSTOMER'])
        
        # Clean the CNTR# column
        if 'CNTR#' in sheet_data.columns:
            sheet_data['CNTR#'] = clean_cntr_column(sheet_data['CNTR#'])
        
        # Clean the SIZE column
        if 'SIZE' in sheet_data.columns:
            sheet_data['SIZE'] = clean_size_column(sheet_data['SIZE'])
        
        # Clean all date columns
        for date_col in date_columns:
            if date_col in sheet_data.columns:
                print(f"\nCleaning date column: {date_col}")
                sheet_data[date_col] = clean_date_column(sheet_data[date_col], date_col)
        
        # Clean the SSL column
        if 'SSL' in sheet_data.columns:
            print(f"\nCleaning SSL column in sheet: {sheet_name}")
            sheet_data['SSL'] = clean_ssl_column(sheet_data['SSL'])

        # Clean the TIME column
        if 'TIME' in sheet_data.columns:
            print(f"\nCleaning TIME column in sheet: {sheet_name}")
            sheet_data = clean_time_column_with_misc(sheet_data, "TIME")
        
        # Clean PU# Column and create PU# MISC
        if 'PU#' in sheet_data.columns:
            print(f"\nCleaning PU# column in sheet: {sheet_name}")
            sheet_data = clean_pu_column_with_misc(sheet_data, "PU#")

        # Clean Inv Status column and create Inv # column
        if 'Inv status' in sheet_data.columns:
            print(f"\nCleaning 'Inv status' column in sheet: {sheet_name}")
            sheet_data = clean_inv_status_column(sheet_data, "Inv status")

        # Clean Rail Column    
        if 'Rail' in sheet_data.columns:
            print(f"\nCleaning Rail column in sheet: {sheet_name}")
            sheet_data = clean_rail_column(sheet_data, "Rail")
        
        # Store the cleaned sheet for saving
        cleaned_sheets[sheet_name] = sheet_data

# Save the cleaned data back to a new Excel file
output_file_path = 'cleaned_data_with_fixed_Rail.xlsx'
with pd.ExcelWriter(output_file_path, engine='openpyxl') as writer:
    for sheet_name, sheet_data in cleaned_sheets.items():
        sheet_data.to_excel(writer, sheet_name=sheet_name, index=False)

print(f"\nCleaned data has been saved to {output_file_path}")
