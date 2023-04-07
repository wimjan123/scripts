import json
import jsonlines
from multiprocessing import Pool

def convert_to_jsonlines(item):
    with jsonlines.open('gpt4.jsonl', mode='a') as writer:
        writer.write(item)

if __name__ == '__main__':
    with open('input.json', 'r') as json_file:
        data = json.load(json_file)

    with Pool() as pool:
        pool.map(convert_to_jsonlines, data)

    json_file.close()
