from util import Queue, Stack

# reading in the file of words
f = open('words.txt', 'r')
words = f.read().split("\n")
f.close()

# create a set of the words from the file

word_set = set()
for word in words:
      word_set.add(word.lower())

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


# implement the function 
# along with any helper functions you need
def find_word_ladder(beginWord, endWord):
    pass



if __name__ == '__main__':
    print(find_word_ladder("sail", "boat"))