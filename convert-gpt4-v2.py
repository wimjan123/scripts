import json
from bs4 import BeautifulSoup

def clean_html(raw_html):
    soup = BeautifulSoup(raw_html, 'lxml')
    for br in soup.find_all("br"):
        br.replace_with("\n")
    return soup.get_text()

def process_posts(in_file, out_file):
    with open(out_file, 'w') as out_f:
        first_group = True
        for line in in_file:
            post_group = json.loads(line)
            question = ''
            answer = ''
            for post in post_group['posts']:
                if 'com' in post:
                    if not question:
                        post_no = post['no']
                        question = f"{'-'*5}\n---{post_no}\n{clean_html(post['com'])}"
                    else:
                        answer += clean_html(post['com']) + '\n'
            if answer:
                output_dict = {
                    'question': question,
                    'answer': answer
                }
                if first_group:
                    first_group = False
                else:
                    out_f.write(",\n")
                out_f.write(json.dumps(output_dict, indent=4))
        out_f.write("\n]")

with open('data.ndjson', 'r') as in_f:
    process_posts(in_f, 'output.json')