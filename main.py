# from pathlib import Path
# repo = input('enter repo: ')
# p = Path()

# result = os.system(f'git clone {repo}')
import os
import time

os.system(f'git add .')
time.sleep(2)
com = input('enter commit')
os.system(f'git commit -m {com}')
time.sleep(2)
os.system(f'git push')
print('done')