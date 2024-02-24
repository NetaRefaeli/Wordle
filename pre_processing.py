import re
import random
from datetime import date,timedelta,datetime
import pickle

# get relevant raw data and random it:
file_name = 'nouns.txt'
with open(file_name,'r') as f:
  words = [line.replace('\n','') for line in f if len(re.search('[א-ת]+',line).group() )== 5]
  random.shuffle(words) # need plant a seed!

# create the words for each day ahead:
history = {} 
date = date.today()
for index in range (len(words)):
  history[date] = words[index]
  date = date + +timedelta(days=1)

# pickle it:
with open('history.pickle', 'wb') as f:
  pickle.dump(history,f)