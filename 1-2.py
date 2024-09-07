import re
from pathlib import Path

path = str(Path(__file__).parent)
file_path = path + '/1_input.txt'

nums = []

numerics = {'one' : '1xx', 
            'two' : '2xx',
            'three' : '3xxxx',
            'four' : '4xxx',
            'five' : '5xxx',
            'six' : '6xx',
            'seven': '7xxxx',
            'eight': '8xxxx',
            'nine' : '9xxx',}
pos = []
first = None
last = None
file = []

with open(file_path, 'r') as f:
    for line in f:
        file.append(line.strip())
        # print(line)
        # get the positions of the numerics
        for key in numerics:
            if line.find(key) != -1:
                # error, only finds the first key in the string sixninesix doesn't work
                pos.append(line.find(key))
                #pos.append(line.rfind(key))
        try:
            first = min(pos)
            last = max(pos)
        except ValueError:
            pass
        pos = []
        #print(first, last)
        try:
            for key, value in numerics.items():
                if key in line[first:len(key) + first]:
                    line = line.replace(key, str(value))
                if key in line[last:len(key) + last]:
                    line = line.replace(key, str(value))
        except TypeError:
            pass
        #print(line)
        line_r = reversed(line)
        for item in line:
            if item.isnumeric():
                store = item
                break
        #print(store)
        for item2 in line_r:
            if item2.isnumeric():
                store2 = item2
                break
        #print(store2)
        nums.append(store + store2)
total = 0
for num in nums:
    total += int(num)
    #print(num)

print(total)