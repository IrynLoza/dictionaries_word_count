# put your code here.

import sys

file = open(sys.argv[1])   # first real argument

#file = open('test.txt')

def get_words(file):
    """Get words from file"""

    all_words = []
    for line in file:
        line = line.rstrip()
        full_line = line.split(' ')
        for word in full_line:
            all_words.append(word)

    return all_words 

#get_words(file)

def count_words_in_dict(all_words):
    """Create dictionary with count of how many times
    every word appears"""

    word_count = {}
    for item in all_words:
        item = item.rstrip('.,:?";!()"_''')
        item = item.lower()
        word_count[item] = word_count.get(item, 0) + 1  

    return word_count 

def sort_dict(dictionary):
    """Sort dictionary"""

    sorted_dict = sorted((value, key) for (key,value) in dictionary.items())  
    sorted_dict.reverse()
    new_dict = {}
    for index,value in sorted_dict:
        new_dict[value] = index

    print(new_dict)    
    return new_dict         

def print_words():
    """Print sorted words with count"""

    words = get_words(file)
    word_count = count_words_in_dict(words)
    result = sort_dict(word_count)
    for (key, value) in result.items():
        print(f'{key}: {value}')

print_words()
