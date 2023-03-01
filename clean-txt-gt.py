import argparse
import os

parser = argparse.ArgumentParser(description='Remove "&gt;" from a text file')
parser.add_argument('--input', help='path to input file')
args = parser.parse_args()

if not args.input:
    parser.error('Please specify the path to the input file using --input')

if not os.path.isfile(args.input):
    parser.error(f'{args.input} is not a valid file')

output_filename = os.path.splitext(args.input)[0] + '_clean.txt'

with open(args.input, 'r') as input_file, open(output_filename, 'w') as output_file:
    for line in input_file:
        output_file.write(line.replace('&gt;', ''))

print(f'Successfully cleaned {args.input} and saved as {output_filename}')

