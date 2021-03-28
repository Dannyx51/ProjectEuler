rawtxt = open("Python Solutions\\prje59_text.txt","r+").read()

l = list(map(int,rawtxt.split(','))) # list of all characters in the encrypted message in ascii val form

# idk i dont wanna do cryptanalysis