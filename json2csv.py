import json
import csv
import sys
import os

# Get the input filename from the command-line arguments
input_filename = sys.argv[1]

# Define the output filename by replacing the extension with .csv
output_filename = os.path.splitext(input_filename)[0] + '.csv'

# Load the json data from the input file into memory
with open(input_filename, 'r') as f:
    data = json.load(f)

# Open the output file for writing
with open(output_filename, 'w', newline='') as f:
    # Create a csv writer object
    writer = csv.writer(f)

    # Write the header row
    writer.writerow(data[0].keys())

    # Loop over each object in the data and write its values as a row in the csv file
    for obj in data:
        writer.writerow(obj.values())
        
print("Conversion completed successfully!")
