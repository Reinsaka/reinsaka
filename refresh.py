import json
import os
from docx import Document
from pathlib import Path
#更新文本
BASE_DIR = Path(__file__).resolve().parent      # 脚本所在目录
text_file = str(BASE_DIR / 'dia' / 'text')
js_file = str(BASE_DIR / 'js' / 'textlist.json')
doc_list = os.listdir(text_file)


existing = {text_file + '/' + j for j in doc_list}

with open(js_file, "r", encoding="utf-8") as f:
    data = json.load(f)
new_data = []
for item in data:
    if item['doc'] in existing:
        new_data.append(item)
data = new_data


docs = []
for i in data:
    docs.append(i['doc'])


for j in doc_list:
    if "/dia/text/" + j not in docs:
        docls = Document(text_file + '/' + j)
        text = "<br>".join(p.text for p in docls.paragraphs)
        data.append({"doc": "/dia/text/" + j, "text": text, "cover": ""})

with open(js_file, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)