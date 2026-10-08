import json
import os
from docx import Document
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent      # 脚本所在目录
data_file = str(BASE_DIR / 'dia' / 'text' )
js_file = str(BASE_DIR / 'js' / 'textlist.json')
doc_list = os.listdir(data_file)

with open(js_file, "r", encoding="utf-8") as f:
    data = json.load(f)

docs = []
for i in data:
    docs.append(i['doc'])
#html换行是<br>
for j in doc_list:
    
    docls = Document(data_file +'/'+ j)
    
    if "/dia/text/" + j not in docs:
        
        text = "<br>".join(p.text for p in docls.paragraphs)
        data.append({"doc": "/dia/text/" + j, "text": text, "cover": ""})

with open(js_file, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

