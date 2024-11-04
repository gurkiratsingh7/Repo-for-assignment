"""
Name: Gurkirat Singh
Topic Challenge: 6B
Date: October 10, 2024

"""

import csv

# Function to read CSV, modify the data (multiply by 2), and return a list of dictionaries
def csv_reader(file_name):
    modified_data = []
    
    # Open the CSV file and read it into a list of dictionaries
    with open(file_name, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        
        # For each row in the CSV file
        for row in reader:
            # Create a new dictionary to store the modified values
            modified_row = {}
            
            # Multiply each numerical value by 2 and store it in the modified_row
            for key, value in row.items():
                modified_row[key] = float(value) * 2  # Convert to float and multiply by 2
            
            # Append the modified row to the list
            modified_data.append(modified_row)
    
    return modified_data

# Function to write the modified list of dictionaries to a new CSV file
def csv_writer(file_name, data):
    # Get the field names (header) from the first dictionary in the list
    fieldnames = data[0].keys()
    
    # Open the new CSV file in write mode
    with open(file_name, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        # Write the header
        writer.writeheader()
        
        # Write the modified rows
        for row in data:
            writer.writerow(row)

# Main program
input_file = 'data.csv'  # Original CSV file
output_file = 'modified_data.csv'  # File to write the modified data

# Read and modify the data
modified_data = csv_reader(input_file)

# Write the modified data to a new CSV file
csv_writer(output_file, modified_data)

print(f"Data from {input_file} has been modified and written to {output_file}.")
