from util import Queue, Stack

# reading in the file of words
f = open('words.txt', 'r')
words = f.read().split("\n")
f.close()

# create a set of the words from the file

word_set = set()
for word in words:
      word_set.add(word.lower())


# implement the function 
# along with any helper functions you need
def find_word_ladder(beginWord, endWord):
    pass