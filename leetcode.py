
def bfs (root, goal):
    final_queue.append(root)
    temp = []
    
    #Possible words
    for i in range(len(root)):
        for k in 'abcdefghijklmnopqrstuvwxyz':
            root_word = list(root)
            root_word[i] = k
            for key in dictionary:
                if ("".join(root_word) == key and dictionary[key] == 0):
                    temp.append(key)
                    dictionary[key] = 1
        
    #Check for word in list  
    wordInList = 1
    for i in range(len(temp)):
        if temp[i] == goal:
            final_queue.append(temp[i])
            print temp[i]
            wordInList = 0
            return 1
            
    #if word is not in first list go to first node and create another list and repeat
    if wordInList == 1:
        for i in range(len(temp)):
            value = bfs(temp[i], goal)
            print value
        
            if value == 1:
                print temp[i]
                return 1
            else:
                final_queue.remove(temp[i])

                    

dictionary = {}

startWord = raw_input('write a start word: ')
endWord = raw_input('write an ending word: ')

length = len(startWord)
#open the words file
with open("words.txt") as text:
    #Scan each word and assign it to line
    for line in text:
       key = line.strip()
       dictionary[key] = 0

               
           
           
           
final_queue = []

dictionary[startWord] = 1
print final_queue.get([0])

#for word in dictionary:
 #   print dictionary[word], word
e = 0
bfs(startWord, endWord)
for word in final_queue:
    print word

           
           
       

           
       
