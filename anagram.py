
#declare a dictionary
dictionary = {}

#Open file and create a key with the sorted letter of the word read.
#add the actual word as a value to the dictionary
with open("words.txt") as text:
    for line in text: 
        key = ''.join(sorted(line))
        val = line.strip()
        dictionary.setdefault(key,[]).append(val)
        
#print only the words that have similar letters
for word in dictionary: 
    if len(dictionary[word]) > 1:
        print dictionary[word]
    
