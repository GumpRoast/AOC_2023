from pathlib import Path

path = str(Path(__file__).parent)
file_path = path + '/1_ex.txt'

with open(file_path, 'r') as f:
    for line in f:
        for item in line:
            if item.isnumeric():
                store = item
                break
        
        print(store)

