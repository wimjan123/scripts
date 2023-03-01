import json
import csv
import sys
import os

# Get the input filename from the command-line arguments
input_filename = sys.argv[1]

# Define the output filename by replacing the extension with .csv
output_filename = os.path.splitext(input_filename)[0] + '.csv'

# Open the input file for reading and the output file for writing
with open(input_filename, 'r') as f_input, open(output_filename, 'w', newline='') as f_output:
    # Create a csv writer object
    writer = csv.writer(f_output)

    # Loop over each line in the ndjson file
    for line in f_input:
        # Load the json object from the line
        obj = json.loads(line)

        # If this is the first object, write the header row
        if f_input.tell() == len(line):
            writer.writerow(obj.keys())

        # Write the values of the object as a row in the csv file
        writer.writerow(obj.values())
        
print("Conversion completed successfully!")
