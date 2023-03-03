import argparse
import csv
import os

# Parse the input arguments
parser = argparse.ArgumentParser(description='Extract Reddit comments from CSV files')
parser.add_argument('--input-dir', help='path to directory containing input CSV files')
args = parser.parse_args()

# Check if the input argument is provided and the directory exists
if not args.input_dir:
    parser.error('Please specify the path to the input directory using --input-dir')

if not os.path.isdir(args.input_dir):
    parser.error(f'{args.input_dir} is not a valid directory')

# Loop over all the CSV files in the input directory
for filename in os.listdir(args.input_dir):
    if filename.endswith('.csv'):
        input_file = os.path.join(args.input_dir, filename)

        # Open the input CSV file
        with open(input_file, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            rows = []
            for row in reader:
                # Check if column 3 contains "[removed]"
                if "[deleted]" not in row[2]:
                    rows.append(row)

        # Generate the output filename
        output_filename = os.path.splitext(input_file)[0] + '.txt'

        # Open the output TXT file
        with open(output_filename, 'w') as txtfile:
            # Extract column 3 from each row and write to the TXT file
            for row in rows:
                txtfile.write("User:\n\nReddit Comment: " + row[1] + "\n<|endoftext|>\n")

        # Print a success message
        print(f'Successfully extracted Reddit comments from {input_file} and saved as {output_filename}')

