import re
import random
from datetime import date,timedelta
import pickle

from constants import PATH_TO_PICKLE_FILE

# get relevant raw data and random it:
file_name = 'common_words.txt'

with open (file_name,'r') as f:
  f = re.findall('[a-zA-Z]+', f.read())
  words = [i.lower() for i in f if len(i)==5]
  random.shuffle(words)

# create the words for each day ahead:
daily_words = {} 
date = date.today()
for index in range (len(words)):
  daily_words[date] = words[index]
  date = date + +timedelta(days=1)

# pickle it:
with open(PATH_TO_PICKLE_FILE, 'wb') as f:
  pickle.dump(daily_words,f)