import argparse
import csv
import ndjson
import os


def remove_gt(input_file):
    output_filename = os.path.splitext(input_file)[0] + '_clean.txt'
    with open(input_file, 'r') as input_file, open(output_filename, 'w') as output_file:
        for line in input_file:
            output_file.write(line.replace('&gt;', ''))
    print(f'Successfully cleaned {input_file} and saved as {output_filename}')


def sift_deleted(input_csv):
    output_filename = os.path.splitext(input_csv)[0] + '_sifted.csv'
    with open(input_csv, 'r', newline='', encoding='utf-8') as f, \
            open(output_filename, 'w', newline='', encoding='utf-8') as g:
        reader = csv.reader(f)
        writer = csv.writer(g)
        for row in reader:
            if '[deleted]' not in row[1]:
                writer.writerow(row)
    print(f'Successfully sifted {input_csv} and saved as {output_filename}')


def extract_comments(input_csv):
    with open(input_csv, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = []
        for row in reader:
            if "[deleted]" not in row[2]:
                rows.append(row)
    output_filename = os.path.splitext(input_csv)[0] + '.txt'
    with open(output_filename, 'w') as txtfile:
        for row in rows:
            txtfile.write("User:\n\nReddit Comment: " + row[1] + "\n\n")
    print(f'Successfully extracted Reddit comments from {input_csv} and saved as {output_filename}')


def convert_ndjson_to_csv(input_ndjson):
    output_filename = os.path.splitext(input_ndjson)[0] + '.csv'
    with open(input_ndjson, 'r', encoding='utf-8') as f, open(output_filename, 'w', newline='', encoding='utf-8') as g:
        writer = csv.writer(g)
        for row in ndjson.load(f):
            writer.writerow(row.values())
    print(f'Successfully converted {input_ndjson} to {output_filename}')


def main():
    parser = argparse.ArgumentParser(description='Batch process data files')
    parser.add_argument('--path', help='path to directory containing input files')
    args = parser.parse_args()

    if not args.path:
        parser.error('Please specify the path to the input directory using --path')

    if not os.path.isdir(args.path):
        parser.error(f'{args.path} is not a valid directory')

    for file in os.listdir(args.path):
        if file.endswith('.txt'):
            remove_gt(os.path.join(args.path, file))
        elif file.endswith('.csv'):
            if '[deleted]' in open(os.path.join(args.path, file), encoding='utf-8').read():
                sift_deleted(os.path.join(args.path, file))
            else:
                extract_comments(os.path.join(args.path, file))
        elif file.endswith('.json'):
            convert_ndjson_to_csv(os.path.join(args.path, file))


if __name__ == '__main__':
    main()


