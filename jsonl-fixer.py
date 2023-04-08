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

def fix_jsonl_file(input_filename, output_filename):
    invalid_lines = []
    with open(input_filename, mode='r') as input_file:
        with jsonlines.open(output_filename, mode='w') as writer:
            lines = input_file.readlines()
            with Pool() as pool:
                fixed_lines = pool.map(fix_jsonl_line, lines)
                for index, fixed_line in enumerate(fixed_lines):
                    if fixed_line is not None:
                        writer.write(json.loads(fixed_line))
                    else:
                        invalid_lines.append(index + 1)

    if invalid_lines:
        print(f'Found {len(invalid_lines)} invalid lines:')
        for line in invalid_lines:
            print(f'Removed line {line} from output file')

if __name__ == '__main__':
    fix_jsonl_file('input.jsonl', 'output.jsonl')
