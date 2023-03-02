import argparse
import csv
import os

# Parse the input arguments
parser = argparse.ArgumentParser(description='Extract Reddit comments from a CSV file')
parser.add_argument('--input', help='path to input CSV file')
args = parser.parse_args()

# Check if the input argument is provided and the file exists
if not args.input:
    parser.error('Please specify the path to the input file using --input')

if not os.path.isfile(args.input):
    parser.error(f'{args.input} is not a valid file')

# Open the input CSV file
with open(args.input, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    rows = []
    for row in reader:
        # Check if column 3 contains "[removed]"
        if "[deleted]" not in row[2]:
            rows.append(row)

# Generate the output filename
output_filename = os.path.splitext(args.input)[0] + '.txt'

# Open the output TXT file
with open(output_filename, 'w') as txtfile:
    # Extract column 3 from each row and write to the TXT file
    for row in rows:
        txtfile.write("User:\n\nReddit Comment: " + row[1] + "\n<|endoftext|>\n")

# Print a success message
print(f'Successfully extracted Reddit comments from {args.input} and saved as {output_filename}')

