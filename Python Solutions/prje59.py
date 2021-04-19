from time import time

def valid(x:int) -> bool:
    chx = chr(x)

    lbools = [ # bro im litterally crying why is this a thing
        'a'<= chx <='z', # 97 to 122
        'A'<= chx <='Z', # 65 to 90
        chx == ' ',      # 32
        chx == '\'',     # 39
        chx == ',',      # 44
        chx == '"',      # 34
        chx == '[',      # 91
        chx == ']',      # 93
        chx == ':',      # 58
        '0'<= chx <='9', # 48 - 57
        chx == '/',      # 47
        chx == '.',      # 46
        chx == '(',      # 40
        chx == ')',      # 41
        chx == ';',      # 59
        chx == '+'       # 43
    ]

    return any(lbools)
    
def enc(message:'list[int]', key:'list[int]') -> 'list[int]':
    encMessage = []
    
    for i in range(len(message)):
        encMessage.append(message[i] ^ key[i % len(key)])
    
    return encMessage

st = time()

rawtxt = open("Python Solutions\\prje59_text.txt","r+").read().strip()

l = list(map(int,rawtxt.split(','))) # list of all characters in the encrypted message in ascii val form

lc = range(97,123)

key = [set(),set(),set()]

for k in range(3):
    for a in lc:
        for i in range(k, len(l), 3):
            key[k].add(a)
            if not valid(a ^ l[i]):
                key[k].remove(a)
                break
    key[k] = list(key[k])[0]

decrypted = enc(l,key)

print(f"The sum of the decrypted acii is {sum(decrypted)}")
print(f"Time taken : {time() - st} \n")
#Avg Time Taken: 2E-3 seconds

# While the previous print statement was the answer, i kinda wanna see the full decrypted message...
print(''.join(list(map(chr,decrypted))))

# Oh it's more stuff about euler!
# neato


