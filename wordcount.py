# put your code here.

import sys

file = open(sys.argv[1])   # first real argument

#file = open('test.txt')

def get_words(file):

    all_words = []
    for line in file:
        line = line.rstrip()
        full_line = line.split(' ')
        for word in full_line:
            all_words.append(word)

    return all_words 

get_words(file)

word_count = {}
for item in all_lines:
    item = item.rstrip('.,:?";!()"''')
    item = item.lower()
    word_count[item] = word_count.get(item, 0) + 1    

def sort_dict(dictionary):
    """Sort dictionary"""

    sorted_dict = sorted((value, key) for (key,value) in dictionary.items())  
    sorted_dict.reverse()
    for index,value in sorted_dict:
        print(value, index)

sort_dict(word_count)

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