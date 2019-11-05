 # How to Solve Any Graph Problem

* Here are steps to solve (almost) any graph problems:

1. Translate the problem into graph terminology
2. Build your graph
3. Traverse your graph


## Word Ladders Problem

```
Given two words (beginWord and endWord), and a dictionary's word list, return the shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return None if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
```

```
Sample:
beginWord = "hit"
endWord = "cog"
return: ['hit', 'hot', 'cot', 'cog']

beginWord = "sail"
endWord = "boat"
['sail', 'bail', 'boil', 'boll', 'bolt', 'boat']

beginWord = "hungry"
endWord = "happy"
None
```