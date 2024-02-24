import re
import random
from datetime import date,timedelta,datetime
import pickle

# get relevant raw data and random it:
file_name = 'wordlist.js'
with open (file_name,'r',encoding='utf-8') as f:
  words = re.findall('[א-ת]+', f.read())
  random.shuffle(words)

# create the words for each day ahead:
history = {} 
date = date.today()
for index in range (len(words)):
  history[date] = words[index]
  date = date + +timedelta(days=1)

# pickle it:
with open('history.pickle', 'wb') as f:
  pickle.dump(history,f)