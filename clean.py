import argparse
import os
import csv

parser = argparse.ArgumentParser(description='Filter out rows containing [deleted] in column B of a CSV file')
parser.add_argument('--input', help='path to input CSV file')
args = parser.parse_args()

if not args.input:
    parser.error('Please specify the path to the input CSV file using --input')

if not os.path.isfile(args.input):
    parser.error(f'{args.input} is not a valid file')

output_filename = os.path.splitext(args.input)[0] + '_sifted.csv'

with open(args.input, 'r', newline='', encoding='utf-8') as f, \
     open(output_filename, 'w', newline='', encoding='utf-8') as g:
    reader = csv.reader(f)
    writer = csv.writer(g)
    for row in reader:
        if '[deleted]' not in row[1]:
            writer.writerow(row)

print(f'Successfully sifted {args.input} and saved as {output_filename}')

