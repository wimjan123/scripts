import ndjson
import csv
import argparse
import os

parser = argparse.ArgumentParser(description='Convert NDJSON to CSV')
parser.add_argument('--input', help='path to input NDJSON file')
args = parser.parse_args()

if not args.input:
    parser.error('Please specify the path to the input NDJSON file using --input')

if not os.path.isfile(args.input):
    parser.error(f'{args.input} is not a valid file')

output_filename = os.path.splitext(args.input)[0] + '.csv'

# Open the input NDJSON file
with open(args.input, 'r', encoding='utf-8') as f:
    # Open the output CSV file
    with open(output_filename, 'w', newline='', encoding='utf-8') as g:
        writer = csv.writer(g)
        # Parse the NDJSON data and write each row to the CSV file
        for row in ndjson.load(f):
            writer.writerow(row.values())

print(f'Successfully converted {args.input} to {output_filename}')

