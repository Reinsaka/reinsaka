import subprocess
import os
from pathlib import Path
file = input("dia gui image music\n")

ls = os.listdir('H:/desktop/web/'+ file + "/cover/")
for i in ls:
    path = 'H:/desktop/web/'+ file + "/cover/" + i
    name = 'H:/desktop/web/'+ file + "/cover/" + Path(i).stem +'.webp'
    if i.lower().endswith('.webp'):
        continue;
    else:
        subprocess.run([
            'ffmpeg', '-i', path,
            '-quality','80',
            name
]) 

print(ls)
