# Project 2: Solving Problems by Searching

*If you choose, you may work with a partner to complete this
assignment.*

**Due Sunday, February 26 at 11:59 PM**

## Description



## Warm-Up: Anagrams

Find all of the anagrams in the word list. Your program should
scan through the word list and print each group of words with the
same letters on a single line. For example,

```
    ['buffered', 'rebuffed']
    ['biders', 'brides', 'debris', 'rebids']
    ['gateman', 'magenta', 'magnate']
    ['stewed', 'tweeds']
    ['basest', 'basset', 'bastes', 'beasts']
    ['rationalizes', 'realizations']
    ['night', 'thing']
    ['dares', 'dears', 'rased', 'reads']
```   
   
You could do this by comparing every word in the word list to
every other word and seeing if they contain the same letters, but
that would have O(N^2) complexity, which is lame.

A better solution makes only one pass through the list using a
dictionary to store all of the sets of words with the same letters.
The values in the dictionary would be the lists of words that are
anagrams of each other. What shoud the keys be?

Hints:
    - If word is a string, what is sorted(word)?
    - You can turn a list into a tuple using tuple()
    - Tuples can be dictionary keys
    
    
    
## Word Ladders

This is inspired by a problem from `leetcode.com`.

Given a start_word and an end_word, generate a chain of words that 
connects the two. Each word in the chain may differ from the previous
word by only one letter.

For example,

```    
    dog
    cog
    cot
    cat
``` 

You may assume the length of the word remains constant. Use `words.txt`
as your reference.

Find a ladder connecting snakes and brains.

Hint: For fast word lookups, make a dictionary with all of the words
in the list as its keys. The values for each key can be anything.
You can then check if a word is in the list using

```
if word in all_words:
```

## Boggle

Boggle is a popular word game played with a 4x4 grid of letter dice.
The goal is to identify the most words in the grid by connecting
letters horizontally, vertically, or diagonally.

For example, for the grid

```
u n t h
g a e s
s r t r
h m i a
```

some of the words you can generate include tars, hermits, gates,
miters, great, irate, guar, and gathers.

The same grid position can't be used multiple times in one word.

Write a program that can find as many words as possible in a 4x4
grid. Any word in words.txt is valid.

I recommend having a search method that takes a starting location in
the grid as its input argument. The search routine then returns all
the words that can be built off of that starting letter. For example,
search(1, 3) would return all words that can be built starting with
the s in the second row. Call this method 16 times, once for each 
starting position.

Some other considerations:

    - Use the example grid for testing.

    - You'll need a way to keep track of the sequence of letters
    belonging to each candidate word, to ensure that you don't use
    the same square twice. A list of tuples might do the job. For
    example, 
        
        ```
        [(1, 3), (2, 2), (1, 1), (2, 1)]
        ```
        
    corresponds to the positions of the word star.
        
    - You can check if an item is in a list using the in operator:
    
    ```
        if position in position_list:
    ```
    
    - To make this efficient, you shouldn't waste time exploring
    paths that can't lead to solutions. For example, there are no
    words in the list that begin with gt-, fn-, or ds-, so those 
    prefixes can never lead to useful solutions and should be 
    dropped from the search. Perhaps a dictionary that stores all
    prefixes in the word list would help?
    
