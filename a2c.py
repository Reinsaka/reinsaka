import subprocess
from pathlib import Path
import os
import json
BASE_DIR = Path(__file__).resolve().parent      # 脚本所在目录
data_file = str(BASE_DIR / 'music' / 'music')
music_list = os.listdir(data_file)#compare cover and music 
ls = []
js_file = str(BASE_DIR / 'js' / 'textlist.json')
with open(js_file, "r", encoding="utf-8") as f:
    data = json.load(f)
for i in music_list:
    
    ls.append(data_file + '/' + i)
for j in music_list:

    subprocess.run([
        'ffmpeg', '-i', data_file + '/' + j,
        '-map', '0:v', '-c', 'copy',
        str(BASE_DIR / 'music' / 'cover' / (j + '.jpg'))
    ])