import json
from bs4 import BeautifulSoup
import multiprocessing as mp

def clean_html(raw_html):
    soup = BeautifulSoup(raw_html, 'lxml')
    for br in soup.find_all("br"):
        br.replace_with("\n")
    return soup.get_text()

def process_posts(post_group):
    question = ''
    answer = ''
    for post in post_group['posts']:
        if 'com' in post:
            if not question:
                post_no = post['no']
                question = f"{'-'*5}\n---{post_no}\n{clean_html(post['com'])}"
            else:
                post_no = post['no']
                answer += f"---{post_no}\n{clean_html(post['com'])}\n\n"
    if answer:
        output_dict = {
            'question': question,
            'answer': answer
        }
        return json.dumps(output_dict, indent=4)
    else:
        return None

if __name__ == '__main__':
    input_file = 'data.ndjson'
    output_file = 'output.json'
    num_processes = mp.cpu_count()

    with open(input_file, 'r') as in_f, open(output_file, 'w') as out_f, mp.Pool(processes=num_processes) as pool:
        first_group = True
        out_f.write("[\n")
        for result in pool.imap(process_posts, (json.loads(line) for line in in_f), chunksize=100):
            if result:
                if not first_group:
                    out_f.write(",\n")
                else:
                    first_group = False
                out_f.write(result)
        out_f.write("\n]")
