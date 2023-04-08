import json
import jsonlines
from multiprocessing import Pool

def fix_jsonl_line(line):
    try:
        json.loads(line)
        return line
    except json.JSONDecodeError:
        stripped_line = line[:line.rfind('}') + 1]
        try:
            json.loads(stripped_line)
            return stripped_line
        except json.JSONDecodeError:
            return None

def process_lines(lines):
    with Pool() as pool:
        for fixed_line in pool.imap_unordered(fix_jsonl_line, lines):
            yield fixed_line

def fix_jsonl_file(input_filename, output_filename):
    invalid_lines = []

    with open(input_filename, mode='r') as input_file:
        with jsonlines.open(output_filename, mode='w') as writer:
            line_number = 0
            for fixed_line in process_lines(input_file):
                line_number += 1
                if fixed_line is not None:
                    writer.write(json.loads(fixed_line))
                else:
                    invalid_lines.append(line_number)

    if invalid_lines:
        print(f'Found {len(invalid_lines)} invalid lines:')
        for line in invalid_lines:
            print(f'Removed line {line} from output file')

if __name__ == '__main__':
    fix_jsonl_file('input.jsonl', 'output.jsonl')
