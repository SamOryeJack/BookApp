from bookv2 import html

import pandas as pd
import numpy as np
import nltk
import re
import random
import matplotlib.pyplot as plt
import string

from nltk.tokenize import word_tokenize, sent_tokenize


got1 = html
got = html

text = ' '.join(html)
my_list = text.split(' ')
test = ' '.join(my_list)


punct = list(string.punctuation)

# print('There are', len(punct), 'punctuation marks.')
# [‘!’, ‘“‘, ‘#’, ‘$’, ‘%’, ‘&’, “‘“, ‘(‘, ‘)’, ‘*’, ‘+’, ‘,’, ‘-’] 
# There are 32 punctuation marks.

stops = ["''", 'r.', '``', "'s", "n't"]
filtered_words=[]
for w in my_list:
    if w.lower() not in stops:
        filtered_words.append(w.lower())

# [‘game’, ‘thrones’, ‘book’, ‘one’, ‘song’, ‘ice’, ‘fire’, ‘george’]
