#!/usr/bin/env python

import random
import sys

importfile = sys.argv[1]
count = int(sys.argv[2])

with open(importfile) as f:
    input = f.read()

dict_of_words = {}
output = []
list_of_words = input.split()
list_of_words_count = len(list_of_words)

for i in range(list_of_words_count-2):
    key = (list_of_words[i], list_of_words[i+1])
    if key in dict_of_words:
        dict_of_words[key].append(list_of_words[i+2])
    else:
        dict_of_words[key] = [list_of_words[i+2]]

rand = random.randint(0, list_of_words_count-3)
w1, w2 = list_of_words[rand], list_of_words[rand+1]

for i in range(count-1):
    output.append(w1)
    w1, w2 = w2, random.choice(dict_of_words[(w1, w2)])

output.append(w2)
print ' '.join(output)


