from nltk import tokenize
from bookv2 import html

import pandas as pd
import numpy as np
import nltk 


import re
import random
import matplotlib.pyplot as plt
import string

from nltk.tokenize import word_tokenize, sent_tokenize

chap1 = html[5]
chap2 = html[6]
chap3 = html[7]
chap4 = html[8]
chap5 = html[9]
chap6 = html[10]
chap7 = html[11]
chap8 = html[12]
chap9 = html[13]
chap10 = html[14]
chap11 = html[15]
chap12 = html[16]
chap13 = html[17]
chap14 = html[18]
chap15 = html[19]
chap16 = html[20]
chap17 = html[21]
chap18 = html[22]
chap19 = html[23]
chap20 = html[24]

print(chap1)


# from nltk.corpus import stopwords
# stop_words=stopwords.words("english")

# import string
# punct = list(string.punctuation)

# # [‘!’, ‘“‘, ‘#’, ‘$’, ‘%’, ‘&’, “‘“, ‘(‘, ‘)’, ‘*’, ‘+’, ‘,’, ‘-’] 
# # There are 32 punctuation marks.
# stops = stop_words + punct + ["''", 'r.', '``', "'s", "n't"]

# tokenized_chap = word_tokenize(chap1)

# filtered_words=[]
# for w in tokenized_chap:
#     if w.lower() in stops:
#         filtered_words.append(w.lower())

# # [‘game’, ‘thrones’, ‘book’, ‘one’, ‘song’, ‘ice’, ‘fire’, ‘george’]