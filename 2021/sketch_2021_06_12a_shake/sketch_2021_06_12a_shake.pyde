import pickle
from collections import Counter

# from urllib.request import urlopen # Python 3
# from urllib2 import urlopen # Jython 2
# shakespeare = urlopen('http://inst.eecs.berkeley.edu/~cs61a/fa11/shakespeare.txt')
# words = list(shakespeare.read().decode().split())
# with open("words.pickle", "w") as f:
#     pickle.dump(words, f)
    
with open("words.pickle") as f:
    words = pickle.load(f)
    
word_frequency = Counter(words)
c = sorted(word_frequency.items(), key=lambda kv:kv[1])
for w, c in c[-40:-30]:
    print(w)

    
# Result:    
"""
all
do
thy
The
her
but
so
as
thou
will
"""
