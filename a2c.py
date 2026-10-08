import subprocess
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent      # 脚本所在目录
data_file = BASE_DIR / 'music' / 'music' / 

subprocess.run([
    'ffmpeg', '-i', 'H:/deskop/web/music/music/2.mp3',
    '-map', '0:v', '-c', 'copy',
    'H:/deskop/web/music/cover/2.jpg'
])