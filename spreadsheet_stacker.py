import pandas as pd

print("File name? (exclude .xlsx)")
fileName = input()

# Read the xlsx file
input_file = fileName + ".xlsx"  # Replace with your file's name
output_file = fileName + '_stacked.xlsx'  # Replace with the desired output file name
df = pd.read_excel(input_file, engine='openpyxl')

# Stack the rows into a single column
stacked_df = df.stack().reset_index(drop=True).to_frame()

# Rename the column
stacked_df.columns = ['values']

# Write the output to a new xlsx file
stacked_df.to_excel(output_file, engine='openpyxl', index=False)
