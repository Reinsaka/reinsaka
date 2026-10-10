import json
import os
import subprocess
from docx import Document
from pathlib import Path
#更新文本
BASE_DIR = Path(__file__).resolve().parent      # 脚本所在目录
text_file = str(BASE_DIR / 'dia' / 'text')
js_file = str(BASE_DIR / 'js' / 'textlist.json')
doc_list = os.listdir(text_file)


existing = {text_file + '/' + j for j in doc_list}#已有文件目录

with open(js_file, "r", encoding="utf-8") as f:
    data = json.load(f)#读json

new_data = []
for item in data:#item词典
    if item['doc'] in existing:
        new_data.append(item)
data1 = new_data#需要添加的文件词典



docs = []
for i in data1:
    docs.append(i['doc'])


for j in doc_list:#j 未有文件
    if "/dia/text/" + j not in docs:
        docls = Document(text_file + '/' + j)
        text = "<br>".join(p.text for p in docls.paragraphs)
        data1.append({"doc": "/dia/text/" + j, "text": text, "cover": "","title":Path(j).stem})

with open(js_file, "w", encoding="utf-8") as f:
    json.dump(data1, f, ensure_ascii=False, indent=2)

#更新音乐
music_file = str(BASE_DIR / 'music' / 'music')
music_list = os.listdir(music_file)#compare cover and music 
ls = []
js_file = str(BASE_DIR / 'js' / 'textlist.json')
with open(js_file, "r", encoding="utf-8") as f:
    data = json.load(f)
for i in music_list:
    
    ls.append(music_file + '/' + i)
for j in music_list:
    

    subprocess.run([
        'ffmpeg', '-y','-i', music_file + '/' + j,
        '-map', '0:v', '-c', 'copy',
        str(BASE_DIR / 'music' / 'cover' / (Path(j).stem + '.jpg'))
    ])
#p2wb
ls = []
file_list = ["dia","music"]
for file in file_list:
    ls = os.listdir(str(BASE_DIR / file / "cover/"))
    for i in ls:
        path = str(BASE_DIR / file / "cover/" / i)
        name = str(BASE_DIR / file / "cover/" /( Path(i).stem +'.webp'))
        if i.lower().endswith('.webp'):
            continue;
        else:
            subprocess.run([
                'ffmpeg','-y' ,'-i', path,
                '-quality','80',
                name
    ]) 

    print(ls)