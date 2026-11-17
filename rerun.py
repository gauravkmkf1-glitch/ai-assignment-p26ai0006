import json, sys, io, os
os.chdir(r'C:\Users\ACER\Documents\New folder\evaluation_run')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
nb = json.load(open('reasoning_agent.ipynb', encoding='utf-8'))
G = {}
for i, c in enumerate(nb['cells']):
    if c['cell_type'] != 'code' or i == 11:
        if i == 11:
            print('(cell 11 public-set evaluation skipped here; it does not affect submission.csv)')
        continue
    exec(compile(''.join(c['source']), 'cell_%d' % i, 'exec'), G)
