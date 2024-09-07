from pathlib import Path

path = str(Path(__file__).parent)
file_path = path + '/1_ex.txt'

nums = []

with open(file_path, 'r') as f:
    for line in f:

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
print(total)
  