from pathlib import Path

path = str(Path(__file__).parent)
file_path = path + '/1_ex.txt'

nums = []

numerics = ['one', 
            'two',
            'three',
            'four',
            'five',
            'six',
            'seven',
            'eight',
            'nine',]
pos = []
first = None
last = None

with open(file_path, 'r') as f:
    for line in f:
        for item in numerics:
            if line.find(item) != -1:
                pos.append(line.find(item))
        try:
            first = min(pos)
            last = max(pos)
        except ValueError:
            pass
        pos = []
        print(first, last)
            