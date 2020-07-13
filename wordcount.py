# put your code here.

import sys

file = open(sys.argv[1])   # first real argument
#for data in open(file):
    #print(data)

#file = open('test.txt')

all_lines = []
for line in file:
    line = line.rstrip()
    full_line = line.split(' ')
    for word in full_line:
        all_lines.append(word)

word_count = {}
for item in all_lines:
    item = item.rstrip('.,:?";!()"''')
    item = item.lower()
    word_count[item] = word_count.get(item, 0) + 1    

sorted_dict = sorted((value, key) for (key,value) in word_count.items())  
sorted_dict.reverse()
for index,value in sorted_dict:
    print(value, index)

    
#print(word_count.items())     

#print(word_count)



"""all_lines = []
for line in file:
    line = line.rstrip()
    full_line = line.split(' ')
    for word in full_line:
        all_lines.append(word)

word_count = {}
for item in all_lines:
    item = item.rstrip('.,:?";!()"''')
    item = item.lower()
    word_count[item] = word_count.get(item, 0) + 1 

print(word_count)"""    