
import random

def createBoard():
    """This will return the dictionary with a key letter pair"""
    return {(x, y): random.choice('abcdefghijklmnopqrstuvwxyz') for x in range(n) for y in range(n)}

    """get the keys in the board and pull the letters from the board dictionary
    check the surrounding for possible paths. 
    makes sure the code stays within boundaries"""
def neighborhood():
    neigh = {}


    for position in board:
        
        x, y = position
        
        positions = [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x + 1, y),
                     (x + 1, y + 1), (x, y + 1), (x - 1, y + 1), (x - 1, y)]
                     
        
        neigh[position] = [p for p in positions if 0 <= p[0] < n and 0 <= p[1] < n]
        
    return neigh

    """This is taking the list of keys (x,y) taking the letters and return a
        word to each in the dictionary"""
def cell_list(path):

    #print([board[p] for p in path])
    return ''.join([board[p] for p in path])

    """Checks the list of possible words agaisnt the dictionary to find
    a match. after it gets the path, it goes on to fin the next word"""
def search(path):

    word = cell_list(path)
    if word not in possible:
        return
    if word in dictionary:
        paths.append(path)
    for next_pos in neighbours[path[-1]]:
        if next_pos not in path:
            search(path + [next_pos])


    """looks for all possible words plus itself and adds them to a set"""
def dictionary():

    possible, dictionary = set(), set()
    with open('words.txt') as text:
        for word in text:
            word = word.strip()
            dictionary.add(word)

            for i in range(len(word)):
                possible.add(word[:i + 1])

    return dictionary, possible

def get_words():
    """ get the letters and show the word"""
    match_word = []
    for position in board:
        search([position])
    for p in paths:
        found = 1
        for word in match_word:
            if cell_list(p) == word:
                found = 0
        if found:
            match_word.append(cell_list(p))

    return match_word

def print_board(board):
    s = ''
    for y in range(n):
        for x in range(n):
            s += board[x, y] + ' '
        s += '\n'
    print s

n = int(raw_input('Enter board size inf the format n X n: '))

board = createBoard()

neighbours = neighborhood()
dictionary, possible = dictionary()
paths = []
print_board(board)
matches =  get_words()
print get_words()

            