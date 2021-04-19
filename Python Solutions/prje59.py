
def enc(message:'list[int]', key:'list[int]') -> 'list[int]':
    encMessage = []
    
    for i in range(len(message)):
        encMessage.append(message[i] ^ key[i%len(key)])
    
    return encMessage

def freq(l:'list[int]'):
    return max(set(l), key = l.count)

rawtxt = open("Python Solutions\\prje59_text.txt","r+").read()

l = list(map(int,rawtxt.split(','))) # list of all characters in the encrypted message in ascii val form

lc = [i for i in range(97,123)]



