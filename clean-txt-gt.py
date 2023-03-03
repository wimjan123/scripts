import argparse
import os

parser = argparse.ArgumentParser(description='Remove "&gt;" from text files')
parser.add_argument('--input', help='path to input file(s)', nargs='+')
args = parser.parse_args()

if not args.input:
    parser.error('Please specify the path to the input file(s) using --input')

for input_file in args.input:
    if not os.path.isfile(input_file):
        parser.error(f'{input_file} is not a valid file')

    output_filename = os.path.splitext(input_file)[0] + '_clean.txt'

    with open(input_file, 'r') as input_file, open(output_filename, 'w') as output_file:
        for line in input_file:
            output_file.write(line.replace('&gt;', ''))

    print(f'Successfully cleaned {input_file} and saved as {output_filename}')

