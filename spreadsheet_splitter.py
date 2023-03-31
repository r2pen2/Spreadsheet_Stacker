import pandas as pd

print("File name? (exclude .xlsx)")
fileName = input()

# Read the xlsx file
input_file = fileName + ".xlsx"  # Replace with your file's name
output_file_prefix = 'output_sheet_'  # Replace with the desired output file name prefix

# Load all sheets into a dictionary
all_sheets = pd.read_excel(input_file, engine='openpyxl', sheet_name=None)

# Iterate through the sheets and save each one as a separate xlsx file
for sheet_name, sheet_data in all_sheets.items():
    output_file_name = f"{output_file_prefix}{sheet_name}.xlsx"
    sheet_data.to_excel(output_file_name, engine='openpyxl', index=False, sheet_name=sheet_name)

print("All sheets have been saved as separate xlsx files.")
